from __future__ import annotations

import fitz  # PyMuPDF

from .config import ImpositionConfig, PresetMode, OrderMode
from .layouts import A4_W, A4_H, draw_guides, get_slots_for_preset
from .order import make_64up_order, make_64up_order_stackable
from .utils import validate_pdf_paths, validate_rotation


def impose_pdf(config: ImpositionConfig) -> None:
    """
    根据 ImpositionConfig 执行 PDF 拼版。
    这版接口与 cli.py 保持一致：cli 直接传入 config 对象。
    """

    validate_pdf_paths(config.input_pdf, config.output_pdf)
    validate_rotation(config.rotate_each)

    src = fitz.open(str(config.input_pdf))
    n = src.page_count

    # -------- 页序 --------
    if config.order_mode == OrderMode.STACK_AFTER_CUT:
        page_order = make_64up_order_stackable(n)
    elif config.order_mode == OrderMode.CLASSIC:
        page_order = make_64up_order(n)
    else:
        raise ValueError(f"Unsupported order_mode: {config.order_mode}")

    # -------- 槽位 --------
    slots = get_slots_for_preset(
        preset=config.preset.value,
        margin_mm=config.margin_mm,
        _gap_mm_unused=config.gap_mm,
    )

    out = fitz.open()

    i = 0
    per_side = len(slots)  # 4
    side_index = 0

    while i < len(page_order):
        out_page = out.new_page(width=A4_W, height=A4_H)

        if config.draw_guides:
            draw_guides(out_page, preset=config.preset.value)

        is_back_side = (side_index % 2 == 1)

        for slot_idx in range(per_side):
            if i >= len(page_order):
                break

            pno = page_order[i]
            i += 1

            if pno is None:
                continue

            src_page_index = pno - 1

            rot = config.rotate_each
            if config.back_rotate_180 and is_back_side:
                rot = (rot + 180) % 360

            out_page.show_pdf_page(
                slots[slot_idx],
                src,
                src_page_index,
                rotate=rot,
            )

        side_index += 1

    out.save(str(config.output_pdf))
    out.close()
    src.close()
from __future__ import annotations

import fitz  # PyMuPDF

# A4 纸尺寸（PDF point，72dpi）
A4_W, A4_H = fitz.paper_size("a4")


def mm_to_pt(mm: float) -> float:
    return mm * 72.0 / 25.4


def _base_quadrants(margin_mm: float) -> tuple[fitz.Rect, fitz.Rect, fitz.Rect, fitz.Rect]:
    """
    返回最基础的 2x2 四个象限矩形：
    左上、右上、左下、右下
    """
    m = mm_to_pt(margin_mm)
    mid_x = A4_W / 2
    mid_y = A4_H / 2

    lt = fitz.Rect(m, m, mid_x - m, mid_y - m)
    rt = fitz.Rect(mid_x + m, m, A4_W - m, mid_y - m)
    lb = fitz.Rect(m, mid_y + m, mid_x - m, A4_H - m)
    rb = fitz.Rect(mid_x + m, mid_y + m, A4_W - m, A4_H - m)

    return lt, rt, lb, rb


def get_slots_for_preset(preset: str, margin_mm: float, _gap_mm_unused: float = 0.0) -> list[fitz.Rect]:
    """
    按 preset 返回 4 个槽位。

    vertical:
        逻辑上按“上半/下半”分组
        顺序：左上、右上、左下、右下

    horizontal:
        几何位置仍是 2x2，但逻辑上按“左半/右半”分组。
        为了实现“左侧书脊”，每一列内部再做一次上下交换：
        顺序：左下、左上、右下、右上
        这样相当于把横版结果页的上下两侧全部交换。
    """
    lt, rt, lb, rb = _base_quadrants(margin_mm)

    if preset == "vertical":
        return [lt, rt, lb, rb]

    if preset == "horizontal":
        # 左右两沓 + 左侧书脊：
        # 先左列，再右列；并且每列内部上下交换
        return [lb, lt, rb, rt]

    raise ValueError(f"Unsupported preset: {preset}")


def _draw_guide_line(page, p1, p2, line_width: float = 0.5) -> None:
    """
    画辅助线。

    这里故意不用 dashes 参数。
    原因是当前项目生成的某些 PDF 在浏览器查看器（尤其 Edge）里
    可能因为虚线内容流兼容性问题而显示为空白。

    先统一改成实线，优先保证 PDF 输出的兼容性和可见性。
    """
    page.draw_line(
        p1,
        p2,
        color=(0, 0, 0),
        width=line_width,
    )


def draw_guides(page, preset: str, line_width: float = 0.5) -> None:
    """
    画辅助线。

    vertical:
        - 一条整页竖线
        - 一条整页横线

    horizontal:
        - 一条整页竖线（主裁切线）
        - 左半页内部一条横线
        - 右半页内部一条横线
    """
    mid_x = A4_W / 2
    mid_y = A4_H / 2

    if preset == "vertical":
        _draw_guide_line(page, (mid_x, 0), (mid_x, A4_H), line_width)
        _draw_guide_line(page, (0, mid_y), (A4_W, mid_y), line_width)
        return

    if preset == "horizontal":
        _draw_guide_line(page, (mid_x, 0), (mid_x, A4_H), line_width)
        _draw_guide_line(page, (0, mid_y), (mid_x, mid_y), line_width)
        _draw_guide_line(page, (mid_x, mid_y), (A4_W, mid_y), line_width)
        return

    raise ValueError(f"Unsupported preset: {preset}")
import argparse
import fitz  # PyMuPDF

# A4 纸尺寸（PDF point，72dpi）
A4_W, A4_H = fitz.paper_size("a4")


def make_64up_order(n_pages: int):
    """
    旧逻辑：保持你现在一直在用的排版顺序。

    每张 A4 纸（两面）用 8 个小页：
      正面：左上 A(=X-4s)，右上 a(=4s+1)，左下 C(=X-2-4s)，右下 c(=4s+3)
      背面：左上 b(=4s+2)，右上 B(=X-1-4s)，左下 d(=4s+4)，右下 D(=X-3-4s)

    这和你“例子.pdf”的结构一致：第一页、第三页、X、X-2；背面第二页、第四页、X-1、X-3。:contentReference[oaicite:1]{index=1}
    缺点是：从中间撕开后，通常需要手动上下穿插整理。
    """
    padded = n_pages if n_pages % 8 == 0 else ((n_pages + 7) // 8) * 8
    order = []
    sheets = padded // 8

    for s in range(sheets):
        a = 4 * s + 1
        b = a + 1
        c = a + 2
        d = a + 3

        A = padded - 4 * s
        B = A - 1
        C = A - 2
        D = A - 3

        # 正面：左上 A，右上 a，左下 C，右下 c
        order.extend([A, a, C, c])

        # 背面：左上 b，右上 B，左下 d，右下 D
        order.extend([b, B, d, D])

    order = [p if 1 <= p <= n_pages else None for p in order]
    return order


def make_64up_order_stackable(n_pages: int):
    """
    新逻辑：撕开后可直接整沓叠放，无需手动上下穿插。

    目标：
    - 中间横向撕开后，得到“上半沓”和“下半沓”
    - 直接把“上半沓”整沓放到“下半沓”上面，就是正确顺序

    思路：
    - 一个“半张”对应一个 4 页小册子单元
    - 旧逻辑每张纸放相邻两个半张，导致撕开后需要上下交替穿插
    - 新逻辑每张纸的上半放“前半段”的半张，下半放“后半段”的半张
      这样撕开后两沓天然分成前半册和后半册，直接整叠即可
    """
    padded = n_pages if n_pages % 8 == 0 else ((n_pages + 7) // 8) * 8
    sheets = padded // 8               # A4 张数
    half_units = padded // 4           # 半张小册子单元数
    half_point = half_units // 2       # 前半段 / 后半段分界

    order = []

    for s in range(sheets):
        # 上半张：前半段
        k_top = s

        # 下半张：后半段
        k_bottom = s + half_point

        # ---- 上半张的 4 页 ----
        top_L = padded - 2 * k_top
        top_r1 = 2 * k_top + 1
        top_r2 = 2 * k_top + 2
        top_R = padded - 2 * k_top - 1

        # ---- 下半张的 4 页 ----
        bot_L = padded - 2 * k_bottom
        bot_r1 = 2 * k_bottom + 1
        bot_r2 = 2 * k_bottom + 2
        bot_R = padded - 2 * k_bottom - 1

        # 正面：左上=上半左，右上=上半右，左下=下半左，右下=下半右
        order.extend([top_L, top_r1, bot_L, bot_r1])

        # 背面：左上=上半背左，右上=上半背右，左下=下半背左，右下=下半背右
        order.extend([top_r2, top_R, bot_r2, bot_R])

    order = [p if 1 <= p <= n_pages else None for p in order]
    return order


def get_slots_2x2(margin_mm: float, _gap_mm_unused: float = 0.0):
    """
    把 A4 按中心线平均分成四块：
      - 中心竖线 x = A4_W / 2
      - 中心横线 y = A4_H / 2

    每块内部再留 margin_mm 的白边，返回四个矩形框：
    顺序：左上、右上、左下、右下
    """
    mm_to_pt = 72 / 25.4
    m = margin_mm * mm_to_pt

    mid_x = A4_W / 2
    mid_y = A4_H / 2

    slots = [
        # 左上
        fitz.Rect(m, m, mid_x - m, mid_y - m),
        # 右上
        fitz.Rect(mid_x + m, m, A4_W - m, mid_y - m),
        # 左下
        fitz.Rect(m, mid_y + m, mid_x - m, A4_H - m),
        # 右下
        fitz.Rect(mid_x + m, mid_y + m, A4_W - m, A4_H - m),
    ]
    return slots


def draw_guides(page, line_width: float = 0.5):
    """
    在整张 A4 上画两条等分线（虚线）：
    竖直通过 A4 中点，水平通过 A4 中点。
    """
    mid_x = A4_W / 2
    mid_y = A4_H / 2

    # 竖线
    page.draw_line(
        (mid_x, 0),
        (mid_x, A4_H),
        color=(0, 0, 0),
        width=line_width,
        dashes=[3, 3],
    )

    # 横线
    page.draw_line(
        (0, mid_y),
        (A4_W, mid_y),
        color=(0, 0, 0),
        width=line_width,
        dashes=[3, 3],
    )


def impose_64up(input_pdf: str,
                output_pdf: str,
                margin_mm: float = 8.0,
                gap_mm: float = 0.0,
                rotate_each: int = 0,
                stack_after_cut: bool = False):
    """
    把单页 PDF 拼到 A4 上。

    参数：
    - input_pdf: 输入 PDF
    - output_pdf: 输出 PDF
    - margin_mm: 每个小页留白
    - gap_mm: 兼容保留参数，目前不使用
    - rotate_each: 每个小页统一旋转角度
    - stack_after_cut:
        False -> 旧逻辑（默认）
        True  -> 新逻辑：撕开后两沓纸可直接整叠
    """
    src = fitz.open(input_pdf)
    n = src.page_count

    if stack_after_cut:
        page_order = make_64up_order_stackable(n)
    else:
        page_order = make_64up_order(n)

    slots = get_slots_2x2(margin_mm, gap_mm)
    out = fitz.open()

    i = 0
    per_side = len(slots)  # 4 个小区域

    while i < len(page_order):
        out_page = out.new_page(width=A4_W, height=A4_H)

        # 画分割线
        draw_guides(out_page)

        for slot_idx in range(per_side):
            if i >= len(page_order):
                break

            pno = page_order[i]
            i += 1

            if pno is None:
                continue

            src_page_index = pno - 1

            out_page.show_pdf_page(
                slots[slot_idx],
                src,
                src_page_index,
                rotate=rotate_each
            )

    out.save(output_pdf)
    out.close()
    src.close()


def main():
    ap = argparse.ArgumentParser(
        description=(
            "把单页 PDF 按 64 开方式拼到 A4 上（2x2，每张纸 8 页，带等分线）。"
            "默认使用旧排版逻辑；若加 --stack-after-cut，则启用“撕开后直接整沓叠放”模式。"
        )
    )
    ap.add_argument("-i", "--input", required=True, help="输入 PDF 文件路径")
    ap.add_argument("-o", "--output", required=True, help="输出 PDF 文件路径")
    ap.add_argument("--margin-mm", type=float, default=4.0,
                    help="每个小页离边界的白边（mm）")
    ap.add_argument("--gap-mm", type=float, default=0.0,
                    help="兼容参数，不再使用，可随便填")
    ap.add_argument("--rotate", type=int, default=0,
                    help="每个小页额外旋转角度：0 / 90 / 180 / 270")
    ap.add_argument("--stack-after-cut", action="store_true",
                    help="启用新排版：从中间撕开后，不需要手动上下穿插，可直接把上半沓整沓放到下半沓上")

    args = ap.parse_args()

    # 简单校验旋转角度
    if args.rotate not in (0, 90, 180, 270):
        raise ValueError("--rotate 只能是 0 / 90 / 180 / 270")

    impose_64up(
        input_pdf=args.input,
        output_pdf=args.output,
        margin_mm=args.margin_mm,
        gap_mm=args.gap_mm,
        rotate_each=args.rotate,
        stack_after_cut=args.stack_after_cut
    )


if __name__ == "__main__":
    main()
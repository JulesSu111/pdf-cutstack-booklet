from __future__ import annotations


def _pad_to_multiple_of_8(n_pages: int) -> int:
    if n_pages <= 0:
        return 0
    return n_pages if n_pages % 8 == 0 else ((n_pages + 7) // 8) * 8


def make_64up_order(n_pages: int) -> list[int | None]:
    """
    经典页序：
    每张 A4（两面）放 8 个小页，顺序与原竖版脚本一致。

    正面：左上 A，右上 a，左下 C，右下 c
    背面：左上 b，右上 B，左下 d，右下 D

    其中：
      a = 4s+1
      b = 4s+2
      c = 4s+3
      d = 4s+4
      A = X-4s
      B = X-1-4s
      C = X-2-4s
      D = X-3-4s
    """
    padded = _pad_to_multiple_of_8(n_pages)
    order: list[int | None] = []
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

        # 正面
        order.extend([A, a, C, c])

        # 背面
        order.extend([b, B, d, D])

    return [p if 1 <= p <= n_pages else None for p in order]


def make_64up_order_stackable(n_pages: int) -> list[int | None]:
    """
    可整沓叠放页序：
    撕开后不必手动上下/左右交错穿插，直接把一整沓放到另一整沓上即可。

    这个函数只负责“前四格 / 后四格”的逻辑分组；
    真正是按“上下两沓”还是“左右两沓”，由 layouts.py 里的槽位顺序决定。
    """
    padded = _pad_to_multiple_of_8(n_pages)
    order: list[int | None] = []

    sheets = padded // 8
    half_units = padded // 4
    half_point = half_units // 2

    for s in range(sheets):
        # 第一沓对应的半张单元
        k1 = s

        # 第二沓对应的半张单元
        k2 = s + half_point

        # ---- 第一半张的 4 页 ----
        first_L = padded - 2 * k1
        first_r1 = 2 * k1 + 1
        first_r2 = 2 * k1 + 2
        first_R = padded - 2 * k1 - 1

        # ---- 第二半张的 4 页 ----
        second_L = padded - 2 * k2
        second_r1 = 2 * k2 + 1
        second_r2 = 2 * k2 + 2
        second_R = padded - 2 * k2 - 1

        # 正面：前两个槽给第一沓，后两个槽给第二沓
        order.extend([first_L, first_r1, second_L, second_r1])

        # 背面：前两个槽给第一沓，后两个槽给第二沓
        order.extend([first_r2, first_R, second_r2, second_R])

    return [p if 1 <= p <= n_pages else None for p in order]
from __future__ import annotations

import argparse

from .config import ImpositionConfig, OrderMode, PresetMode
from .core import impose_pdf



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Impose a PDF into A4 2x2 booklet pages. "
            "Supports vertical/horizontal presets and an optional cut-and-stack page order."
        )
    )
    parser.add_argument("-i", "--input", required=True, help="Input PDF path")
    parser.add_argument("-o", "--output", required=True, help="Output PDF path")
    parser.add_argument(
        "--preset",
        choices=[mode.value for mode in PresetMode],
        default=PresetMode.VERTICAL.value,
        help="Use built-in defaults for vertical or horizontal booklet jobs",
    )
    parser.add_argument(
        "--order-mode",
        choices=[mode.value for mode in OrderMode],
        default=OrderMode.CLASSIC.value,
        help="classic = original order, stack-after-cut = direct whole-stack merge after cutting",
    )
    parser.add_argument("--margin-mm", type=float, default=None, help="Inner margin inside each quadrant")
    parser.add_argument("--gap-mm", type=float, default=0.0, help="Reserved for future spacing support")
    parser.add_argument("--rotate", type=int, default=None, help="Rotate every imposed page: 0 / 90 / 180 / 270")
    parser.add_argument(
        "--back-rotate-180",
        action="store_true",
        help="Rotate the back side by an additional 180 degrees",
    )
    parser.add_argument(
        "--no-guides",
        action="store_true",
        help="Do not draw the center guide lines",
    )
    return parser



def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    preset = PresetMode(args.preset)
    order_mode = OrderMode(args.order_mode)

    config = ImpositionConfig.with_preset_defaults(
        input_pdf=args.input,
        output_pdf=args.output,
        preset=preset,
        order_mode=order_mode,
        margin_mm=args.margin_mm,
        gap_mm=args.gap_mm,
        rotate_each=args.rotate,
        back_rotate_180=args.back_rotate_180 if args.back_rotate_180 else None,
        draw_guides=not args.no_guides,
    )

    impose_pdf(config)
    print(f"Done: {config.output_pdf}")


if __name__ == "__main__":
    main()

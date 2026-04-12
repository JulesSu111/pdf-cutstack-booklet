from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class PresetMode(str, Enum):
    """High-level preset selected by the user."""
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


class OrderMode(str, Enum):
    """Page-ordering behavior."""
    CLASSIC = "classic"
    STACK_AFTER_CUT = "stack-after-cut"


@dataclass(slots=True)
class ImpositionConfig:
    input_pdf: Path
    output_pdf: Path
    preset: PresetMode = PresetMode.VERTICAL
    order_mode: OrderMode = OrderMode.STACK_AFTER_CUT
    margin_mm: float = 1.0
    gap_mm: float = 0.0
    rotate_each: int = 0
    back_rotate_180: bool = False
    draw_guides: bool = True

    @classmethod
    def with_preset_defaults(
        cls,
        *,
        input_pdf: str | Path,
        output_pdf: str | Path,
        preset: PresetMode,
        order_mode: OrderMode = OrderMode.STACK_AFTER_CUT,
        margin_mm: float | None = None,
        gap_mm: float = 0.0,
        rotate_each: int | None = None,
        back_rotate_180: bool | None = None,
        draw_guides: bool = True,
    ) -> "ImpositionConfig":
        preset_defaults = get_preset_defaults(preset)
        return cls(
            input_pdf=Path(input_pdf),
            output_pdf=Path(output_pdf),
            preset=preset,
            order_mode=order_mode,
            margin_mm=preset_defaults["margin_mm"] if margin_mm is None else margin_mm,
            gap_mm=gap_mm,
            rotate_each=preset_defaults["rotate_each"] if rotate_each is None else rotate_each,
            back_rotate_180=(
                preset_defaults["back_rotate_180"] if back_rotate_180 is None else back_rotate_180
            ),
            draw_guides=draw_guides,
        )


def get_preset_defaults(preset: PresetMode) -> dict[str, float | int | bool]:
    """Preset defaults."""
    if preset == PresetMode.VERTICAL:
        return {
            "margin_mm": 1.0,
            "rotate_each": 0,
            "back_rotate_180": False,
        }
    if preset == PresetMode.HORIZONTAL:
        return {
            "margin_mm": 1.0,
            "rotate_each": 0,
            "back_rotate_180": False,
        }
    raise ValueError(f"Unsupported preset: {preset}")
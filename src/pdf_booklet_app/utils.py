from __future__ import annotations

from pathlib import Path

MM_TO_PT = 72 / 25.4
VALID_ROTATIONS = {0, 90, 180, 270}


def validate_rotation(rotation: int) -> None:
    if rotation not in VALID_ROTATIONS:
        raise ValueError("rotate must be one of: 0, 90, 180, 270")



def validate_pdf_paths(input_pdf: Path, output_pdf: Path) -> None:
    if not input_pdf.exists():
        raise FileNotFoundError(f"Input PDF not found: {input_pdf}")
    if input_pdf.suffix.lower() != ".pdf":
        raise ValueError(f"Input file is not a PDF: {input_pdf}")
    if output_pdf.suffix.lower() != ".pdf":
        raise ValueError(f"Output file must end with .pdf: {output_pdf}")
    output_pdf.parent.mkdir(parents=True, exist_ok=True)



def pad_to_multiple(value: int, multiple: int) -> int:
    if value % multiple == 0:
        return value
    return ((value + multiple - 1) // multiple) * multiple

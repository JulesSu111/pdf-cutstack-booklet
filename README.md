# PDF Booklet App

A small but reusable Python project for imposing single-page PDFs onto A4 paper in a 2x2 booklet layout.

It already supports two workflows taken from your existing scripts:

- **vertical preset**: matches the defaults from your `pdf_64up.py`
- **horizontal preset**: matches the defaults from your `pdf_64upheng.py`
- **classic order**: your original booklet ordering
- **stack-after-cut order**: the new ordering where, after cutting, one half-stack can be placed directly onto the other

## Why this structure is better

This version is no longer "one big script".

- `cli.py` only handles command-line arguments
- `core.py` contains the main PDF processing service
- `order.py` contains page-order algorithms
- `layouts.py` contains A4 slot geometry and guide drawing
- `config.py` contains reusable configuration objects

That means you can later add:

- a GUI with Tkinter / PySide / custom web UI
- tests for page-order logic
- more presets and paper layouts
- packaging into a standalone desktop app

## Project structure

```text
pdf-booklet-app/
├─ archive/
│  ├─ original_horizontal.py
│  └─ original_vertical.py
├─ src/
│  └─ pdf_booklet_app/
│     ├─ __init__.py
│     ├─ cli.py
│     ├─ config.py
│     ├─ core.py
│     ├─ layouts.py
│     ├─ order.py
│     └─ utils.py
├─ .gitignore
├─ main.py
├─ pyproject.toml
├─ README.md
└─ requirements.txt
```

## Install

### Option 1: local run

```bash
pip install -r requirements.txt
```

### Option 2: install as a command

```bash
pip install -e .
```

Then you can use:

```bash
pdf-booklet --help
```

## Usage

### Vertical preset

```bash
python main.py -i input.pdf -o output.pdf --preset vertical
```

### Horizontal preset

```bash
python main.py -i input.pdf -o output.pdf --preset horizontal
```

### Cut-and-stack order

```bash
python main.py -i input.pdf -o output.pdf --preset horizontal --order-mode stack-after-cut
```

### Rotate the back side by 180 degrees

```bash
python main.py -i input.pdf -o output.pdf --preset horizontal --back-rotate-180
```

## CLI options

- `--preset vertical|horizontal`
- `--order-mode classic|stack-after-cut`
- `--margin-mm NUMBER`
- `--gap-mm NUMBER`
- `--rotate 0|90|180|270`
- `--back-rotate-180`
- `--no-guides`

## Recommended next steps

1. Add automated tests for `make_classic_order()` and `make_stackable_order()`.
2. Add support for more paper sizes and slot layouts.
3. Add a GUI layer that calls `impose_pdf(config)` directly.
4. Package it later with PyInstaller once the behavior is stable.

## Notes

The current implementation keeps the same core 2x2 A4 imposition logic from your two existing scripts. This refactor mainly improves structure, maintainability, packaging, and future extensibility.

from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
)

from .main_window import Ui_MainWindow
from .config import ImpositionConfig, PresetMode, OrderMode
from .core import impose_pdf


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("PDF Cut-Stack Booklet")

        self._init_form()
        self._connect_signals()

    def _init_form(self) -> None:
        self.ui.comboPreset.addItems(["vertical", "horizontal"])
        self.ui.comboRotate.addItems(["0", "90", "180", "270"])

        self.ui.spinMargin.setDecimals(1)
        self.ui.spinMargin.setRange(0.0, 50.0)
        self.ui.spinMargin.setValue(4.0)

        self.ui.checkDrawGuides.setChecked(True)
        self.ui.checkBackRotate180.setChecked(False)

        self._apply_preset_defaults()

    def _connect_signals(self) -> None:
        self.ui.buttonBrowseInput.clicked.connect(self._browse_input)
        self.ui.buttonBrowseOutput.clicked.connect(self._browse_output)
        self.ui.buttonGenerate.clicked.connect(self._generate_pdf)
        self.ui.comboPreset.currentTextChanged.connect(self._apply_preset_defaults)

    def _browse_input(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select input PDF",
            "",
            "PDF Files (*.pdf)"
        )
        if file_path:
            self.ui.lineEditInput.setText(file_path)

            # 自动填一个默认输出名
            input_path = Path(file_path)
            default_output = input_path.with_name(f"{input_path.stem}_booklet.pdf")
            if not self.ui.lineEditOutput.text().strip():
                self.ui.lineEditOutput.setText(str(default_output))

    def _browse_output(self) -> None:
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Select output PDF",
            "",
            "PDF Files (*.pdf)"
        )
        if file_path:
            if not file_path.lower().endswith(".pdf"):
                file_path += ".pdf"
            self.ui.lineEditOutput.setText(file_path)

    def _apply_preset_defaults(self) -> None:
        preset = self.ui.comboPreset.currentText()

        if preset == "vertical":
            self.ui.spinMargin.setValue(4.0)
            self.ui.comboRotate.setCurrentText("0")
            self.ui.checkBackRotate180.setChecked(False)
        elif preset == "horizontal":
            self.ui.spinMargin.setValue(1.0)
            self.ui.comboRotate.setCurrentText("90")
            self.ui.checkBackRotate180.setChecked(False)

    def _log(self, text: str) -> None:
        self.ui.plainTextLog.appendPlainText(text)

    def _generate_pdf(self) -> None:
        input_pdf = self.ui.lineEditInput.text().strip()
        output_pdf = self.ui.lineEditOutput.text().strip()

        if not input_pdf:
            QMessageBox.warning(self, "Missing input", "Please select an input PDF.")
            return

        if not output_pdf:
            QMessageBox.warning(self, "Missing output", "Please select an output PDF.")
            return

        try:
            config = ImpositionConfig.with_preset_defaults(
                input_pdf=input_pdf,
                output_pdf=output_pdf,
                preset=PresetMode(self.ui.comboPreset.currentText()),
                order_mode=OrderMode.STACK_AFTER_CUT,
                margin_mm=float(self.ui.spinMargin.value()),
                gap_mm=0.0,
                rotate_each=int(self.ui.comboRotate.currentText()),
                back_rotate_180=self.ui.checkBackRotate180.isChecked(),
                draw_guides=self.ui.checkDrawGuides.isChecked(),
            )

            self._log("Starting PDF generation...")
            self._log(f"Input: {input_pdf}")
            self._log(f"Output: {output_pdf}")
            self._log(f"Preset: {config.preset.value}")
            self._log(f"Order mode: {config.order_mode.value}")

            impose_pdf(config)

            self._log("Done.")
            QMessageBox.information(self, "Success", f"PDF generated:\n{output_pdf}")

        except Exception as exc:
            self._log(f"Error: {exc}")
            QMessageBox.critical(self, "Error", str(exc))


def run() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
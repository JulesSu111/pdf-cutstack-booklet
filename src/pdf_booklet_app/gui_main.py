from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
)

from .main_window import Ui_MainWindow
from .config import ImpositionConfig, PresetMode, OrderMode
from .core import impose_pdf


class MainWindow(QMainWindow):
    """
    Main GUI window for the PDF booklet app.

    Notes for future i18n:
    - All user-facing strings are grouped in self._texts.
    - Rotation combo uses display text + internal angle data separately.
    - Current implementation supports English / 中文 / Deutsch.
    """

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._language = "en"
        self._texts = self._build_texts()

        self._create_language_menu()
        self._apply_static_texts()
        self._init_form()
        self._connect_signals()

    def _build_texts(self) -> dict[str, dict[str, Any]]:
        return {
            "en": {
                "window_title": "PDF Cut-Stack Booklet",
                "menu_language": "Language",
                "labels": {
                    "input_file": "Input File",
                    "output_file": "Output File",
                    "input_layout": "Input PDF Layout",
                    "page_padding": "Page Padding",
                    "page_rotation": "Output Page Rotation",
                    "back_rotate_180": "Rotate back side by 180°",
                    "draw_guides": "Draw cut/fold guides",
                    "browse": "Browse...",
                    "generate": "Generate PDF",
                    "unit_mm": " mm",
                },
                "dialogs": {
                    "select_input_pdf": "Select Input PDF",
                    "select_output_pdf": "Select Output PDF",
                    "pdf_filter": "PDF Files (*.pdf)",
                    "missing_input_title": "Missing Input",
                    "missing_input_text": "Please select an input PDF.",
                    "missing_output_title": "Missing Output",
                    "missing_output_text": "Please select an output PDF.",
                    "success_title": "Success",
                    "success_text": "PDF generated:<br>{output_pdf}<br><br>{print_tip}",
                    "error_title": "Error",
                },
                "logs": {
                    "start": "Starting PDF generation...",
                    "input": "Input: {input_pdf}",
                    "output": "Output: {output_pdf}",
                    "preset": "Preset: {preset}",
                    "rotation": "Rotation: {rotation_label}",
                    "order_mode": "Order mode: {order_mode}",
                    "done": "Done.",
                    "print_tip": "Printing tip:<br>{print_tip}",
                    "error": "Error: {error}",
                },
                "tooltips": {
                    "experimental": "Experimental feature, not recommended to change.",
                },
                "print_tips": {
                    "vertical": (
                        "1. Please print in duplex mode with <b>long-edge flip</b>.<br>"
                        "2. Cut along the <b>shorter center line</b>.<br>"
                        "3. Stack the upper half onto the lower half.<br>"
                        "4. Fold."
                    ),
                    "horizontal": (
                        "1. Please print in duplex mode with <b>short-edge flip</b>.<br>"
                        "2. Cut along the <b>longer center line</b>.<br>"
                        "3. Stack the upper half onto the lower half.<br>"
                        "4. Fold."
                    ),
                },
                "preset_items": [
                    ("Vertical PDF", PresetMode.VERTICAL.value),
                    ("Horizontal PDF", PresetMode.HORIZONTAL.value),
                ],
                "rotation_items": [
                    ("No rotation", 0),
                    ("Rotate 90° clockwise", 90),
                    ("Rotate 180°", 180),
                    ("Rotate 90° counterclockwise", 270),
                ],
            },
            "zh": {
                "window_title": "PDF 裁切叠放小册子",
                "menu_language": "语言",
                "labels": {
                    "input_file": "输入文件",
                    "output_file": "输出文件",
                    "input_layout": "输入 PDF 版式",
                    "page_padding": "页边距",
                    "page_rotation": "输出页面旋转",
                    "back_rotate_180": "背面额外旋转 180°",
                    "draw_guides": "绘制裁切/折叠辅助线",
                    "browse": "浏览...",
                    "generate": "生成 PDF",
                    "unit_mm": " mm",
                },
                "dialogs": {
                    "select_input_pdf": "选择输入 PDF",
                    "select_output_pdf": "选择输出 PDF",
                    "pdf_filter": "PDF 文件 (*.pdf)",
                    "missing_input_title": "缺少输入文件",
                    "missing_input_text": "请选择输入 PDF。",
                    "missing_output_title": "缺少输出文件",
                    "missing_output_text": "请选择输出 PDF。",
                    "success_title": "成功",
                    "success_text": "PDF 已生成：<br>{output_pdf}<br><br>{print_tip}",
                    "error_title": "错误",
                },
                "logs": {
                    "start": "开始生成 PDF...",
                    "input": "输入：{input_pdf}",
                    "output": "输出：{output_pdf}",
                    "preset": "版式：{preset}",
                    "rotation": "旋转：{rotation_label}",
                    "order_mode": "排序模式：{order_mode}",
                    "done": "完成。",
                    "print_tip": "打印提示：<br>{print_tip}",
                    "error": "错误：{error}",
                },
                "tooltips": {
                    "experimental": "实验功能，不建议修改。",
                },
                "print_tips": {
                    "vertical": (
                        "1. 请使用双页打印 <b>长边翻转</b> 进行打印<br>"
                        "2. 沿 <b>较短中线</b> 裁开<br>"
                        "3. 上下叠放<br>"
                        "4. 折叠"
                    ),
                    "horizontal": (
                        "1. 请使用双页打印 <b>短边翻转</b> 进行打印<br>"
                        "2. 沿 <b>较长中线</b> 裁开<br>"
                        "3. 上下叠放<br>"
                        "4. 折叠"
                    ),
                },
                "preset_items": [
                    ("竖版 PDF", PresetMode.VERTICAL.value),
                    ("横版 PDF", PresetMode.HORIZONTAL.value),
                ],
                "rotation_items": [
                    ("不旋转", 0),
                    ("顺时针旋转 90°", 90),
                    ("旋转 180°", 180),
                    ("逆时针旋转 90°", 270),
                ],
            },
            "de": {
                "window_title": "PDF Cut-Stack Broschüre",
                "menu_language": "Sprache",
                "labels": {
                    "input_file": "Eingabedatei",
                    "output_file": "Ausgabedatei",
                    "input_layout": "Layout der Eingabe-PDF",
                    "page_padding": "Seitenrand",
                    "page_rotation": "Drehung der Ausgabeseite",
                    "back_rotate_180": "Rückseite um 180° drehen",
                    "draw_guides": "Schneide-/Falthilfslinien zeichnen",
                    "browse": "Durchsuchen...",
                    "generate": "PDF erzeugen",
                    "unit_mm": " mm",
                },
                "dialogs": {
                    "select_input_pdf": "Eingabe-PDF auswählen",
                    "select_output_pdf": "Ausgabe-PDF auswählen",
                    "pdf_filter": "PDF-Dateien (*.pdf)",
                    "missing_input_title": "Eingabe fehlt",
                    "missing_input_text": "Bitte wählen Sie eine Eingabe-PDF aus.",
                    "missing_output_title": "Ausgabe fehlt",
                    "missing_output_text": "Bitte wählen Sie eine Ausgabe-PDF aus.",
                    "success_title": "Erfolg",
                    "success_text": "PDF erzeugt:<br>{output_pdf}<br><br>{print_tip}",
                    "error_title": "Fehler",
                },
                "logs": {
                    "start": "PDF-Erzeugung gestartet...",
                    "input": "Eingabe: {input_pdf}",
                    "output": "Ausgabe: {output_pdf}",
                    "preset": "Voreinstellung: {preset}",
                    "rotation": "Drehung: {rotation_label}",
                    "order_mode": "Reihenfolge: {order_mode}",
                    "done": "Fertig.",
                    "print_tip": "Druckhinweis:<br>{print_tip}",
                    "error": "Fehler: {error}",
                },
                "tooltips": {
                    "experimental": "Experimentelle Funktion, Änderung wird nicht empfohlen.",
                },
                "print_tips": {
                    "vertical": (
                        "1. Bitte im Duplexmodus mit <b>Wenden an der langen Kante</b> drucken.<br>"
                        "2. Entlang der <b>kürzeren Mittellinie</b> schneiden.<br>"
                        "3. Die obere Hälfte auf die untere Hälfte stapeln.<br>"
                        "4. Falten."
                    ),
                    "horizontal": (
                        "1. Bitte im Duplexmodus mit <b>Wenden an der kurzen Kante</b> drucken.<br>"
                        "2. Entlang der <b>längeren Mittellinie</b> schneiden.<br>"
                        "3. Die obere Hälfte auf die untere Hälfte stapeln.<br>"
                        "4. Falten."
                    ),
                },
                "preset_items": [
                    ("Hochformat-PDF", PresetMode.VERTICAL.value),
                    ("Querformat-PDF", PresetMode.HORIZONTAL.value),
                ],
                "rotation_items": [
                    ("Keine Drehung", 0),
                    ("90° im Uhrzeigersinn", 90),
                    ("180° drehen", 180),
                    ("90° gegen den Uhrzeigersinn", 270),
                ],
            },
        }

    def _lang(self) -> dict[str, Any]:
        return self._texts[self._language]

    def _create_language_menu(self) -> None:
        self.menuLanguage = self.ui.menubar.addMenu("Language")

        self.actionEnglish = QAction("English", self)
        self.actionChinese = QAction("中文", self)
        self.actionGerman = QAction("Deutsch", self)

        self.actionEnglish.triggered.connect(lambda: self.set_language("en"))
        self.actionChinese.triggered.connect(lambda: self.set_language("zh"))
        self.actionGerman.triggered.connect(lambda: self.set_language("de"))

        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionChinese)
        self.menuLanguage.addAction(self.actionGerman)

    def set_language(self, language_code: str) -> None:
        if language_code not in self._texts:
            raise ValueError(f"Unsupported language: {language_code}")
        self._language = language_code
        self._apply_static_texts()
        self._reload_dynamic_texts()
        self._apply_tooltips()

    def _apply_static_texts(self) -> None:
        text = self._lang()
        labels = text["labels"]

        self.setWindowTitle(text["window_title"])
        self.menuLanguage.setTitle(text["menu_language"])

        self.ui.labelInput.setText(labels["input_file"])
        self.ui.buttonBrowseInput.setText(labels["browse"])
        self.ui.labelOutput.setText(labels["output_file"])
        self.ui.buttonBrowseOutput.setText(labels["browse"])
        self.ui.labelPreset.setText(labels["input_layout"])
        self.ui.labelLayout.setText(labels["page_padding"])
        self.ui.labelRotate.setText(labels["page_rotation"])
        self.ui.checkBackRotate180.setText(labels["back_rotate_180"])
        self.ui.checkDrawGuides.setText(labels["draw_guides"])
        self.ui.buttonGenerate.setText(labels["generate"])
        self.ui.spinMargin.setSuffix(labels["unit_mm"])

    def _reload_dynamic_texts(self) -> None:
        current_preset_value = self.ui.comboPreset.currentData()
        current_rotate_value = self.ui.comboRotate.currentData()

        self.ui.comboPreset.clear()
        for label, value in self._lang()["preset_items"]:
            self.ui.comboPreset.addItem(label, value)

        self.ui.comboRotate.clear()
        for label, angle in self._lang()["rotation_items"]:
            self.ui.comboRotate.addItem(label, angle)

        if current_preset_value is not None:
            self._set_combo_by_data(self.ui.comboPreset, current_preset_value)
        if current_rotate_value is not None:
            self._set_combo_by_data(self.ui.comboRotate, current_rotate_value)

    def _init_form(self) -> None:
        self._reload_dynamic_texts()

        self.ui.spinMargin.setDecimals(1)
        self.ui.spinMargin.setRange(0.0, 50.0)
        self.ui.spinMargin.setSingleStep(0.5)
        self.ui.spinMargin.setValue(1.0)

        self.ui.plainTextLog.setReadOnly(True)
        self.ui.checkDrawGuides.setChecked(True)
        self.ui.checkBackRotate180.setChecked(False)

        self._apply_preset_defaults()
        self._apply_tooltips()

    def _connect_signals(self) -> None:
        self.ui.buttonBrowseInput.clicked.connect(self._browse_input)
        self.ui.buttonBrowseOutput.clicked.connect(self._browse_output)
        self.ui.buttonGenerate.clicked.connect(self._generate_pdf)
        self.ui.comboPreset.currentIndexChanged.connect(self._apply_preset_defaults)

    def _apply_tooltips(self) -> None:
        experimental_tip = self._lang()["tooltips"]["experimental"]
        self.ui.comboRotate.setToolTip(experimental_tip)
        self.ui.comboRotate.setStatusTip(experimental_tip)
        self.ui.checkBackRotate180.setToolTip(experimental_tip)
        self.ui.checkBackRotate180.setStatusTip(experimental_tip)

    def _set_combo_by_data(self, combo_box, value: Any) -> None:
        for i in range(combo_box.count()):
            if combo_box.itemData(i) == value:
                combo_box.setCurrentIndex(i)
                return

    def _browse_input(self) -> None:
        dialogs = self._lang()["dialogs"]

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            dialogs["select_input_pdf"],
            "",
            dialogs["pdf_filter"],
        )
        if file_path:
            self.ui.lineEditInput.setText(file_path)

            input_path = Path(file_path)
            default_output = input_path.with_name(f"{input_path.stem}_booklet.pdf")
            self.ui.lineEditOutput.setText(str(default_output))

    def _browse_output(self) -> None:
        dialogs = self._lang()["dialogs"]

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            dialogs["select_output_pdf"],
            "",
            dialogs["pdf_filter"],
        )
        if file_path:
            if not file_path.lower().endswith(".pdf"):
                file_path += ".pdf"
            self.ui.lineEditOutput.setText(file_path)

    def _current_preset(self) -> PresetMode:
        return PresetMode(self.ui.comboPreset.currentData())

    def _set_rotate_value(self, angle: int) -> None:
        self._set_combo_by_data(self.ui.comboRotate, angle)

    def _current_rotation_angle(self) -> int:
        return int(self.ui.comboRotate.currentData())

    def _current_rotation_label(self) -> str:
        return self.ui.comboRotate.currentText()

    def _current_print_tip(self) -> str:
        preset = self._current_preset()
        print_tips = self._lang()["print_tips"]

        if preset == PresetMode.VERTICAL:
            return print_tips["vertical"]
        return print_tips["horizontal"]

    def _apply_preset_defaults(self) -> None:
        preset = self._current_preset()

        self.ui.spinMargin.setValue(1.0)

        if preset == PresetMode.VERTICAL:
            self._set_rotate_value(0)
            self.ui.checkBackRotate180.setChecked(False)

        elif preset == PresetMode.HORIZONTAL:
            self._set_rotate_value(90)
            self.ui.checkBackRotate180.setChecked(False)

    def _log(self, text: str) -> None:
        plain_text = (
            text.replace("<br>", "\n")
            .replace("<b>", "")
            .replace("</b>", "")
        )
        self.ui.plainTextLog.appendPlainText(plain_text)

    def _generate_pdf(self) -> None:
        dialogs = self._lang()["dialogs"]
        logs = self._lang()["logs"]

        input_pdf = self.ui.lineEditInput.text().strip()
        output_pdf = self.ui.lineEditOutput.text().strip()

        if not input_pdf:
            QMessageBox.warning(
                self,
                dialogs["missing_input_title"],
                dialogs["missing_input_text"],
            )
            return

        if not output_pdf:
            QMessageBox.warning(
                self,
                dialogs["missing_output_title"],
                dialogs["missing_output_text"],
            )
            return

        try:
            config = ImpositionConfig.with_preset_defaults(
                input_pdf=input_pdf,
                output_pdf=output_pdf,
                preset=self._current_preset(),
                order_mode=OrderMode.STACK_AFTER_CUT,
                margin_mm=float(self.ui.spinMargin.value()),
                gap_mm=0.0,
                rotate_each=self._current_rotation_angle(),
                back_rotate_180=self.ui.checkBackRotate180.isChecked(),
                draw_guides=self.ui.checkDrawGuides.isChecked(),
            )

            print_tip = self._current_print_tip()

            self._log(logs["start"])
            self._log(logs["input"].format(input_pdf=input_pdf))
            self._log(logs["output"].format(output_pdf=output_pdf))
            self._log(logs["preset"].format(preset=config.preset.value))
            self._log(logs["rotation"].format(rotation_label=self._current_rotation_label()))
            self._log(logs["order_mode"].format(order_mode=config.order_mode.value))

            impose_pdf(config)

            self._log(logs["done"])
            self._log(logs["print_tip"].format(print_tip=print_tip))
            QMessageBox.information(
                self,
                dialogs["success_title"],
                dialogs["success_text"].format(output_pdf=output_pdf, print_tip=print_tip),
            )

        except Exception as exc:
            self._log(logs["error"].format(error=str(exc)))
            QMessageBox.critical(
                self,
                dialogs["error_title"],
                str(exc),
            )


def run() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
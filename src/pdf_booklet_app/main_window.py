# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 681, 511))
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 20, 271, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEditInput = QLineEdit(self.verticalLayoutWidget)
        self.lineEditInput.setObjectName(u"lineEditInput")

        self.verticalLayout.addWidget(self.lineEditInput)

        self.buttonBrowseInput = QPushButton(self.verticalLayoutWidget)
        self.buttonBrowseInput.setObjectName(u"buttonBrowseInput")

        self.verticalLayout.addWidget(self.buttonBrowseInput)

        self.lineEditOutput = QLineEdit(self.verticalLayoutWidget)
        self.lineEditOutput.setObjectName(u"lineEditOutput")

        self.verticalLayout.addWidget(self.lineEditOutput)

        self.buttonBrowseOutput = QPushButton(self.verticalLayoutWidget)
        self.buttonBrowseOutput.setObjectName(u"buttonBrowseOutput")

        self.verticalLayout.addWidget(self.buttonBrowseOutput)

        self.comboPreset = QComboBox(self.verticalLayoutWidget)
        self.comboPreset.setObjectName(u"comboPreset")

        self.verticalLayout.addWidget(self.comboPreset)

        self.comboOrderMode = QComboBox(self.verticalLayoutWidget)
        self.comboOrderMode.setObjectName(u"comboOrderMode")

        self.verticalLayout.addWidget(self.comboOrderMode)

        self.spinMargin = QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinMargin.setObjectName(u"spinMargin")

        self.verticalLayout.addWidget(self.spinMargin)

        self.comboRotate = QComboBox(self.verticalLayoutWidget)
        self.comboRotate.setObjectName(u"comboRotate")

        self.verticalLayout.addWidget(self.comboRotate)

        self.checkBackRotate180 = QCheckBox(self.verticalLayoutWidget)
        self.checkBackRotate180.setObjectName(u"checkBackRotate180")

        self.verticalLayout.addWidget(self.checkBackRotate180)

        self.checkDrawGuides = QCheckBox(self.verticalLayoutWidget)
        self.checkDrawGuides.setObjectName(u"checkDrawGuides")

        self.verticalLayout.addWidget(self.checkDrawGuides)

        self.buttonGenerate = QPushButton(self.verticalLayoutWidget)
        self.buttonGenerate.setObjectName(u"buttonGenerate")

        self.verticalLayout.addWidget(self.buttonGenerate)

        self.plainTextLog = QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextLog.setObjectName(u"plainTextLog")

        self.verticalLayout.addWidget(self.plainTextLog)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonBrowseInput.setText(QCoreApplication.translate("MainWindow", u"input", None))
        self.buttonBrowseOutput.setText(QCoreApplication.translate("MainWindow", u"output", None))
        self.checkBackRotate180.setText(QCoreApplication.translate("MainWindow", u"back rotate 180", None))
        self.checkDrawGuides.setText(QCoreApplication.translate("MainWindow", u"draw guides", None))
        self.buttonGenerate.setText(QCoreApplication.translate("MainWindow", u"generate", None))
    # retranslateUi


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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(742, 531)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 10, 721, 461))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QWidget(self.horizontalLayoutWidget_3)
        self.leftPanel.setObjectName(u"leftPanel")
        self.verticalLayoutWidget = QWidget(self.leftPanel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 361, 378))
        self.verticalLayoutLeft = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutLeft.setObjectName(u"verticalLayoutLeft")
        self.verticalLayoutLeft.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelInput = QLabel(self.verticalLayoutWidget)
        self.labelInput.setObjectName(u"labelInput")

        self.horizontalLayout.addWidget(self.labelInput)

        self.lineEditInput = QLineEdit(self.verticalLayoutWidget)
        self.lineEditInput.setObjectName(u"lineEditInput")

        self.horizontalLayout.addWidget(self.lineEditInput)

        self.buttonBrowseInput = QPushButton(self.verticalLayoutWidget)
        self.buttonBrowseInput.setObjectName(u"buttonBrowseInput")

        self.horizontalLayout.addWidget(self.buttonBrowseInput)


        self.verticalLayoutLeft.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelOutput = QLabel(self.verticalLayoutWidget)
        self.labelOutput.setObjectName(u"labelOutput")

        self.horizontalLayout_2.addWidget(self.labelOutput)

        self.lineEditOutput = QLineEdit(self.verticalLayoutWidget)
        self.lineEditOutput.setObjectName(u"lineEditOutput")

        self.horizontalLayout_2.addWidget(self.lineEditOutput)

        self.buttonBrowseOutput = QPushButton(self.verticalLayoutWidget)
        self.buttonBrowseOutput.setObjectName(u"buttonBrowseOutput")

        self.horizontalLayout_2.addWidget(self.buttonBrowseOutput)


        self.verticalLayoutLeft.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelPreset = QLabel(self.verticalLayoutWidget)
        self.labelPreset.setObjectName(u"labelPreset")

        self.horizontalLayout_5.addWidget(self.labelPreset)

        self.comboPreset = QComboBox(self.verticalLayoutWidget)
        self.comboPreset.setObjectName(u"comboPreset")

        self.horizontalLayout_5.addWidget(self.comboPreset)


        self.verticalLayoutLeft.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelLayout = QLabel(self.verticalLayoutWidget)
        self.labelLayout.setObjectName(u"labelLayout")

        self.horizontalLayout_4.addWidget(self.labelLayout)

        self.spinMargin = QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinMargin.setObjectName(u"spinMargin")
        self.spinMargin.setDecimals(1)
        self.spinMargin.setMaximum(50.000000000000000)
        self.spinMargin.setSingleStep(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.spinMargin)


        self.verticalLayoutLeft.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelRotate = QLabel(self.verticalLayoutWidget)
        self.labelRotate.setObjectName(u"labelRotate")

        self.horizontalLayout_6.addWidget(self.labelRotate)

        self.comboRotate = QComboBox(self.verticalLayoutWidget)
        self.comboRotate.setObjectName(u"comboRotate")

        self.horizontalLayout_6.addWidget(self.comboRotate)


        self.verticalLayoutLeft.addLayout(self.horizontalLayout_6)

        self.checkBackRotate180 = QCheckBox(self.verticalLayoutWidget)
        self.checkBackRotate180.setObjectName(u"checkBackRotate180")

        self.verticalLayoutLeft.addWidget(self.checkBackRotate180)

        self.checkDrawGuides = QCheckBox(self.verticalLayoutWidget)
        self.checkDrawGuides.setObjectName(u"checkDrawGuides")

        self.verticalLayoutLeft.addWidget(self.checkDrawGuides)

        self.buttonGenerate = QPushButton(self.verticalLayoutWidget)
        self.buttonGenerate.setObjectName(u"buttonGenerate")

        self.verticalLayoutLeft.addWidget(self.buttonGenerate)


        self.horizontalLayout_3.addWidget(self.leftPanel)

        self.plainTextLog = QPlainTextEdit(self.horizontalLayoutWidget_3)
        self.plainTextLog.setObjectName(u"plainTextLog")
        self.plainTextLog.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.plainTextLog)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 742, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelInput.setText(QCoreApplication.translate("MainWindow", u"Input File", None))
        self.buttonBrowseInput.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.labelOutput.setText(QCoreApplication.translate("MainWindow", u"Output File", None))
        self.buttonBrowseOutput.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.labelPreset.setText(QCoreApplication.translate("MainWindow", u"Input PDF Layout", None))
        self.labelLayout.setText(QCoreApplication.translate("MainWindow", u"Page Padding", None))
        self.labelRotate.setText(QCoreApplication.translate("MainWindow", u"Output Page Rotation", None))
        self.checkBackRotate180.setText(QCoreApplication.translate("MainWindow", u"Rotate back side by 180\u00b0", None))
        self.checkDrawGuides.setText(QCoreApplication.translate("MainWindow", u"Draw cut/fold guides", None))
        self.buttonGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi


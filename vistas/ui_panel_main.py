# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_panel_main(object):
    def setupUi(self, panel_main):
        if not panel_main.objectName():
            panel_main.setObjectName(u"panel_main")
        panel_main.resize(520, 507)
        panel_main.setMinimumSize(QSize(520, 507))
        panel_main.setMaximumSize(QSize(520, 507))
        panel_main.setStyleSheet(u"QWidget {\n"
"    background-color: #303030; \n"
"    color: #e0e0e0; \n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2196f3;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"    border-radius: 4px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1976d2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1565c0;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #e0e0e0;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"#relojLbl {\n"
"    font-size: 48px;\n"
"    font-weight: bold;\n"
"    color: #bb86fc; \n"
"}\n"
"\n"
"\n"
"#IblMensaje_2 {\n"
"    font-size: 16px;\n"
"    color: #cf6679; \n"
"}\n"
"\n"
"\n"
"#panel_main {\n"
"    background-color: #1e1e1e; \n"
"    border-radius: 8px;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"#panel_central {\n"
"    background-color: #272727; \n"
"    border-radius: 4px;\n"
"    padding: 10px;\n"
"}")
        self.widget_2 = QWidget(panel_main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 521, 511))
        self.chck12H = QCheckBox(self.widget_2)
        self.chck12H.setObjectName(u"chck12H")
        self.chck12H.setGeometry(QRect(200, 30, 144, 23))
        font = QFont()
        font.setBold(True)
        self.chck12H.setFont(font)
        self.relojLbl = QLabel(self.widget_2)
        self.relojLbl.setObjectName(u"relojLbl")
        self.relojLbl.setGeometry(QRect(90, 70, 333, 82))
        self.relojLbl.setFont(font)
        self.relojLbl.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.relojLbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnActivar = QPushButton(self.widget_2)
        self.btnActivar.setObjectName(u"btnActivar")
        self.btnActivar.setGeometry(QRect(190, 160, 144, 41))
        self.btnActivar.setFont(font)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(20, 240, 481, 241))
        self.lblAlarma = QLabel(self.widget_3)
        self.lblAlarma.setObjectName(u"lblAlarma")
        self.lblAlarma.setGeometry(QRect(190, 10, 121, 51))
        self.lblAlarma.setFont(font)
        self.gridLayoutWidget = QWidget(self.widget_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 60, 441, 151))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblMensaje = QLabel(self.gridLayoutWidget)
        self.lblMensaje.setObjectName(u"lblMensaje")
        self.lblMensaje.setStyleSheet(u"QLabel {\n"
"    color: #e0e0e0;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")

        self.gridLayout_2.addWidget(self.lblMensaje, 0, 0, 1, 1)


        self.retranslateUi(panel_main)

        QMetaObject.connectSlotsByName(panel_main)
    # setupUi

    def retranslateUi(self, panel_main):
        panel_main.setWindowTitle(QCoreApplication.translate("panel_main", u"Reloj", None))
        self.chck12H.setText(QCoreApplication.translate("panel_main", u"Formato 12h", None))
        self.relojLbl.setText(QCoreApplication.translate("panel_main", u"00:00:00 AM", None))
        self.btnActivar.setText(QCoreApplication.translate("panel_main", u"Editar Alarma", None))
        self.lblAlarma.setText(QCoreApplication.translate("panel_main", u"Alarmas:", None))
        self.lblMensaje.setText("")
    # retranslateUi


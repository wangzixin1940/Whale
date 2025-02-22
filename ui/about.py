# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'about.ui'
#
# Created by: Qt User Interface Compiler version 6.8.0
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QLabel)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Help | QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(150, 30, 191, 41))
        font = QFont()
        font.setFamilies([u"Fira Code"])
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.versionNumber = QLabel(Dialog)
        self.versionNumber.setObjectName(u"versionNumber")
        self.versionNumber.setGeometry(QRect(150, 80, 101, 16))
        font1 = QFont()
        font1.setFamilies([u"Fira Code"])
        font1.setPointSize(10)
        self.versionNumber.setFont(font1)
        self.licenseTypeDisplay = QLabel(Dialog)
        self.licenseTypeDisplay.setObjectName(u"licenseTypeDisplay")
        self.licenseTypeDisplay.setGeometry(QRect(10, 130, 241, 16))
        self.copyrightOwnerDisplay = QLabel(Dialog)
        self.copyrightOwnerDisplay.setObjectName(u"copyrightOwnerDisplay")
        self.copyrightOwnerDisplay.setGeometry(QRect(10, 160, 231, 16))
        self.logoDisplay = QLabel(Dialog)
        self.logoDisplay.setObjectName(u"logoDisplay")
        self.logoDisplay.setGeometry(QRect(20, 20, 111, 101))
        self.logoDisplay.setPixmap(QPixmap(u"./ui/logo.png").scaled(90, 90, Qt.AspectRatioMode.KeepAspectRatio))
        self.logoDisplay.setScaledContents(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Whale", None))
        self.versionNumber.setText(QCoreApplication.translate("Dialog", u"0.1-SNAPSHOT", None))
        self.licenseTypeDisplay.setText(QCoreApplication.translate("Dialog", u"This program licensed under "
                                                                             u"MIT License.", None))
        self.copyrightOwnerDisplay.setText(QCoreApplication.translate("Dialog", u"(C) 2025 Zixin Wang", None))
        self.logoDisplay.setText("")
    # retranslateUi

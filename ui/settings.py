# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'settings.ui'
#
# Created by: Qt User Interface Compiler version 6.8.0
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtWidgets import (QCheckBox, QComboBox,
                               QDialogButtonBox, QFontComboBox, QGroupBox,
                               QLabel, QLineEdit, QPushButton, QSpinBox, QTabWidget, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(488, 287)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 240, 471, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 481, 241))
        self.generalSettings = QWidget()
        self.generalSettings.setObjectName(u"generalSettings")
        self.languageChooseLabel = QLabel(self.generalSettings)
        self.languageChooseLabel.setObjectName(u"languageChooseLabel")
        self.languageChooseLabel.setGeometry(QRect(10, 10, 101, 21))
        self.languageChoose = QComboBox(self.generalSettings)
        self.languageChoose.addItem("")
        self.languageChoose.addItem("")
        self.languageChoose.setObjectName(u"languageChoose")
        self.languageChoose.setGeometry(QRect(110, 10, 351, 22))
        self.autoLineWrappingSetting = QCheckBox(self.generalSettings)
        self.autoLineWrappingSetting.setObjectName(u"autoLineWrappingSetting")
        self.autoLineWrappingSetting.setGeometry(QRect(10, 40, 451, 19))
        self.pageSetupButton = QPushButton(self.generalSettings)
        self.pageSetupButton.setObjectName(u"pageSetupButton")
        self.pageSetupButton.setGeometry(QRect(10, 70, 451, 23))
        self.encodingChooseLabel = QLabel(self.generalSettings)
        self.encodingChooseLabel.setObjectName(u"encodingChooseLabel")
        self.encodingChooseLabel.setGeometry(QRect(10, 110, 121, 16))
        self.encodingChoose = QComboBox(self.generalSettings)
        self.encodingChoose.addItem("")
        self.encodingChoose.addItem("")
        self.encodingChoose.addItem("")
        self.encodingChoose.setObjectName(u"encodingChoose")
        self.encodingChoose.setGeometry(QRect(140, 110, 321, 22))
        self.tabWidget.addTab(self.generalSettings, "")
        self.editorSettings = QWidget()
        self.editorSettings.setObjectName(u"editorSettings")
        self.fontSettingLabel = QLabel(self.editorSettings)
        self.fontSettingLabel.setObjectName(u"fontSettingLabel")
        self.fontSettingLabel.setGeometry(QRect(10, 10, 71, 16))
        self.fontSetting = QFontComboBox(self.editorSettings)
        self.fontSetting.setObjectName(u"fontSetting")
        self.fontSetting.setGeometry(QRect(80, 10, 291, 22))
        self.fontSizeSetting = QSpinBox(self.editorSettings)
        self.fontSizeSetting.setObjectName(u"fontSizeSetting")
        self.fontSizeSetting.setGeometry(QRect(381, 10, 81, 22))
        self.fontPreview = QLineEdit(self.editorSettings)
        self.fontPreview.setObjectName(u"fontPreview")
        self.fontPreview.setGeometry(QRect(10, 40, 451, 31))
        self.timestampSettings = QGroupBox(self.editorSettings)
        self.timestampSettings.setObjectName(u"timestampSettings")
        self.timestampSettings.setGeometry(QRect(10, 80, 461, 121))
        self.timestampPresetsChoose = QComboBox(self.timestampSettings)
        self.timestampPresetsChoose.addItem("")
        self.timestampPresetsChoose.addItem("")
        self.timestampPresetsChoose.addItem("")
        self.timestampPresetsChoose.addItem("")
        self.timestampPresetsChoose.addItem("")
        self.timestampPresetsChoose.setObjectName(u"timestampPresetsChoose")
        self.timestampPresetsChoose.setGeometry(QRect(10, 41, 441, 31))
        self.customTimestampSet = QLineEdit(self.timestampSettings)
        self.customTimestampSet.setObjectName(u"customTimestampSet")
        self.customTimestampSet.setEnabled(False)
        self.customTimestampSet.setGeometry(QRect(10, 79, 441, 31))
        self.tabWidget.addTab(self.editorSettings, "")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.languageChooseLabel.setText(QCoreApplication.translate("Dialog", u"Language Profile:", None))
        self.languageChoose.setItemText(0, QCoreApplication.translate("Dialog", u"English (US)", None))
        self.languageChoose.setItemText(1, QCoreApplication.translate("Dialog", u"Simp. Chinese (China Mainland)",
                                                                      None))

        self.autoLineWrappingSetting.setText(QCoreApplication.translate("Dialog", u"Automatic line wrapping", None))
        self.pageSetupButton.setText(QCoreApplication.translate("Dialog", u"Page Setup", None))
        self.encodingChooseLabel.setText(QCoreApplication.translate("Dialog", u"Default File Encoding:", None))
        self.encodingChoose.setItemText(0, QCoreApplication.translate("Dialog", u"UTF-8", None))
        self.encodingChoose.setItemText(1, QCoreApplication.translate("Dialog", u"GBK", None))
        self.encodingChoose.setItemText(2, QCoreApplication.translate("Dialog", u"ANSI", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalSettings), QCoreApplication.translate("Dialog",
                                                                                                           u"General",
                                                                                                           None))
        self.fontSettingLabel.setText(QCoreApplication.translate("Dialog", u"Editor Font:", None))
        self.fontPreview.setText(QCoreApplication.translate("Dialog", u"Type here to preview your settings...", None))
        self.timestampSettings.setTitle(QCoreApplication.translate("Dialog", u"Timestamp Settings", None))
        self.timestampPresetsChoose.setItemText(0, QCoreApplication.translate("Dialog",
                                                                              u"Western Countries (MM-DD-YY hh:mm:ss, "
                                                                              u"example: 02-16-25 13:06:35)", None))
        self.timestampPresetsChoose.setItemText(1, QCoreApplication.translate("Dialog",
                                                                              u"UK Style (DD-MM-YY hh:mm:ss, "
                                                                              u"example: 16-02-15 13:06:35)", None))
        self.timestampPresetsChoose.setItemText(2, QCoreApplication.translate("Dialog",
                                                                              u"China Mainland Style "
                                                                              u"(YYYY-MM-DD hh:mm:ss, "
                                                                              u"example: 2025-02-16 13:06:35)", None))
        self.timestampPresetsChoose.setItemText(3, QCoreApplication.translate("Dialog",
                                                                              u"ISO-8601 (YYYY-MM-DDThh:mm:ss, "
                                                                              u"example: 2025-02-16T13:06:35)", None))
        self.timestampPresetsChoose.setItemText(4, QCoreApplication.translate("Dialog", u"No Presets", None))

# if QT_CONFIG(tooltip)
        self.timestampPresetsChoose.setToolTip(QCoreApplication.translate("Dialog", u"Presets", None))
# endif // QT_CONFIG(tooltip)
        self.customTimestampSet.setText(QCoreApplication.translate("Dialog", u"MM-DD-YY hh:mm:ss", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editorSettings), QCoreApplication.translate("Dialog",
                                                                                                          u"Editor",
                                                                                                          None))
    # retranslateUi

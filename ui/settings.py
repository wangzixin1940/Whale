# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'settings.ui'
#
# Created by: Qt User Interface Compiler version 6.8.2
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
        self.settingsTabs = QTabWidget(Dialog)
        self.settingsTabs.setObjectName(u"settingsTabs")
        self.settingsTabs.setGeometry(QRect(0, 0, 481, 241))
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
        self.encodingChoose.setObjectName(u"encodingChoose")
        self.encodingChoose.setGeometry(QRect(140, 110, 321, 22))
        self.settingsTabs.addTab(self.generalSettings, "")
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
        self.settingsTabs.addTab(self.editorSettings, "")
        self.appearanceSettings = QWidget()
        self.appearanceSettings.setObjectName(u"appearanceSettings")
        self.themeChooseLabel = QLabel(self.appearanceSettings)
        self.themeChooseLabel.setObjectName(u"themeChooseLabel")
        self.themeChooseLabel.setGeometry(QRect(10, 10, 54, 16))
        self.themeChooseLabel.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)
        self.themeChooseCombo = QComboBox(self.appearanceSettings)
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.addItem("")
        self.themeChooseCombo.setObjectName(u"themeChooseCombo")
        self.themeChooseCombo.setGeometry(QRect(70, 10, 371, 22))
        self.settingsTabs.addTab(self.appearanceSettings, "")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.settingsTabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.languageChooseLabel.setText(QCoreApplication.translate("Dialog", u"Language Profile:", None))
        self.languageChoose.setItemText(0, QCoreApplication.translate("Dialog", u"English (US)", None))
        self.languageChoose.setItemText(1, QCoreApplication.translate("Dialog",
                                                                      u"\u7b80\u4f53\u4e2d\u6587 ("
                                                                      u"\u4e2d\u56fd\u5927\u9646)",
                                                                      None))

        self.autoLineWrappingSetting.setText(QCoreApplication.translate("Dialog", u"Automatic line wrapping", None))
        self.pageSetupButton.setText(QCoreApplication.translate("Dialog", u"Page Setup", None))
        self.encodingChooseLabel.setText(QCoreApplication.translate("Dialog", u"Default File Encoding:", None))
        self.encodingChoose.setItemText(0, QCoreApplication.translate("Dialog", u"UTF-8", None))
        self.encodingChoose.setItemText(1, QCoreApplication.translate("Dialog", u"GBK", None))

        self.settingsTabs.setTabText(self.settingsTabs.indexOf(self.generalSettings),
                                     QCoreApplication.translate("Dialog", u"General", None))
        self.fontSettingLabel.setText(QCoreApplication.translate("Dialog", u"Editor Font:", None))
        self.fontPreview.setText(QCoreApplication.translate("Dialog", u"Type here to preview your settings...", None))
        self.timestampSettings.setTitle(QCoreApplication.translate("Dialog", u"Timestamp Settings", None))
        self.timestampPresetsChoose.setItemText(0, QCoreApplication.translate("Dialog",
                                                                              u"Western Countries (MM-DD-YY hh:mm:ss, "
                                                                              u"example: 02-16-25 13:06:35)",
                                                                              None))
        self.timestampPresetsChoose.setItemText(1, QCoreApplication.translate("Dialog",
                                                                              u"UK Style (DD-MM-YY hh:mm:ss, example: "
                                                                              u"16-02-15 13:06:35)",
                                                                              None))
        self.timestampPresetsChoose.setItemText(2, QCoreApplication.translate("Dialog",
                                                                              u"China Mainland Style (YYYY-MM-DD "
                                                                              u"hh:mm:ss, example: 2025-02-16 "
                                                                              u"13:06:35)",
                                                                              None))
        self.timestampPresetsChoose.setItemText(3, QCoreApplication.translate("Dialog",
                                                                              u"ISO-8601 (YYYY-MM-DDThh:mm:ss, "
                                                                              u"example: 2025-02-16T13:06:35)",
                                                                              None))
        self.timestampPresetsChoose.setItemText(4, QCoreApplication.translate("Dialog", u"No Presets", None))

        # if QT_CONFIG(tooltip)
        self.timestampPresetsChoose.setToolTip(QCoreApplication.translate("Dialog", u"Presets", None))
        # endif // QT_CONFIG(tooltip)
        self.customTimestampSet.setText(QCoreApplication.translate("Dialog", u"MM-DD-YY hh:mm:ss", None))
        self.settingsTabs.setTabText(self.settingsTabs.indexOf(self.editorSettings),
                                     QCoreApplication.translate("Dialog", u"Editor", None))
        self.themeChooseLabel.setText(QCoreApplication.translate("Dialog", u"Theme", None))
        self.themeChooseCombo.setItemText(0, QCoreApplication.translate("Dialog", u"Dark Amber", None))
        self.themeChooseCombo.setItemText(1, QCoreApplication.translate("Dialog", u"Dark Blue", None))
        self.themeChooseCombo.setItemText(2, QCoreApplication.translate("Dialog", u"Dark Cyan", None))
        self.themeChooseCombo.setItemText(3, QCoreApplication.translate("Dialog", u"Dark Lightgreen", None))
        self.themeChooseCombo.setItemText(4, QCoreApplication.translate("Dialog", u"Dark Medical", None))
        self.themeChooseCombo.setItemText(5, QCoreApplication.translate("Dialog", u"Dark Pink", None))
        self.themeChooseCombo.setItemText(6, QCoreApplication.translate("Dialog", u"Dark Purple", None))
        self.themeChooseCombo.setItemText(7, QCoreApplication.translate("Dialog", u"Dark Red", None))
        self.themeChooseCombo.setItemText(8, QCoreApplication.translate("Dialog", u"Dark Teal", None))
        self.themeChooseCombo.setItemText(9, QCoreApplication.translate("Dialog", u"Dark Yellow", None))
        self.themeChooseCombo.setItemText(10, QCoreApplication.translate("Dialog", u"Light Amber", None))
        self.themeChooseCombo.setItemText(11, QCoreApplication.translate("Dialog", u"Light Blue", None))
        self.themeChooseCombo.setItemText(12, QCoreApplication.translate("Dialog", u"Light Blue 500", None))
        self.themeChooseCombo.setItemText(13, QCoreApplication.translate("Dialog", u"Light Cyan", None))
        self.themeChooseCombo.setItemText(14, QCoreApplication.translate("Dialog", u"Light Cyan 500", None))
        self.themeChooseCombo.setItemText(15, QCoreApplication.translate("Dialog", u"Light Lightgreen", None))
        self.themeChooseCombo.setItemText(16, QCoreApplication.translate("Dialog", u"Light Lightgreen 500", None))
        self.themeChooseCombo.setItemText(17, QCoreApplication.translate("Dialog", u"Light orange", None))
        self.themeChooseCombo.setItemText(18, QCoreApplication.translate("Dialog", u"Light Pink", None))
        self.themeChooseCombo.setItemText(19, QCoreApplication.translate("Dialog", u"Light Pink 500", None))
        self.themeChooseCombo.setItemText(20, QCoreApplication.translate("Dialog", u"Light Purple", None))
        self.themeChooseCombo.setItemText(21, QCoreApplication.translate("Dialog", u"Light Purple 500", None))
        self.themeChooseCombo.setItemText(22, QCoreApplication.translate("Dialog", u"Light Red", None))
        self.themeChooseCombo.setItemText(23, QCoreApplication.translate("Dialog", u"Light Red 500", None))
        self.themeChooseCombo.setItemText(24, QCoreApplication.translate("Dialog", u"Light Teal", None))
        self.themeChooseCombo.setItemText(25, QCoreApplication.translate("Dialog", u"Light Teal 500", None))
        self.themeChooseCombo.setItemText(26, QCoreApplication.translate("Dialog", u"Light Yellow", None))

        self.settingsTabs.setTabText(self.settingsTabs.indexOf(self.appearanceSettings),
                                     QCoreApplication.translate("Dialog", u"Appearance", None))
    # retranslateUi

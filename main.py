from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTranslator
from PySide6.QtPrintSupport import QPrintDialog, QPrinter, QPageSetupDialog
import qt_material as FormStyle
from ui.form import Ui_MainWindow
from ui.settings import Ui_Dialog as Ui_SettingsDialog
from ui.about import Ui_Dialog as Ui_AboutDialog
import logging
import os
import platform
import traceback
import yaml

language = {
    "en-us": "English (US)",
    "zh-cn": "简体中文 (中国大陆)",
}

encodings = {
    "utf-8": "UTF-8",
    "gbk": "GBK",
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(filename)s:%(funcName)s:%(lineno)d:%(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)
logger = logging.getLogger("MainWindow")

try:
    with open("settings.yaml", "r", encoding="utf-8") as file:
        settings = yaml.safe_load(file)
except FileNotFoundError:
    logger.critical("settings.yaml not found! The program cannot continue to run!")
    logger.critical("Full traceback:\n" + traceback.format_exc())
    exit(1)
except yaml.YAMLError:
    logger.critical("settings.yaml is not a valid YAML file! The program cannot continue to run!")
    logger.critical("Full traceback:\n" + traceback.format_exc())
    exit(1)

# Read settings from settings.yaml

if settings["appearance"]["theme"] not in FormStyle.list_themes():
    logger.warning("An invalid style was detected.")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connect actions to the functions
        self.actionPreference_Settings.triggered.connect(self.settingsWindow)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionNew.triggered.connect(self.newFile)
        self.actionDiscard_Close.triggered.connect(self.discard)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveAsFile)
        self.actionPage_Settings.triggered.connect(self.pageSetup)
        self.actionPrint.triggered.connect(self.printFile)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.aboutWindow)
        self.actionView_README.triggered.connect(lambda: os.startfile("README.MD"))
        self.actionOpen_with.triggered.connect(self.openWith)
        self.actionOpen_in_System_File_Explorer.triggered.connect(self.openInFileExplorer)
        # Connect slots to the functions
        self.textEdit.textChanged.connect(self.textChanged)
        # Define variables
        self.opened = False
        self.changed = False
        self.Printer = QPrinter()
        self.filePath = ""

    def settingsWindow(self):
        logger.info("Settings window called.")
        self.settingsDialog = SettingsDialog()
        logger.info("Settings window opened.")
        self.settingsDialog.show()

    def aboutWindow(self):
        logger.info("About window called.")
        self.aboutDialog = AboutDialog()
        self.aboutDialog.buttonBox.helpRequested.connect(lambda: os.startfile("README.MD"))
        logger.info("About window opened.")
        self.aboutDialog.show()

    def openFile(self):
        logger.info("openFile function called.")
        self.filePath = QFileDialog.getOpenFileName(self, "Open a file", "", "All files(*.*)")[0]
        if self.filePath == "": return
        if os.path.getsize(self.filePath) >= 1 * 1024 * 1024:  # 1 MiB
            if not QMessageBox.question(
                    self, "Warning",
                    "This file looks very large and doesn't seem to be a plain text file. "
                    "Do you still want to open it?") == QMessageBox.StandardButton.Yes:
                return
        if self.opened and self.changed:
            response = QMessageBox.question(self, "Warning", "A file has already been opened and changed. "
                                                             "If you continue to open this file, "
                                                             "the changes you made will disappear. "
                                                             "Do you still want to open it?")
            if response == QMessageBox.StandardButton.No:
                return
        self.opened = True
        self.changed = False
        with open(self.filePath, "r", encoding="utf-8") as file:
            self.text = file.read()
            self.textEdit.setText(self.text)
            self.setWindowTitle("Whale - " + os.path.split(self.filePath)[-1])

    def newFile(self):
        logger.info("newFile function called.")
        if self.opened and self.changed:
            response = QMessageBox.question(self, "Warning", "A file has already been opened and changed. "
                                                             "If you continue to create a new file, "
                                                             "the changes you made will disappear. "
                                                             "Do you still want to continue?")
            if response == QMessageBox.StandardButton.No:
                return
        self.opened = True
        self.changed = False
        self.setWindowTitle("Whale - New File")

    def textChanged(self):
        logger.info("Text changed.")
        self.opened = True
        self.changed = True

    def discard(self):
        logger.info("Discard function called.")
        if not (QMessageBox.question(self, "Warning", "This document is about to be closed. "
                                                      "Once closed, the changes you have made will be discarded. "
                                                      "Do you still want to continue?")
                == QMessageBox.StandardButton.Yes):
            return
        self.filePath = ""
        self.opened = False
        self.changed = False
        self.textEdit.setText("")
        self.setWindowTitle("Whale - New File")

    def saveFile(self):
        logger.info("saveFile function called.")
        if self.filePath == "":
            self.saveAsFile()
            return
        with open(self.filePath, "w", encoding="utf-8") as file:
            file.write(self.textEdit.toPlainText())
            self.statusbar.showMessage("Saved.", 5000)

    def saveAsFile(self):
        logger.info("saveAsFile function called.")
        if self.filePath != "":
            self.filePath = QFileDialog.getSaveFileName(self, "Save file", "", "All files(*.*)")[0]
            with open(self.filePath, "w", encoding="utf-8") as file:
                file.write(self.textEdit.toPlainText())
                self.statusbar.showMessage("Saved.", 5000)
        else:
            self.filePath = QFileDialog.getSaveFileName(self, "Save file", "", "All files(*.*)")[0]
            if self.filePath == "": return
            with open(self.filePath, "w", encoding="utf-8") as file:
                file.write(self.textEdit.toPlainText())
                self.statusbar.showMessage("Saved.", 5000)
            self.setWindowTitle("Whale - " + os.path.split(self.filePath)[-1])

    def pageSetup(self):
        logger.info("pageSetup function called.")
        self.pageSettingsDialog = QPageSetupDialog(self.Printer, self)
        self.pageSettingsDialog.exec()

    def printFile(self):
        logger.info("Print function called.")
        self.printDialog = QPrintDialog(self.Printer, self)
        if self.printDialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            self.textEdit.print_(self.Printer)

    def openInFileExplorer(self):
        logger.info("openInFileExplorer function called.")
        if platform.system() == "Windows":
            os.system(f'explorer /select \"{self.filePath.replace("/", "\\")}\"')
            logger.info(f"Ran command \"explorer /select \"{self.filePath}\"\"")
        elif platform.system() == "Darwin":
            os.system(f'open -R \"{self.filePath}\"')
            logger.info(f"Ran command \"open -R \"{self.filePath}\"\"")
        elif platform.system() == "Linux":
            os.system(f'xdg-open \"{self.filePath}\"')
            logger.info(f"Ran command \"xdg-open \"{self.filePath}\"\"")
        else:
            logger.warning("Could not find system's file explorer.")
            QMessageBox.warning(self, "Warning", f"Could not find system's file explorer.\nThe file path is"
                                                 f"\n{self.filePath}")

    def openWith(self):
        program = QInputDialog.getText(self, "Open with",
                                       "Enter the path of the program you want to open with.")[0]
        os.system(f'{program} "{self.filePath}"')


class SettingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./ui/favicon.ico"))
        self.setFixedSize(self.size())
        # Connect buttons to the functions
        self.buttonBox.accepted.connect(self.saveSettings)
        self.rejected.connect(self.reject)
        self.pageSetupButton.clicked.connect(MainWindow.pageSetup)
        # Connect events to the functions
        self.timestampPresetsChoose.currentIndexChanged.connect(self.timestampPresetChanged)

    def saveSettings(self):
        logger.info("saveSettings function called.")
        global settings
        currentLanguage = ""
        currentEncoding = ""
        for i in list(language.values()):
            if language[i] == self.languageChoose.currentText():
                currentLanguage = i
        for j in list(encodings.values()):
            if encodings[j] == self.encodingChoose.currentText():
                currentEncoding = j
        settings = {
            "region": {
                "language": currentLanguage,
                "encoding": currentEncoding,
                "timestamp": self.customTimestampSet.currentText(),
            },
            "editor": {
                "autoLineWrapping": self.autoLineWrappingSetting.isChecked(),
            },
            "appearance": {
                "theme": self.themeChooseCombo.currentText().replace(" ", "_").lower(),
                "font": self.fontSetting.currentText(),
                "fontSize": int(self.fontSizeSetting.currentText()),
            },
        }
        return self.accept

    def timestampPresetChanged(self):
        logger.info("timestampPresetChanged function called.")
        if self.timestampPresetsChoose.currentIndex() == 4:
            self.customTimestampSet.setEnabled(True)
        else:
            self.customTimestampSet.setEnabled(False)
        match self.customTimestampSet.currentIndex():
            case 0:
                timestampFormat = "MM/DD/YY hh:mm:ss"
                self.customTimestampSet.setText(timestampFormat)
                self.customTimestampSet.setEnabled(False)
            case 1:
                timestampFormat = "DD/MM/YY hh:mm:ss"
                self.customTimestampSet.setText(timestampFormat)
                self.customTimestampSet.setEnabled(False)
            case 2:
                timestampFormat = "YYYY-MM-DD hh:mm:ss"
                self.customTimestampSet.setText(timestampFormat)
                self.customTimestampSet.setEnabled(False)
            case 3:
                timestampFormat = "YYYY-MM-DDThh:mm:ss"
                self.customTimestampSet.setText(timestampFormat)
                self.customTimestampSet.setEnabled(False)
            case 4:
                self.customTimestampSet.setEnabled(True)


class AboutDialog(QtWidgets.QDialog, Ui_AboutDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./ui/favicon.ico"))
        self.setFixedSize(self.size())


def entryPoint(*args):
    app = QApplication.instance()
    if app == None:
        app = QApplication(*args)
    translator = QTranslator()
    if translator.load(settings["region"]["language"], "./ui/i18n"):
        app.installTranslator(translator)
    window = MainWindow()
    window.setWindowIcon(QIcon("./ui/favicon.ico"))
    window.setWindowTitle("Whale - New File")
    FormStyle.apply_stylesheet(app, settings["appearance"]["theme"])
    logger.info("Application started.")
    window.show()
    exitCode = app.exec()
    logger.info(f"Application closed with exit code {exitCode}.")
    exit(exitCode)


if __name__ == "__main__":
    entryPoint()

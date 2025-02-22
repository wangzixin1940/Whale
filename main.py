from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTranslator
from PySide6.QtPrintSupport import QPrintDialog, QPrinter, QPageSetupDialog
import qt_material as FormStyle
from ui.form import Ui_MainWindow
from ui.settings import Ui_Dialog as Ui_SettingsDialog
from ui.about import Ui_Dialog as Ui_AboutDialog
import configparser
import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(filename)s:%(funcName)s:%(lineno)d:%(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)
logger = logging.getLogger("MainWindow")

try:
    config = configparser.ConfigParser()
    config.read("./settings.properties")
    language = config.get("form", "language")
    style = config.get("form", "style")
except configparser.NoSectionError:
    logger.error("settings.properties is invalid or it does not exist. (configparser.NoSectionError)")
    language = ""
    style = ""
# Read settings from settings.properties

if style not in FormStyle.list_themes():
    logger.warning("A non-existent theme has appeared.")


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
        self.aboutDialog.buttonBox.helpRequested.connect(self.help)
        logger.info("About window opened.")
        self.aboutDialog.show()

    def openFile(self):
        logger.info("openFile function called.")
        self.filePath = QFileDialog.getOpenFileName(self, "Open a file", "", "All files(*.*)")[0]
        if os.path.getsize(self.filePath) >= 1073741824:  # 1 GiB
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

    def help(self):
        logger.info("Help function called.")
        # TODO: 完成帮助文档


class SettingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./ui/favicon.ico"))
        self.setFixedSize(self.size())


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
    if translator.load(language, "./ui/i18n"):
        app.installTranslator(translator)
    window = MainWindow()
    window.setWindowIcon(QIcon("./ui/favicon.ico"))
    window.setWindowTitle("Whale - New File")
    FormStyle.apply_stylesheet(app, style)
    logger.info("Application started.")
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    entryPoint()

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTranslator
import qt_material as FormStyle
from ui.form import Ui_MainWindow
from ui.settings import Ui_Dialog as Ui_SettingsDialog
import configparser
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)
logger = logging.getLogger("MainWindow")

try:
    config = configparser.ConfigParser()
    config.read("./settings.properties")
    language = config.get("form", "language")
    style = config.get("form", "style")
except configparser.NoSectionError:
    logger.error("main.py:20:settings.properties is invalid or it does not exist. (configparser.NoSectionError)")
    language = ""
    style = ""
# Read settings from settings.properties

if style not in FormStyle.list_themes():
    logger.warning("main.py:22:A non-existent theme has appeared.")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connect actions to the functions
        self.actionSettings.triggered.connect(self.settingsWindow)

    def settingsWindow(self):
        self.settingsDialog = SettingsDialog()
        self.settingsDialog.show()


class SettingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):
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
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    entryPoint()

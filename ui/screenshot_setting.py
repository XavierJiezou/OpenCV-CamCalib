from string import Template
from PySide6.QtWidgets import QFileDialog, QDialog, QMessageBox, QApplication, QInputDialog, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, Slot, QFile
from PySide6.QtUiTools import QUiLoader

from ui.ui_screenshot import Ui_Dialog


class ScreenshotSetting(QDialog, Ui_Dialog):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
    
    @Slot()
    def on_toolButton_clicked(self):
        save_dir = QFileDialog().getExistingDirectory(self, '选择截图保存位置')
        self.lineEdit.setText(save_dir)
        self.lineEdit.setEnabled(False)
        self.lineEdit.clearFocus()

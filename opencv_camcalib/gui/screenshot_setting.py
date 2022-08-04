import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog

from opencv_camcalib.gui.config import icon_path
from opencv_camcalib.gui.ui.screenshot_setting import Ui_Dialog


class ScreenshotSetting(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowIcon(QIcon(icon_path))

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    @Slot()
    def on_toolButton_clicked(self) -> None:
        save_dir = QFileDialog().getExistingDirectory(self, "选择截图保存位置")

        self.ui.lineEdit.setText(save_dir)
        self.ui.lineEdit.setEnabled(False)
        self.ui.lineEdit.clearFocus()


def main() -> None:
    app = QApplication()
    win = ScreenshotSetting()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

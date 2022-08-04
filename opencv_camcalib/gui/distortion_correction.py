import os
import sys

import cv2 as cv
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from rich.progress import track

from opencv_camcalib.core import CamCalibCore
from opencv_camcalib.gui.config import icon_path
from opencv_camcalib.gui.ui.distortion_correction import Ui_Dialog


class DistortionCorrection(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowIcon(QIcon(icon_path))

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.core = CamCalibCore()

    @Slot()
    def on_toolButton_clicked(self) -> None:
        save_dir = QFileDialog().getExistingDirectory(self, "选择数据")
        self.ui.lineEdit.setText(save_dir)
        self.ui.lineEdit.setEnabled(False)
        self.ui.lineEdit.clearFocus()

    @Slot()
    def on_toolButton_2_clicked(self) -> None:
        matrix_path = QFileDialog().getOpenFileName(self, "相机参数", "*.json", "json")[0]
        self.ui.lineEdit_2.setText(matrix_path)
        self.ui.lineEdit_2.setEnabled(False)
        self.ui.lineEdit_2.clearFocus()

    @Slot()
    def on_pushButton_clicked(self) -> None:
        data_dir = self.ui.lineEdit.text()
        camera_matrix = self.ui.lineEdit_2.text()
        alpha = float(self.ui.doubleSpinBox.text())
        crop_edge = self.ui.checkBox.isChecked()
        ret = self.core.undistort(data_dir, camera_matrix, alpha, crop_edge)
        self.data = ret["data"]
        QMessageBox.information(self, "纠正成功", ret["msg"])

    @Slot()
    def on_pushButton_2_clicked(self) -> None:
        save_dir = QFileDialog().getExistingDirectory(self, "保存位置")
        for k, v in track(self.data.items(), description="Writing..."):
            cv.imwrite(os.path.join(save_dir, k), v)
        QMessageBox.information(self, "保存成功", f"共保存完成{len(self.data)}张纠正的图像")


def main() -> None:
    app = QApplication()
    win = DistortionCorrection()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

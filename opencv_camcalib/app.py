import os
import sys
import time

import cv2
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QApplication, QInputDialog, QMainWindow, QMessageBox

from opencv_camcalib.gui.chessboard_calibration import ChessboardCalibration
from opencv_camcalib.gui.config import icon_path, main_size
from opencv_camcalib.gui.distortion_correction import DistortionCorrection
from opencv_camcalib.gui.screenshot_setting import ScreenshotSetting
from opencv_camcalib.gui.ui.main_window import Ui_MainWindow


class SimpleVideoPlayer(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowIcon(QIcon(icon_path))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.screenshot_setting_dialog = ScreenshotSetting()
        self.chessboard_calibration_dialog = ChessboardCalibration()
        self.distortion_correction_dialog = DistortionCorrection()

        self.ui.play_button.setEnabled(True)
        self.ui.shot_button.setEnabled(False)
        self.ui.stop_button.setEnabled(False)

        self.ui.about_us.triggered.connect(self.about_us)
        self.ui.data_collection.triggered.connect(self.data_collection)
        self.ui.camera_address.triggered.connect(self.camera_address)
        self.ui.screenshot_setting.triggered.connect(self.screenshot_setting)
        self.ui.chessboard_calibration.triggered.connect(self.chessboard_calibration)
        self.ui.distortion_correction.triggered.connect(self.distortion_correction)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    @Slot()
    def distortion_correction(self) -> None:
        self.distortion_correction_dialog.show()

    @Slot()
    def chessboard_calibration(self) -> None:
        self.chessboard_calibration_dialog.show()

    @Slot()
    def screenshot_setting(self) -> None:
        self.screenshot_setting_dialog.show()

    @Slot()
    def camera_address(self) -> None:
        camera_address, is_ok = QInputDialog().getText(
            self,
            "相机地址",
            "请输入相机地址",
        )
        if is_ok:
            self.start_update(camera_address)

    @Slot()
    def data_collection(self) -> None:
        QMessageBox.information(
            self,
            "数据采集",
            "1. 单台相机至少需要采集 15~20 张图片\n" "2. 尽量保证标定板上的光照足够且均匀\n" "3. 标定过程中不能改变相机光圈或焦距",
        )

    @Slot()
    def about_us(self) -> None:
        QMessageBox.about(
            self,
            "关于我们",
            "Version 0.1.2",
        )

    @Slot()
    def update_frame(self) -> None:
        if self.status:
            ret, frame = self.cap.read()
            if ret:
                self.frames = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, _ = self.frames.shape
                image = QImage(
                    self.frames,
                    w,
                    h,
                    self.frames.strides[0],
                    QImage.Format_RGB888,
                )
                self.ui.image_label.setPixmap(
                    QPixmap.fromImage(image).scaled(
                        self.ui.image_label.size(), Qt.KeepAspectRatio
                    )
                )
            else:
                pass
        else:
            pass

    @Slot()
    def start(self) -> None:
        self.status = True
        self.timer.start()
        self.ui.play_button.setEnabled(True)
        self.ui.shot_button.setEnabled(True)
        self.ui.stop_button.setEnabled(True)

    @Slot()
    def stop(self) -> None:
        self.status = False
        self.timer.stop()
        if hasattr(self, "cap"):
            self.cap.release()
        else:
            pass
        self.ui.play_button.setEnabled(True)
        self.ui.shot_button.setEnabled(True)
        self.ui.stop_button.setEnabled(False)

    @Slot()
    def start_update(self, url: str) -> None:
        self.cap = cv2.VideoCapture(url)
        if self.cap.isOpened():
            self.ui.url_input.setText(url)
            self.ui.image_label.setText("正在加载视频..")
            self.start()
        else:
            self.ui.image_label.setText("无效的视频链接")
            self.stop()
            self.ui.shot_button.setEnabled(False)

    @Slot()
    def on_url_input_textChanged(self) -> None:
        if hasattr(self, "cap") and self.cap.isOpened():
            pass
        elif not self.ui.url_input.text():
            self.ui.image_label.setText("请输入视频链接")
        else:
            pass

    @Slot()
    def on_url_input_editingFinished(self) -> None:
        self.start_update(self.ui.url_input.text())

    @Slot()
    def on_play_button_clicked(self) -> None:
        self.start_update(self.ui.url_input.text())

    @Slot()
    def on_shot_button_clicked(self) -> None:
        save_dir = self.screenshot_setting_dialog.ui.lineEdit.text()
        print(save_dir)
        if self.screenshot_setting_dialog.ui.radioButton.isChecked():
            save_format = "bmp"
        elif self.screenshot_setting_dialog.ui.radioButton_2.isChecked():
            save_format = "png"
        else:
            save_format = "jpg"
        save_name = f"{round(time.time())}.{save_format}"
        save_path = os.path.join(save_dir, save_name)
        cv2.imwrite(save_path, self.frames)

    @Slot()
    def on_stop_button_clicked(self) -> None:
        self.stop()


def main() -> None:
    app = QApplication()
    win = SimpleVideoPlayer()
    win.resize(*(main_size))
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

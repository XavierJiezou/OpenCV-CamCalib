import os
import sys
import time

import cv2
from PySide6.QtWidgets import QFileDialog, QDialog, QMessageBox, QApplication, QInputDialog, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, Slot, QFile, Qt


from ui.ui_mainwindow import Ui_MainWindow
from ui.screenshot_setting import ScreenshotSetting


class SimpleVideoPlayer(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.screenshot_dialog = ScreenshotSetting()

        self.ui.play_button.setEnabled(True)
        self.ui.shot_button.setEnabled(False)
        self.ui.stop_button.setEnabled(False)

        self.ui.about_us.triggered.connect(self.about_us)
        self.ui.data_collection.triggered.connect(self.data_collection)
        self.ui.camera_address.triggered.connect(self.camera_address)
        self.ui.screenshot_setting.triggered.connect(self.screenshot_setting)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    @Slot()
    def screenshot_setting(self):
        self.screenshot_dialog.show()

    @Slot()
    def camera_address(self):
        input_dialog = QInputDialog()
        camera_address, is_ok = input_dialog.getText(
            self,
            '相机地址',
            '请输入相机地址',
        )
        if is_ok:
            self.start_update(camera_address)

    @Slot()
    def data_collection(self):
        QMessageBox.information(
            self,
            "数据采集",
            "1. 单台相机至少需要采集 15-20 张图片\n"
            "2. 尽量保证棋盘的光照足够且均匀（不宜曝光）\n"
            "3. 标定过程中不能改变相机的光圈或焦距",
        )

    @Slot()
    def about_us(self):
        QMessageBox.about(
            self,
            "关于我们",
            "Version 1.0.1",
        )

    @Slot()
    def update_frame(self):
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
                        self.ui.image_label.size(), Qt.KeepAspectRatio)
                )
            else:
                pass
        else:
            pass

    @Slot()
    def start(self):
        self.status = True
        self.timer.start()
        self.ui.play_button.setEnabled(True)
        self.ui.shot_button.setEnabled(True)
        self.ui.stop_button.setEnabled(True)

    @Slot()
    def stop(self):
        self.status = False
        self.timer.stop()
        if hasattr(self, 'cap'):
            self.cap.release()
        else:
            pass
        self.ui.play_button.setEnabled(True)
        self.ui.shot_button.setEnabled(True)
        self.ui.stop_button.setEnabled(False)

    @Slot()
    def start_update(self, url):
        self.cap = cv2.VideoCapture(url)
        if self.cap.isOpened():
            self.ui.url_input.setText(url)
            self.ui.image_label.setText('正在加载视频..')
            self.start()
        else:
            self.ui.image_label.setText('无效的视频链接')
            self.stop()
            self.ui.shot_button.setEnabled(False)

    @Slot()
    def on_url_input_textChanged(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            pass
        elif not self.ui.url_input.text():
            self.ui.image_label.setText('请输入视频链接')
        else:
            pass

    @Slot()
    def on_url_input_editingFinished(self):
        self.start_update(self.ui.url_input.text())

    @Slot()
    def on_play_button_clicked(self):
        self.start_update(self.ui.url_input.text())

    @Slot()
    def on_shot_button_clicked(self):
        save_dir = self.screenshot_dialog.lineEdit.text()
        if self.screenshot_dialog.radioButton.isChecked():
            save_format = 'bmp'
        elif self.screenshot_dialog.radioButton_2.isChecked():
            save_format = 'png'
        else:
            save_format = 'jpg'
        save_name = f'{round(time.time())}.{save_format}'
        save_path = os.path.join(save_dir, save_name)
        cv2.imwrite(save_path, self.frames)

    @Slot()
    def on_stop_button_clicked(self):
        self.stop()


if __name__ == '__main__':  # rtsp://admin:abcd8403@172.16.14.37:20001
    app = QApplication([])
    widget = SimpleVideoPlayer()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())

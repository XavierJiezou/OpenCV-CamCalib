import json
import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox

from opencv_camcalib.core import CamCalibCore
from opencv_camcalib.gui.config import icon_path
from opencv_camcalib.gui.ui.chessboard_calibration import Ui_Dialog


class ChessboardCalibration(QDialog):
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
    def on_pushButton_clicked(self) -> None:
        data_dir = self.ui.lineEdit.text()
        rows = int(self.ui.spinBox.text())
        cols = int(self.ui.spinBox_2.text())
        square_size = int(self.ui.lineEdit_2.text())
        draw_pattern = self.ui.checkBox.isChecked()
        info = self.core.calibrate(
            data_dir,
            rows,
            cols,
            square_size,
            draw_pattern,
        )
        self.info = info
        QMessageBox.information(self, "标定结果", info["msg"])
        if info["status"] == "success":
            mtx_str = ""
            for i in info["data"]["mtx"]:
                for j in i:
                    mtx_str += f"{j:.2f}\t"
                mtx_str += "<br>"
            mtx_str += f"f<sub>x</sub>: {info['data']['mtx'][0][0]:.2f}<br>"
            mtx_str += f"f<sub>y</sub>: {info['data']['mtx'][1][1]:.2f}<br>"
            mtx_str += f"c<sub>x</sub>: {info['data']['mtx'][0][2]:.2f}<br>"
            mtx_str += f"c<sub>y</sub>: {info['data']['mtx'][1][2]:.2f}<br>"
            self.ui.textBrowser.setText(mtx_str)
            dist_str = ""
            for k, v in zip(
                [
                    "k<sub>1</sub>",
                    "k<sub>2</sub>",
                    "p<sub>1</sub>",
                    "p<sub>2</sub>",
                    "k<sub>3</sub>",
                ],
                info["data"]["dist"][0],
            ):
                dist_str += f"{k}: {v:.4f}<br>"
            self.ui.textBrowser_2.setText(dist_str)
            rvecs_str = "R: \n"
            for i in info["data"]["rvecs"]:
                tmp = ", ".join([f"{j[0]:.4f}" for j in i])
                rvecs_str += f"[{tmp}]\n"
            tvecs_str = "T: \n"
            for i in info["data"]["tvecs"]:
                tmp = ", ".join([f"{j[0]:.4f}" for j in i])
                tvecs_str += f"[{tmp}]\n"
            self.ui.textBrowser_3.setText(rvecs_str + tvecs_str)
            error_str = (
                f"RMS: {info['data']['rms']:.4f}\nMSE: {info['data']['mse']:.4f}"
            )
            self.ui.textBrowser_4.setText(error_str)
        else:
            pass

    @Slot()
    def on_pushButton_2_clicked(self) -> None:
        save_path = QFileDialog().getSaveFileName(
            self, "保存路径", "camera_matrix.json", "json"
        )[0]
        with open(save_path, "w") as f:
            json.dump(self.info, f)


def main() -> None:
    app = QApplication()
    win = ChessboardCalibration()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

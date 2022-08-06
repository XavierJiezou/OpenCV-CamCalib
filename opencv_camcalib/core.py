import glob
import json
import os
import time
from typing import Any, Dict, Tuple, Union

import cv2 as cv
import numpy as np
from func_timeout import FunctionTimedOut, func_timeout
from rich import print as rich_print
from rich.progress import track

from opencv_camcalib import __version__


class CamCalibCore:
    @property
    def version(self) -> str:
        return __version__

    def capture(
        self, camera_address: Union[str, int], save_dir: str = "screenshot"
    ) -> Dict[str, Any]:
        try:
            cap = func_timeout(3, cv.VideoCapture, (camera_address,))
        except FunctionTimedOut:
            info = {
                "status": "failure",
                "data": "",
                "msg": "连接超时，请检查相机地址",
            }
            return info
        if not cap.isOpened():
            info = {
                "status": "failure",
                "data": "",
                "msg": "打开失败，请检测相机地址",
            }
        else:
            count = 0
            imgs = {}
            while True:
                ret, frame = cap.read()
                if not ret:
                    info = {
                        "status": "failure",
                        "data": "",
                        "msg": "读取失败，流结束？退出...",
                    }
                    break
                else:
                    cv.imshow("Press w for screenshot | q to exit", frame)
                    key = cv.waitKey(1)
                    if key == ord("q"):
                        info = {
                            "status": "success",
                            "data": imgs,
                            "msg": "检测到 q 被按压，退出...",
                        }
                        break
                    elif key == ord("w"):
                        os.makedirs(save_dir, exist_ok=True)
                        name = f"{round(time.time())}.png"
                        path = os.path.join(save_dir, name)
                        imgs[path] = frame
                        cv.imwrite(path, frame)
                        count += 1
                        rich_print(f"检测到 w 被按压，截图 {count:0>2} 保存至 {path}")
                    else:
                        pass
        cap.release()
        cv.destroyAllWindows()
        return info

    def calibrate(
        self,
        data_dir: str,
        rows: int = 9,
        cols: int = 6,
        square_size: int = 30,
        draw_pattern: bool = False,
        pattern_type: str = "chessboard",
        win_size: Tuple[int, int] = (11, 11),
    ) -> Dict[str, Any]:
        criteria = (
            cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,
            30,
            1e-4,
        )
        objp = np.zeros((rows * cols, 3), np.float32)
        objp[:, :2] = np.mgrid[
            0 : rows * square_size : square_size,
            0 : cols * square_size : square_size,
        ].T.reshape(-1, 2)
        objpoints = []
        imgpoints = []
        not_found = []

        def func() -> Any:
            for fname in track(os.listdir(data_dir), description="Calibrating..."):
                img = cv.imread(os.path.join(data_dir, fname))
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                if pattern_type == "chessboard":
                    ret, corners = cv.findChessboardCorners(gray, (rows, cols), None)
                else:
                    pass
                if ret:
                    objpoints.append(objp)
                    corners2 = cv.cornerSubPix(
                        gray, corners, win_size, (-1, -1), criteria
                    )
                    imgpoints.append(corners)
                    if draw_pattern:
                        cv.drawChessboardCorners(img, (rows, cols), corners2, ret)
                        cv.imshow("img", img)
                        cv.waitKey(500)
                    else:
                        pass
                else:
                    not_found.append(fname)
            return gray

        try:
            if not draw_pattern:
                gray = func_timeout(5, func)
            else:
                gray = func_timeout(5 + 0.5 * len(os.listdir(data_dir)), func)
        except FunctionTimedOut:
            return {
                "status": "failure",
                "data": "",
                "msg": "标定超时，请检查标定尺寸",
            }
        cv.destroyAllWindows()
        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(
            objpoints,
            imgpoints,
            gray.shape[::-1],
            None,
            None,
        )
        mean_error = 0
        for i in range(len(objpoints)):
            imgpoints2, _ = cv.projectPoints(
                objpoints[i], rvecs[i], tvecs[i], mtx, dist
            )
            error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2) / len(imgpoints2)
            mean_error += error
        if not_found:
            msg = f"共标定完成{len(objpoints)-len(not_found)}张图像，{not_found}无法检测"
        else:
            msg = f"共标定完成{len(objpoints)}张图像"
        info = {
            "status": "success",
            "data": {
                "rms": ret,
                "mse": mean_error / len(objpoints),
                "mtx": mtx.tolist(),
                "dist": dist.tolist(),
                "rvecs": [i.tolist() for i in rvecs],
                "tvecs": [i.tolist() for i in tvecs],
            },
            "msg": msg,
        }
        return info

    def undistort(
        self,
        data_dir: str,
        camera_matrix: str = "camera_matrix.json",
        alpha: int = 1,
        crop_edge: bool = False,
    ) -> None:
        with open(camera_matrix, encoding="utf-8") as f:
            cfg = json.load(f)["data"]
        mtx = np.array(cfg["mtx"])
        dist = np.array(cfg["dist"])
        h, w = cv.imread(glob.glob(os.path.join(data_dir, "*"))[0]).shape[:2]
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(
            mtx, dist, (w, h), alpha, (w, h)
        )
        mapx, mapy = cv.initUndistortRectifyMap(
            mtx, dist, None, newcameramtx, (w, h), 5
        )
        undistorted = {}
        for fname in track(os.listdir(data_dir), description="Undistorting..."):
            img = cv.imread(os.path.join(os.path.join(data_dir, fname)))
            dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
            if crop_edge:
                x, y, w, h = roi
                dst = dst[y : y + h, x : x + w]
            else:
                pass
            undistorted[fname] = dst
        return {
            "status": "success",
            "data": undistorted,
            "msg": f"共纠正完成{len(undistorted)}张失真的图像",
        }

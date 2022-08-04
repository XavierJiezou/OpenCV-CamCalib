import json
import os
from typing import Tuple, Union

import cv2 as cv
import fire
from rich.console import Console
from rich.progress import track

from opencv_camcalib.core import CamCalibCore


class CamCalibCLI:
    def __init__(self) -> None:
        super().__init__()
        self.core = CamCalibCore()
        self.console = Console()

    def version(self) -> str:
        return self.console.print(self.core.version)

    def capture(
        self, camera_address: Union[str, int], save_dir: str = "screenshot"
    ) -> str:
        return self.console.print(self.core.capture(camera_address, save_dir))

    def calibrate(
        self,
        data_dir: str,
        rows: int = 9,
        cols: int = 6,
        square_size: int = 30,
        draw_pattern: bool = False,
        pattern_type: str = "chessboard",
        win_size: Tuple[int, int] = (11, 11),
        save_calibration: str = "camera_matrix.json",
    ) -> str:
        info = self.core.calibrate(
            data_dir,
            rows,
            cols,
            square_size,
            draw_pattern,
            pattern_type,
            win_size,
        )
        if info["status"] == "success":
            with open(save_calibration, "w", encoding="utf-8") as f:
                json.dump(info, f, ensure_ascii=False)
            self.console.print(f"标定完成，结果已保存至 ./{save_calibration}")
        else:
            pass
        return self.console.print(info)

    def undistort(
        self,
        data_dir: str,
        camera_matrix: str = "camera_matrix.json",
        alpha: int = 1,
        crop_edge: bool = False,
        save_dir: str = "undistorted",
    ) -> str:
        ret = self.core.undistort(
            data_dir,
            camera_matrix,
            alpha,
            crop_edge,
        )
        for k, v in track(ret["data"].items(), description="Writing..."):
            cv.imwrite(os.path.join(save_dir, k), v)
        return self.console.print(ret)


def main() -> None:
    fire.Fire(CamCalibCLI)


if __name__ == "__main__":
    main()

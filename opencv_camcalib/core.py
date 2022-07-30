import time
from typing import Dict, Union

import cv2 as cv
from func_timeout import FunctionTimedOut, func_timeout

from opencv_camcalib import __version__


class CamCalibCore:
    @property
    def version(self) -> str:
        return __version__

    def capture(self, camera_address: Union[str, int]) -> Dict[str, str]:
        try:
            cap = func_timeout(3, cv.VideoCapture, (camera_address,))
        except FunctionTimedOut:
            info = {
                "status": "failure",
                "error": "timeout",
                "msg": "cannot open camera, please check your address.",
            }
            return info
        if not cap.isOpened():
            info = {
                "status": "failure",
                "error": "open",
                "msg": "cannot open camera, please check your address.",
            }
        else:
            count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    info = {
                        "status": "failure",
                        "error": "receive",
                        "msg": "Can't receive frame (stream end?). Exiting ...",
                    }
                    break
                else:
                    cv.imshow("Press q to exit, w for screenshot", frame)
                    if cv.waitKey(1) == ord("q"):
                        info = {
                            "status": "success",
                            "data": "",
                            "msg": "q was pressed. Exiting ...",
                        }
                        break
                    elif cv.waitKey(1) == ord("w"):
                        name = f"{round(time.time())}.png"
                        cv.imwrite(name, frame)
                        count += 1
                        print(f"screenshot {count:0>2} is saved to ./{name}")
        cap.release()
        cv.destroyAllWindows()
        return info

    def calibrate(self, data_dir: str, pattern: str) -> None:
        pass

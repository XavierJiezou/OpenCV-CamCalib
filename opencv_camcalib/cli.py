import json
from typing import Union

import fire
from rich.console import Console

from opencv_camcalib.core import CamCalibCore


class CamCalibCLI:
    def __init__(self) -> None:
        super().__init__()
        self.core = CamCalibCore()
        self.console = Console()

    def version(self) -> str:
        return self.console.print(self.core.version)

    def capture(self, camera_address: Union[str, int]) -> str:
        return self.console.print_json(json.dumps(self.core.capture(camera_address)))


def main() -> None:
    fire.Fire(CamCalibCLI)


if __name__ == "__main__":
    main()

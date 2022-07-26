import fire

from opencv_camcalib.core import CamCalibCore


class CamCalibCLI(CamCalibCore):
    def __init__(self) -> None:
        super().__init__()

    def version(self) -> str:
        return self.version


def main() -> None:
    fire.Fire(CamCalibCLI)


if __name__ == "__main__":
    main()

import toml

from opencv_camcalib.core import CamCalibCore


class TestCamCalibCore(CamCalibCore):
    def test_version(self):
        assert self.version == toml.load("pyproject.toml")["tool"]["poetry"]["version"]

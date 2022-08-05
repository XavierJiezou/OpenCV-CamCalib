import os
import sys


def resource_path(relative_path: str) -> None:
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


icon_path = resource_path("images/favicon_256x256.ico")
main_size = (800, 600)

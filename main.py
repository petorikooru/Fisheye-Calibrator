# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication
from controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainController()
    widget.setWindowTitle("Fisheye Camera Calibrator")
    widget.show()
    sys.exit(app.exec())

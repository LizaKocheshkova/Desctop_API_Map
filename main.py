import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Window(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
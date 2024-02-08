import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from API.api import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('win_map.ui', self)
        self.setWindowTitle('Приложение для Яндекс карт')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
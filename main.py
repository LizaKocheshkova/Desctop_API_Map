import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import Qt
from API.api import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('win_map.ui', self)
        self.setWindowTitle('Приложение для Яндекс карт')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            print("PgUp")
        if event.key() == Qt.Key_PageDown:
            print("PgDn")
        if event.key() == Qt.Key_Up:
            print("Up")
        if event.key() == Qt.Key_Down:
            print("Down")
        if event.key() == Qt.Key_Right:
            print("Right")
        if event.key() == Qt.Key_Left:
            print("Left")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
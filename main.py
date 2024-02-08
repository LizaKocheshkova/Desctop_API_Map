from PyQt5.QtGui import QPixmap
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
        self.btn_show_map.clicked.connect(self.show_map)
        self.delta = 0.002
        self.up = 0
        self.r = 0

    def show_map(self):
        address = self.input_address.text()
        longitude = self.input_long.text()
        latitude = self.input_width.text()
        image_map(str(self.delta), adress=address, lon=longitude, lat=latitude, up=self.up, r=self.r)
        try:
            self.pixmap = QPixmap('map.png')
            self.label_map.setPixmap(self.pixmap)
        except Exception:
            pass

    def keyPressEvent(self, event):
        print(event.key(), Qt.Key_Right, Qt.Key_Left)
        if event.key() == Qt.Key_PageUp:
            print("PgUp")
            self.delta += 0.003
            self.show_map()
        if event.key() == Qt.Key_PageDown:
            print("PgDn")
            if self.delta > 0.003:
                self.delta -= 0.003
            self.show_map()
        if event.key() == Qt.Key_Up:
            print("Up")
            self.up += self.delta
            self.show_map()
        if event.key() == Qt.Key_Down:
            print("Down")
            self.up -= self.delta
            self.show_map()
        if event.key() == Qt.Key_Right:
            print("Right")
            self.r += self.delta
            self.show_map()
        if event.key() == Qt.Key_Left:
            print("Left")
            self.r -= self.delta
            self.show_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import Qt
from API.api import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Приложение для Яндекс карт')
        self.setGeometry(800, 800, 800, 800)
        self.delta = 0.002
        self.long = '0'
        self.width = '0'

    def keyPressEvent(self, event):
        print(event.key(), Qt.Key_Right, Qt.Key_Left)
        if event.key() == Qt.Key_PageUp:
            self.delta += 0.003
            self.show_map()
        if event.key() == Qt.Key_PageDown:
            if self.delta > 0.003:
                self.delta -= 0.003
            self.show_map()
        if event.key() == Qt.Key_Up:
            self.width = str(float(self.width) + self.delta)
            self.show_map()
        if event.key() == Qt.Key_Down:
            self.width = str(float(self.width) - self.delta)
            self.show_map()
        if event.key() == Qt.Key_Right:
            self.long = str(float(self.long) + self.delta)
            self.show_map()
        if event.key() == Qt.Key_Left:
            self.long = str(float(self.long) - self.delta)
            self.show_map()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

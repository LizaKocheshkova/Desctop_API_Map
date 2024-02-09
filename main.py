from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
from API.api import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('win_map.ui', self)
        self.setWindowTitle('Приложение для Яндекс карт')
        self.btn_show_map.clicked.connect(self.show_map)
        self.btn_input_data.clicked.connect(self.show_win_input_data)
        self.delta = 0.002
        self.up = 0
        self.r = 0

    def show_map(self):  # тут нужно переделать, получить данные из диалогового окна для показа карты
        address = self.input_address.text()
        longitude = self.input_long.text()  # эти три строки скорее всего поменяются или уберутся
        latitude = self.input_width.text()
        image_map(str(self.delta), address=address, lon=longitude, lat=latitude, up=self.up, r=self.r)
        try:
            self.pixmap = QPixmap('map.png')
            self.label_map.setPixmap(self.pixmap)
        except Exception:
            pass

    def show_win_input_data(self):
        print('ok')
        self.data = InputData()
        self.data.show()
        if self.data.exec_() == QDialog.Accepted:
            self.update_welcome()

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


class InputData(QDialog):
    def __init__(self):
        super(InputData, self).__init__()
        uic.loadUi('input_data.ui', self)
        self.setWindowTitle('Ввод данных')
        self.buttonBox.accepted.connect(self.input_data_ok)
        self.buttonBox.rejected.connect(self.log_user_not)

    def input_data_ok(self):  # тут нужно доделать сохранение введенных данных для передачи их в функцию показа карты
        address = self.input_address.text()
        longitude = self.input_long.text()
        latitude = self.input_width.text()

    def input_data_not(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

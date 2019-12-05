import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        loadUi('main.ui',self)
        self.label_img.setPixmap(QPixmap('ex2.png'))
        self.label_img.setScaledContents(True)

        self.pushButton.clicked.connect(self.solve)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.exit)
    def solve(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        x = self.lineEdit_3.text()
        try:
            a = float(a)
            b = float(b)
            x = float(x)
            try:
                if x < 7:
                    y = (x ** 2 + a ** 2 + b ** 2) / (a + b)
                else:
                    y = (x ** 3) * ((a + b) ** 2)
                self.label_4.setText('Ответ = ' + str(format(y, '.2f')))
            except:
                self.label_4.setText('Нет решения')
        except:
            self.label_4.setText('Неверные данные')

    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.label_4.setText('Ответ = ')

    def exit(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


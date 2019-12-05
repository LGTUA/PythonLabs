import sys
import math

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from random import randint

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui',self)

        self.label.setPixmap(QPixmap('ex9.png'))
        self.label.setScaledContents(True)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        tableWidth = self.tableWidget.geometry().width()
        tableHeight = self.tableWidget.geometry().height() - 21
        row = 0
        col = 0
        while row < maxRows:
            self.tableWidget.setRowHeight(row, tableHeight / maxRows)
            row += 1
        while col < maxColumns:
            self.tableWidget.setColumnWidth(col, tableWidth / maxColumns)
            col += 1
        self.tableWidget.setItem(0, 0, QTableWidgetItem(""))

        maxRows = self.tableWidget_2.rowCount()
        maxColumns = self.tableWidget_2.columnCount()
        # headerHeight = float(self.tableWidget.horizontalHeaderSize())
        tableWidth = self.tableWidget_2.geometry().width()
        tableHeight = self.tableWidget_2.geometry().height()
        row = 0
        col = 0
        while row < maxRows:
            self.tableWidget_2.setRowHeight(row, tableHeight / maxRows)
            row += 1
        while col < maxColumns:
            self.tableWidget_2.setColumnWidth(col, tableWidth / maxColumns)
            col += 1
        self.tableWidget_2.setItem(0, 0, QTableWidgetItem("a"))
        self.tableWidget_2.setItem(0, 1, QTableWidgetItem("x"))
        self.tableWidget_2.setItem(1, 0, QTableWidgetItem("0"))
        self.tableWidget_2.setItem(1, 1, QTableWidgetItem("0"))

        self.pushButton_2.clicked.connect(self.fillRandom)
        self.pushButton_3.clicked.connect(self.clearTable)
        self.pushButton_4.clicked.connect(self.solve)
        self.pushButton_5.clicked.connect(self.exit)

    def fillRandom(self):
        row = 0
        maxRows = self.tableWidget.rowCount()
        while row < maxRows:
            randNum = randint(0, 100)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(randNum)))
            row += 1

    def solve(self):
        Solution.solve(self)

    def clearTable(self):
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        row = 0
        col = 0
        while row < maxRows:
            while col < maxColumns:
                self.tableWidget.setItem(row, col, QTableWidgetItem(""))
                col += 1
            row += 1
            col = 0

    def exit(self):
        self.close()


class Solution(Main):
    def __init__(self):
        pass

    def solve(self):
        if not self.tableWidget.item(0, 0).text():
            self.label_2.setText("Заполните слева таблицу числами")
            return
        try:
            a = float(self.tableWidget_2.item(1, 0).text())
            x = float(self.tableWidget_2.item(1, 1).text())
        except:
            self.label_2.setText("Неверно заданы a, x")
            return
        for i in range(10):
            try:
                ki = float(self.tableWidget.item(i, 0).text())
                try :
                    kii = float(self.tableWidget.item(i - 1, 0).text())
                except :
                    kii = 0
                y = math.sqrt(a ** 2 + x ** 4) / math.factorial(i) * (math.sin(ki) - math.cos(kii))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(y)))
            except:
                self.tableWidget.setItem(i, 1, QTableWidgetItem("Нет решения"))


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
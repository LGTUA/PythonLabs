import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from random import randint


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        tableWidth = self.tableWidget.geometry().width()
        tableHeight = self.tableWidget.geometry().height()
        self.pushButton.clicked.connect(self.fillRandom)
        self.pushButton_2.clicked.connect(self.solve)
        row = 0
        col = 0
        while row < maxRows:
            self.tableWidget.setColumnWidth(row, tableWidth / maxRows)
            row += 1
        while col < maxColumns:
            self.tableWidget.setRowHeight(col, tableHeight / maxColumns)
            col += 1
        row = 0
        col = 0
        while row < maxRows:
            while col < maxColumns:
                randNum = randint(0, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(randNum)))
                col += 1
            row += 1
            col = 0

    def fillRandom (self):
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        row = 0
        col = 0
        while row < maxRows:
            while col < maxColumns:
                randNum = randint(0, 100)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(randNum)))
                col += 1
            row += 1
            col = 0
        self.label_3.setText('?')

    def solve(self):
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        row = 1
        col = 0
        k = 0
        while col < maxColumns:
            item = int(self.tableWidget.item(row, col).text())
            if item == 100:
                k += 2
            else:
                if item % 10 == 0:
                    k += 1
            col += 1
        self.label_3.setText(str(k))
        maxIndex = 0
        row = 1
        col = 1
        while row < maxRows:
            if int(self.tableWidget.item(row, col).text()) > int(self.tableWidget.item(maxIndex, col).text()):
                maxIndex = row
            row += 1
        self.tableWidget.setItem(maxIndex, col, QTableWidgetItem(str(k)))


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

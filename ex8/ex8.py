import sys

from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
# delete below
from PyQt5.QtWidgets import QListWidget, QCheckBox, QTableWidget, QLineEdit
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
data = [['', -1], ['', '', '', ''], ['', -1]]


class Form1 (QtWidgets.QMainWindow):
    switchWindow = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form1, self).__init__()
        uic.loadUi('form1.ui',self)
        self.btnExit.clicked.connect(self.close)
        self.btnNext.clicked.connect(self.next)

    def next(self):
        self.switchWindow.emit('1>2')


class Form2(QtWidgets.QMainWindow):
    switchWindow = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form2, self).__init__()
        uic.loadUi('form2.ui',self)
        self.labelImg.setPixmap(QPixmap('form2.jpg'))
        self.labelImg.setScaledContents(True)
        if data[0][1] >= 0 :
            self.label_3.setText(data[0][0])
            self.listWidget.setCurrentRow(data[0][1])
        else:
            self.listWidget.setCurrentRow(-1)
        self.btnPrev.clicked.connect(self.prev)
        self.btnNext.clicked.connect(self.next)
        self.listWidget.itemSelectionChanged.connect(self.itemSelect)

    def prev(self):
        self.switchWindow.emit('2>1')

    def next(self):
        self.switchWindow.emit('2>3')

    def itemSelect(self):
        data[0][0] = self.listWidget.currentItem().text()
        data[0][1] = self.listWidget.currentRow()
        self.label_3.setText(self.listWidget.currentItem().text())


class Form3(QtWidgets.QMainWindow):
    switchWindow = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form3, self).__init__()
        uic.loadUi('form3.ui', self)
        self.labelImg.setPixmap(QPixmap('form3.jpg'))
        self.labelImg.setScaledContents(True)
        self.btnPrev.clicked.connect(self.prev)
        self.btnNext.clicked.connect(self.next)
        if data[1][0] != '':
            self.checkBox_0.setCheckState(2)
        if data[1][1] != '':
            self.checkBox_1.setCheckState(2)
        if data[1][2] != '':
            self.checkBox_2.setCheckState(2)
        if data[1][2] != '':
            self.checkBox_2.setCheckState(2)
        self.label_3.setText(form3input(data[1]))
        self.checkBox_0.stateChanged.connect(self.cb0)
        self.checkBox_1.stateChanged.connect(self.cb1)
        self.checkBox_2.stateChanged.connect(self.cb2)
        self.checkBox_3.stateChanged.connect(self.cb3)

    def cb0(self):
        if self.checkBox_0.checkState() > 0 :
            data[1][0] = self.checkBox_0.text()
        else:
            data[1][0] = ''
        self.label_3.setText(form3input(data[1]))

    def cb1(self):
        if self.checkBox_1.checkState() > 0 :
            data[1][1] = self.checkBox_1.text()
        else:
            data[1][1] = ''
        self.label_3.setText(form3input(data[1]))

    def cb2(self):
        if self.checkBox_2.checkState() > 0 :
            data[1][2] = self.checkBox_2.text()
        else:
            data[1][2] = ''
        self.label_3.setText(form3input(data[1]))

    def cb3(self):
        if self.checkBox_3.checkState() > 0 :
            data[1][3] = self.checkBox_3.text()
        else:
            data[1][3] = ''
        self.label_3.setText(form3input(data[1]))
        print(data[1])


    def prev(self):
        self.switchWindow.emit('3>2')

    def next(self):
        self.switchWindow.emit('3>4')


class Form4(QtWidgets.QMainWindow):
    switchWindow = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form4, self).__init__()
        uic.loadUi('form4.ui',self)
        self.labelImg.setPixmap(QPixmap('form4.jpg'))
        self.labelImg.setScaledContents(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        tableWidth = self.tableWidget.geometry().width()
        tableHeight = self.tableWidget.geometry().height()
        row = 0
        col = 0
        while row < maxRows:
            self.tableWidget.setRowHeight(row, tableHeight / maxRows)
            row += 1
        while col < maxColumns:
            self.tableWidget.setColumnWidth(col, tableWidth / maxColumns)
            col += 1
        if data[2][1] >= 0:
            self.label_3.setText(data[2][0])
            self.tableWidget.setCurrentCell(data[2][1], 0)
        self.tableWidget.itemSelectionChanged.connect(self.itemSelect)
        self.btnPrev.clicked.connect(self.prev)
        self.btnNext.clicked.connect(self.next)

    def itemSelect(self):
        data[2][0] = self.tableWidget.currentItem().text()
        data[2][1] = self.tableWidget.currentRow()
        self.label_3.setText(self.tableWidget.currentItem().text())

    def prev(self):
        self.switchWindow.emit('4>3')

    def next(self):
        self.switchWindow.emit('4>5')


class Form5(QtWidgets.QMainWindow):
    switchWindow = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form5, self).__init__()
        uic.loadUi('form5.ui', self)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        maxRows = self.tableWidget.rowCount()
        maxColumns = self.tableWidget.columnCount()
        tableWidth = self.tableWidget.geometry().width()
        tableHeight = self.tableWidget.geometry().height()
        row = 0
        col = 0
        while row < maxRows:
            self.tableWidget.setRowHeight(row, tableHeight / maxRows - 21)
            row += 1
        while col < maxColumns:
            self.tableWidget.setColumnWidth(col, tableWidth / maxColumns)
            col += 1
        self.tableWidget.setItem(0, 1, QTableWidgetItem(data[0][0]))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(form3input(data[1])))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(data[2][0]))
        self.btnPrev.clicked.connect(self.prev)
        self.btnExit.clicked.connect(self.close)

    def prev(self):
        self.switchWindow.emit('5>4')


class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = Form1()
            self.form1.switchWindow.connect(self.select_forms)
            self.form1.show()

        if text == '1>2' :
            self.form2 = Form2()
            self.form2.switchWindow.connect(self.select_forms)
            self.form2.show()
            self.form1.close()

        if text == '2>3':
            self.form3 = Form3()
            self.form3.switchWindow.connect(self.select_forms)
            self.form3.show()
            self.form2.close()

        if text == '3>4':
            self.form4 = Form4()
            self.form4.switchWindow.connect(self.select_forms)
            self.form4.show()
            self.form3.close()

        if text == '4>5':
            self.form5 = Form5()
            self.form5.switchWindow.connect(self.select_forms)
            self.form5.show()
            self.form4.close()

        if text == '5>4':
            self.form4 = Form4()
            self.form4.switchWindow.connect(self.select_forms)
            self.form4.show()
            self.form5.close()

        if text == '4>3':
            self.form3 = Form3()
            self.form3.switchWindow.connect(self.select_forms)
            self.form3.show()
            self.form4.close()

        if text == '3>2':
            self.form2 = Form2()
            self.form2.switchWindow.connect(self.select_forms)
            self.form3.close()
            self.form2.show()

        if text == '2>1':
            self.form1 = Form1()
            self.form1.switchWindow.connect(self.select_forms)
            self.form1.show()
            self.form2.close()


def form3input(array):
    tempvar = 0
    tempstr = ''
    for i in range(4):
        if array [i] != '':
            if tempvar == 0:
                tempstr += array[i]
                tempvar += 1
            else:
                tempstr += ', ' + array[i]
    return tempstr

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms('1')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

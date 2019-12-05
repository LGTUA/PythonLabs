import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    outputArray = []
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui',self)

        inputArray = read_file('ex6.txt')
        self.pushButton.clicked.connect(self.loadIn)
        self.pushButton_2.clicked.connect(self.solve)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.saveOut)


    def loadIn(self):
        self.label_3.setText("")
        self.textBrowser.setText("")
        inputArray = read_file('ex6.txt')
        self.textBrowser.setText("Исходные данные")
        self.textBrowser.append(open('ex6.txt').read())

    def solve(self):
        if self.textBrowser.toPlainText() == "":
            self.label_3.setText("Загрузите исходные данные из таблицы")
            return
        else:
            self.label_3.setText("")
        inputArray = read_file('ex6.txt')
        self.outputArray = []
        max = inputArray[0][0]
        maxi = 0
        maxj = 0
        for i in range(6):
            for j in range (5):
                if inputArray[i][j] > max:
                    max = inputArray[i][j]
                    maxi = i
                    maxj = j
        sum = 0
        sub_array = []
        for i in range(6):
            for j in range (5):
                if (i == maxi) and (j == maxj):
                    break
                sum += inputArray[i][j]
            if (i == maxi) and (j == maxj):
                break
        for i in range(6):
            sub_array =[]
            for j in range (5):
                if inputArray[i][j] == 0:
                    sub_array.append(sum)
                else:
                    sub_array.append(inputArray[i][j])
            self.outputArray.append(sub_array)
        self.textBrowser.append("\n\nПолученные данные")
        for row in self.outputArray:
            subString = ""
            for col in row:
                subString += str(col) + " "
            self.textBrowser.append(subString)
        return


    def clear(self):
        self.label_3.setText("")
        self.textBrowser.setText("")

    def saveOut(self):
        if self.outputArray:
            write_file('out.txt', self.outputArray)
            self.label_3.setText("Файл успешно загружен")
        else:
            self.label_3.setText("Сначала обработайте данные")


def read_file(filename):
    in_file = open(filename, 'r')
    array = []
    for line in in_file:
        sub_array = []
        str_nums = line.split(' ')
        for sn in str_nums:
            sub_array.append(int(sn))
        array.append(sub_array)
    return array

def write_file(filename, array):
    out_file = open('out.txt','w')
    for row in array:
        for num in row:
            out_file.write(str(num) + " ")
        out_file.write('\n')


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui',self)

        textFile = open('ex5.txt', 'r')
        text = textFile.read()
        self.lineEdit.setText(text)

        self.pushButton.clicked.connect(self.solve)
        self.pushButton_2.clicked.connect(self.clear)

    def solve(self):
        inStr = self.lineEdit.text()
        outStr = ""
        for char in inStr:
            addChar = True
            for jchar in outStr:
                if char == jchar:
                    addChar = False
                    break
            if addChar:
                outStr += char + "\n"
        self.textEdit.setText(outStr)
        self.label_5.setText(str(len(outStr)))

    def clear(self):
        self.textEdit.setText("")


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
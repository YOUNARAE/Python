import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("main03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        arr45 = [
            1,2,3,4,5,      6,7,8,9,10,
            11,12,13,14,15, 16,17,18,19,20,
            21,22,23,24,25, 26,27,28,29,30,
            31,32,33,34,35, 36,37,38,39,40,
            41,42,43,44,45
        ]
        
        for i in range(1000):
            rnd = int(random()*45)
            a = arr45[0]
            b = arr45[rnd]
            arr45[0]=b
            arr45[rnd]=a
            
        self.le1.setText(str(arr45[0]))
        self.le2.setText(str(arr45[1]))
        self.le3.setText(str(arr45[2]))
        self.le4.setText(str(arr45[3]))
        self.le5.setText(str(arr45[4]))
        self.le6.setText(str(arr45[5]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
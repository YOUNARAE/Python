import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

from_class = uic.loadUiType("main04.ui")[0]

class MyWindow(QMainWindow, from_class):
    
    def __init__(self):
        super().__init__();
        self.setupUI(self);
        
        self.pb.clicked.connect(self.myclick)
    
    def myclick(self):
        mine = self.leMine.text();
        com=""
        result=""

        rnd = random.random()
        
        if rnd >0.5 :
            com = "홀"
        else:
            com = "짝" 
            
        if mine == com  :
            result = "이김"
        else:
            result = "짐" 
        
        self.leCom.setText();
        self.leResult.setText();
        

if __name__== "__main__":
    app = QApplication(sys.argv)
    MyWindow = MyWindow()
    MyWindow.show()
    app.exec_()
            

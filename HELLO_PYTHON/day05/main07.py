import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("main07.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myclick)

    
    def myclick(self):
        mine = self.leMine.text()
        com = ""
        result =""

        rnd = random.random()

        if rnd >0.66 :
            com = "가위"
        elif rnd >0.33 :
            com = "바위"
        else:
            com = "보" 
            
        if com == "가위" and mine == "가위" :   result ="비김"
        if com == "가위" and mine == "바위" :   result ="이김"
        if com == "가위" and mine == "보" :   result ="짐"
        
        if com == "바위" and mine == "가위" :   result ="짐"
        if com == "바위" and mine == "바위" :   result ="비김"
        if com == "바위" and mine == "보" :   result ="이김"
        
        if com == "보" and mine == "가위" :   result ="이김"
        if com == "보" and mine == "바위" :   result ="짐"
        if com == "보" and mine == "보" :   result ="비김"
        
        self.leCom.setText(com)
        self.leResult.setText(result)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        















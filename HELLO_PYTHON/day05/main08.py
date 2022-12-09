import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.myclick)
    
    def drawStar(self,cnt):
        ret = "";
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret
         
    def myclick(self):
        f = self.le_f.text()
        l = self.le_l.text()
        ff = int(f)
        ll = int(l)
        txt = "";
        
        for i in range(ff,ll+1):
            txt += self.drawStar(i)
            
        self.pte.setPlainText(txt)
       
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        


















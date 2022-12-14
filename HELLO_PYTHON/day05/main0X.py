import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("main0X.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__() #생성자
        self.com = "123"
        self.setupUi(self)
        self.setCom()
        self.pb.clicked.connect(self.myclick)
    
    def setCom(self):
        arr = [1,2,3,4,5,6,7,8,9]
        
        for i in range(1000):
            rnd = int(random.random()*9) #8.99까지 나오는 것을 int로 잘라준다
            a = arr[0]
            b = arr[rnd]
            arr[0] = b
            arr[rnd] = a
        
        self.com = "{}{}{}".format(arr[0],arr[1],arr[2])
        #com = str(arr[0]+""+arr[1]+""+arr[2])
        print("self.com",self.com)
        
        
    def myclick(self):
        #print("myclick") 출력해보기
        mine = self.le.text() #글자 가져올 땐 text()
        
        s = self.getStrike(self.com,mine) #여기엔 없으니까 com을 전역변수로 만들어준다.
        b = self.getBall(self.com,mine) 
        #클래스 내에 멤버변수에는 구냥 self를 붙인디
        
        str_old = self.te.toPlainText()
        str_new = "{} {}S{}B\n".format(mine,s,b)

        self.te.setText(str_old+str_new)
        self.le.setText("")
        
        print("s",s)
        print("b",b)
        
        if s == 3 :
            QMessageBox.question(None, "야구게임", self.com+"를 맞췄습니다!", QMessageBox.Yes, QMessageBox.NoButton)

    
    def getBall(self,com,mine):
        ret = 0
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]

        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]

        if c1 == m2 or c1 == m3:   ret += 1
        if c2 == m1 or c2 == m3:   ret += 1
        if c3 == m1 or c3 == m2:   ret += 1
        
        return ret
    
    def getStrike(self,com,mine):
        ret = 0
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]

        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]

        if c1 == m1: ret += 1
        if c2 == m2: ret += 1
        if c3 == m3: ret += 1
        
        return ret
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    
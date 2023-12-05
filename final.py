import random
import sys

from PySide6.QtCore import QSize, Qt, QVariantAnimation, QObject, QTimer, QPoint
from PySide6.QtGui import QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel


class FinalWind(QMainWindow):
    global spr
    global s
    spr = []
    vx = 1
    vy = 1
    wdt = 0
    hgt = 0
    x=1
    y=1
    def __init__(self, parent= None):
        super().__init__()
        (self.wdt, self.hgt) = app.screens()[0].size().toTuple()
        stsh="background-color: black"
        self.setStyleSheet(stsh)
        n=2
        self.k=0
        pix=QPixmap('screenshot.png')
        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(self.screenup)
        self.tmr.start(100)


        for i in range (n):
            for j in range(n):
                self.k+=1
                pix1=pix.copy(i*(self.wdt/n),j*(self.hgt/n),self.wdt/n,self.hgt/n)
                lbl=QLabel(self)
                lbl.setObjectName("lbl"+str(i)+"w"+str(j))
                lbl.setGeometry(i*(self.wdt/n),j*(self.hgt/n),self.wdt/n,self.hgt/n)
                lbl.setPixmap(pix1)
                spr.append(lbl)

    def screenup(self):
        for s in spr:
            self.x+=self.vx
            self.y+=self.vy
            if self.x>=self.wdt or self.x<=0:
                self.vx*=-1
            if self.y>=self.hgt or self.y<=0:
                self.vy*=-1
            #print(x,y)
            s.setGeometry(self.x,self.y,50,50)

                #     for i in range (n):
    #         for j in range(n):
    #             self.move("lbl"+str(i)+"w"+str(j), wdt/n, hgt/n )
    #
    # def move(self, oName, oWdt, oHgt):
    #     obj1 = self.findChild(QLabel,oName)
    #
    #     obj1.setGeometry(random.randint(600,1200),random.randint(300,600),oWdt/4,oHgt/4)




app = QApplication(sys.argv)
window = FinalWind()
window.showFullScreen()
app.exec()
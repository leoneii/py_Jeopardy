import random
import sys

from PySide6.QtCore import QSize, Qt, QVariantAnimation, QObject, QTimer, QPoint
from PySide6.QtGui import QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel


class FinalWind(QMainWindow):

    def __init__(self, parent= None):
        super().__init__()
        (wdt, hgt) = app.screens()[0].size().toTuple()
        stsh="background-color: black"
        self.setStyleSheet(stsh)
        n=2
        spr=[]

        self.k=0
        pix=QPixmap('screenshot.png')

        for i in range (n):
            for j in range(n):
                self.k+=1
                pix1=pix.copy(i*(wdt/n),j*(hgt/n),wdt/n,hgt/n)
                lbl=QLabel(self)
                lbl.setObjectName("lbl"+str(i)+"w"+str(j))
                lbl.setGeometry(i*(wdt/n),j*(hgt/n),wdt/n,hgt/n)
                lbl.setPixmap(pix1)
                spr.append(lbl)
        vx=1
        for i in range(1000):
            j=0
            for s in spr:
                x=spr[j].pos().x()
                y=spr[j].pos().y()

                x+=vx
                if x>=wdt or x<=0:
                    vx*=-1
                # y+=1

                s.pos=QPoint(1,1)
                #spr[j].move(x,y)
                j=j+1


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
import random
import sys
import logging
from PySide6.QtCore import QSize, Qt, QVariantAnimation, QObject, QTimer, QPoint
from PySide6.QtGui import QPainter, QPen, QPixmap, QColor
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QGraphicsDropShadowEffect


class FinalWind(QMainWindow):
    global spr,vx,vy
    global s,n,tick

    n = 15
    spr = []
    vx =[]
    vy=[]
    wdt = 0
    hgt = 0
    x=1
    y=1


    def __init__(self, parent= None):


        super().__init__()
        sqlDB = QSqlDatabase.addDatabase('QSQLITE')
        sqlDB.setDatabaseName("./jep.sqlite")
        sqlDB.open()

        query = QSqlQuery()
        if not query.exec(
                """
                    SELECT max(sum), count(Name) FROM Teams Where sum = (SELECT max(sum) FROM teams) ;
                """
        ):
            logging.error("Failed to query database")
        query.first()
        maxsum=query.value(0)
        wincount= query.value(1)
        if not query.exec("SELECT Name FROM Teams Where sum = "+str(maxsum)+";"):
            logging.error("Failed to query database")
        query.first()

        textName = ""
        if wincount==1:
            textPob="Побеждает"
            textName=query.value(0)+"\n"
        else:
            textPob = "Побеждают"
            k=0
            textName+="\n"
            while k<wincount:
                k+=1
                ktext=query.value(0)
                textName=textName+ktext+"\n\n"
                query.next()


        print(textName)
        (self.wdt, self.hgt) = app.screens()[0].size().toTuple()

        tlab = QLabel(self)
        tlab.setText(textPob)
        tlab.setGeometry(self.wdt/2-275, self.hgt*.1, 560, 100)
        tlab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        shadow = QGraphicsDropShadowEffect(
            self, blurRadius=20, offset=0, color=QColor(255, 255, 80, 255)
        )
        # tlab.setGraphicsEffect(shadow)
        tlab.setStyleSheet("background-color: rgba(224, 255, 255, 0); color: rgba(200,60,0,255); font: bold 94px")

        nameLab=QLabel(self)
        nameLab.setText(textName)
        nameLab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nameLab.setWordWrap(True)
        nameLab.setGeometry(self.wdt / 2 -self.wdt / 3 , self.hgt *.1+100, 2*self.wdt / 3, self.hgt*.9-210)
        nameLab.setStyleSheet("background-color: rgba(224, 255, 255, 0); color: rgba(200,60,0,255); font: bold 115px")



        stsh="background-color: black"
        self.setStyleSheet(stsh)
        self.tick = 0
        self.k=0
        pix=QPixmap('screenshot.png')
        self.tmr = QTimer()
        self.tmr.timeout.connect(self.screenup)
        self.tmr.start()



        for i in range (n):
            for j in range(n):
                self.k+=1
                pix1=pix.copy(i*(self.wdt/n),j*(self.hgt/n),self.wdt/n,self.hgt/n)
                lbl=QLabel(self)
                lbl.setObjectName(str(self.k))
                lbl.setGeometry(i*(self.wdt/n),j*(self.hgt/n),self.wdt/n,self.hgt/n)
                lbl.setPixmap(pix1)
                spr.append(lbl)
                tmp=random.randint(-7,7)
                vx.append(tmp)
                tmp = random.randint(-3, 3)
                vy.append(tmp)



    def screenup(self):
        self.tick+=1
        self.k=0
        self.g=0.4
        if self.tick>25000 and self.tick<25048:
            for s in spr:
                tmw = s.size().width()
                tmh = s.size().height()
                self.x=int(s.pos().x())
                self.y=int(s.pos().y())
                dx=random.randint(-1,1)
                self.x+=dx
                dy = random.randint(-1, 1)
                self.y += dy
                s.setGeometry(self.x, self.y, tmw , tmh )
        if self.tick>=25048 and self.tick<=25052:
            for s in spr:
                tmw = s.size().width()
                tmh = s.size().height()
                self.x = int(s.pos().x())
                self.y = int(s.pos().y())
                s.setGeometry(self.x+tmw*.1,self.y,tmw*.8,tmh*.8)

        self.k=0
        if self.tick>25052:
            for s in spr:
                tmw = s.size().width()
                tmh = s.size().height()
                self.x=int(s.pos().x())
                self.y=int(s.pos().y())
                self.x+=vx[self.k]
                vy[self.k]+=self.g
                self.y+=vy[self.k]
                if self.x>self.wdt or self.x<0:
                    vx[self.k]*=-0.9
                    if tmw>10:
                        tmw *= 0.6
                        tmh *= 0.6
                if self.y>self.hgt or self.y<0:
                    vy[self.k]*=-0.8
                    vx[self.k]*=0.9
                    if tmw > 10:
                        tmw *= 0.6
                        tmh *= 0.6
                if tmw<=10 and self.y>self.hgt-tmh*2:
                    if self.x<=self.wdt/2:
                        self.x=50+random.randint(-10,10)
                        self.dvy=-24*random.random()-5
                        vy[self.k]=self.dvy
                        self.dvx=random.random()*6-2
                        vx[self.k]=self.dvx
                    else:
                        self.x=self.wdt-50+20*random.random()-10
                        self.dvy = -24 * random.random() - 5
                        vy[self.k] = self.dvy
                        self.dvx = random.random() * 6 - 3
                        vx[self.k] = self.dvx

                s.setGeometry(self.x,self.y,tmw,tmh)
                shadow = QGraphicsDropShadowEffect(self, blurRadius=20, offset=0, color=QColor(155*random.random(), 100*random.random()+155, 100*random.random()+155, 255))
                s.setGraphicsEffect(shadow)


                self.k += 1


app = QApplication(sys.argv)
window = FinalWind()
window.showFullScreen()
app.exec()
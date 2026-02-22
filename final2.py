import sys
import random
from random import randint, choice
import logging

from PySide6.QtCore import QSize, QMetaObject, Qt, QVariantAnimation, QObject, QTimer, QPoint, QUrl, QEvent
from PySide6.QtGui import QPainter, QPen, QPixmap, QColor, QLinearGradient
#from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtSql import  QSqlQuery
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QGraphicsDropShadowEffect
import simpleaudio as simple_audio
import time


class FinalWind(QWidget):
    global spr, vx, vy, isspr, spd
    global s, n, tick, tend, colors
    global spix
    # spix=QPixmap()
    tend = 0
    n = 15
    spr = []
    vx = []
    vy = []
    isspr = []
    spd=[]
    wdt = 0
    hgt = 0
    x = 1
    y = 1
    colors = ["rgba(255, 0, 0, 10)", "rgba(255, 255, 0, 10)", "rgba(0, 255, 0, 10)", "rgba(0, 255, 255, 10)",
              "rgba(255, 200, 255, 10)"]

    def __init__(self, app=QApplication, parent=None):

        super().__init__()

        self.finalSound = simple_audio.WaveObject.from_wave_file("./resourses/sound/finalsound.wav")
        self.coda = self.finalSound.play()

        # начало чуда
        def scrupd():
            sth = "background-color: rgba(0,0,80,255); color: #ddFFaa;"
            self.setStyleSheet(sth)

        self.tmr4 = QTimer()  # 4
        self.tmr4.timeout.connect(scrupd)
        self.tmr4.start(40)
        self.tmr4.stop()
        # конец чуда

        (self.wdt, self.hgt) = app.screens()[0].size().toTuple()
        stsh = "background-color: black"
        stshf = 'border-image: url("resourses/logo/back.png");'
        self.setStyleSheet(stsh)
        fonl = QLabel(self)
        fonl.setGeometry(0, 0, self.wdt, self.hgt)
        fonl.setStyleSheet(stshf)

        query = QSqlQuery()
        if not query.exec(
            "SELECT sum ,  count(Name) FROM Teams Where sum = (SELECT max(sum) FROM teams) ;"
        ):
            logging.error("Failed to query database")
        query.first()
        maxsum = query.value(0)
        wincount = query.value(1)
        if not query.exec("SELECT Name FROM Teams Where sum = '" + str(maxsum) + "';"):
            logging.error("Failed to query database")
        query.first()
        self.fs = 120
        textName = ""
        if wincount == 1:
            textPob = "Побеждает"
            textName = '"'+query.value(0)+'"'
        else:
            textPob = "Побеждают"
            k = 0
            textName+='"'
            while k < wincount:
                k += 1
                self.fs -= 7
                ktext = query.value(0)
                textName = textName + '"' + ktext + '"\n'
                query.next()

        self.tlab = QLabel(self)
        self.tlab.setText(textPob)
        #geometry текста "побдила"
        self.tlab.setGeometry(self.wdt / 2 - 275, self.hgt * .15, 560, 100)
        self.tlab.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        # tlab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shadow = QGraphicsDropShadowEffect(
            self, blurRadius=0, offset=0, color=QColor(255, 255, 80, 255)
        )
        # tlab.setGraphicsEffect(shadow)

        self.shadow1 = QGraphicsDropShadowEffect(
            self, blurRadius=15, offset=0, color=QColor(25, 45, 60, 255)       )
        self.tlab.setGraphicsEffect(self.shadow1)
        self.tlab.setStyleSheet(
            "border: none; background-color: rgba(224, 255, 255, 0); color: rgba(250,200,90,255); font: bold 90px")
        self.nameLab = QLabel(self)
        self.nameLab.setText(textName)
        # self.nameLab.setAlignment(
        #      Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        # )
        self.nameLab.setAlignment(
             Qt.AlignmentFlag.AlignHCenter
        )
        self.nameLab.setWordWrap(True)
        self.nameLab.setGeometry(self.wdt / 2 -self.wdt / 3 , self.hgt *.1+100, 2*self.wdt / 3, self.hgt*.9-100)
        # self.nameLab.setGeometry(0, 0, 3, 3)
        # self.nameLab.setStyleSheet("background-color: rgba(224, 255, 255, 0); color: rgba(0,0,0,255); font: bold "+str(self.fs)+"px")
        self.nameLab.setGraphicsEffect(self.shadow)
        self.nameLab.setVisible(False)

        self.tick = 0
        self.k = 0
        pix = QPixmap('screenshot.png')
        self.tmr = QTimer()
        self.tmr.timeout.connect(self.screenup)
        self.tmr.start()

        self.tmrsh = QTimer()
        self.tmrsh.timeout.connect(self.shadblink)

        for i in range(n):
            for j in range(n):
                self.k += 1
                pix1 = pix.copy(i * (self.wdt / n), j * (self.hgt / n), self.wdt / n, self.hgt / n)
                lbl = QLabel(self)
                lbl.setObjectName(str(self.k))
                lbl.setGeometry(i * (self.wdt / n), j * (self.hgt / n), self.wdt / n, self.hgt / n)
                lbl.setPixmap(pix1)
                spr.append(lbl)
                tmp = random.randint(-7, 7)
                vx.append(tmp)
                tmp = random.randint(-3, 3)
                vy.append(tmp)
                isspr.append(0)
                spd.append(0.0)
        self.nb = 16
        self.br = 1
        # очищаем таблицу
        quec = QSqlQuery()
        if not quec.exec("UPDATE teams set sum=0;"):
            logging.error("Ошибка очистки teams")
        if not quec.exec("DELETE from steps;"):
            logging.error("Ошибка очистки steps")

    def shadblink(self):
        self.nb += self.br
        if self.nb > 50 or self.nb < 5:
            self.br *= -1

        self.nameLab.setStyleSheet(
            "background-color: rgba(224, 255, 255, 0); color: rgba(" + str(205 - 4 * self.nb) + "," + str(
                26 - self.nb / 2) + "," + str(2 * self.nb / 2) + ",255); font: bold " + str(self.fs) + "px")
        self.shadow.setBlurRadius(self.nb)

    def screenup(self):
        self.tick += 1
        self.k = 0
        self.g = 0.7
        if self.tick > 25000 and self.tick < 25048:
            for s in spr:
                tmw = s.size().width()
                tmh = s.size().height()
                self.x = int(s.pos().x())
                self.y = int(s.pos().y())
                dx = random.randint(-1, 1)
                self.x += dx
                dy = random.randint(-1, 1)
                self.y += dy
                s.setGeometry(self.x, self.y, tmw, tmh)
        if self.tick >= 25048 and self.tick <= 25052:
            for s in spr:
                tmw = s.size().width()
                tmh = s.size().height()
                self.x = int(s.pos().x())
                self.y = int(s.pos().y())
                s.setGeometry(self.x + tmw * .1, self.y, tmw * .8, tmh * .8)
    
    
        if self.tick >= 25120 and self.tick <= 25129:
                   #Искры перед сменой текста
                   
                    
                    for s in spr:
                       
                        tmw = s.size().width()
                        tmh = s.size().height()
                        self.x = int(s.pos().x())
                        self.y = int(s.pos().y())
                        dx = random.randint(-25, 25)
                        self.x += dx
                        dy = random.randint(-1, 1)
                        self.y += dy
                        
                        self.x = self.wdt/2 + random.randint(-380, 380)
                        self.y=200+random.randint(-80,80)
                        s.setGeometry(self.x, self.y, tmw, tmh)
                            
    
       
        if self.tick == 25130:
            self.tmrsh.start(40)
            self.nameLab.setGeometry(self.wdt / 2 - self.wdt / 3, self.hgt * .1 , 2 * self.wdt / 3, self.hgt * .9 - 100) 
            self.nameLab.setVisible(True)
            self.tlab.setVisible(False)
            
            #Искры от смены текста
            for s in spr:
                tmw = s.size().width()
                tmh = s.size().height()
                self.x = int(s.pos().x())
                self.y = int(s.pos().y())
                dx = random.randint(-25, 25)
                self.x += dx
                dy = random.randint(-1, 1)
                self.y += dy
                
                self.x = self.wdt/2 + random.randint(-350, 350)
                self.y=200+random.randint(-100,100)
                s.setGeometry(self.x, self.y, tmw, tmh)
                
        if self.tick >= 25131 and self.tick <= 25136:
            #Искры после смены текста
            for s in spr:
                tmw = s.size().width()
                tmh = s.size().height()
                self.x = int(s.pos().x())
                self.y = int(s.pos().y())
                dx = random.randint(-25, 25)
                self.x += dx
                dy = random.randint(-1, 1)
                self.y += dy
                
                self.x = self.wdt/2 + random.randint(-500, 500)
                self.y=200+random.randint(-100,100)
                s.setGeometry(self.x, self.y, tmw, tmh)
                    
        
            

        self.k = 0
        if self.tick > 25052:
            for s in spr:
                tmw = s.size().width()
                tmh = s.size().height()
                self.x = int(s.pos().x())
                self.y = int(s.pos().y())
                self.x += vx[self.k]
                vy[self.k] += self.g
                self.y += vy[self.k]
                if self.x > self.wdt or self.x < 0:
                    vx[self.k] *= -0.9

                if self.y > self.hgt:
                    isspr[self.k] = 1
                    tmcol = choice(colors)
                    spd[self.k]= random.randint(15, 20)
                    s.setPixmap(QPixmap("./resourses/icon/sprite.png").scaled(QSize(spd[self.k], spd[self.k]), Qt.KeepAspectRatio))
                    s.setStyleSheet("background-color: " + tmcol + "; border-radius: " + str(spd[self.k] / 2) + ";")

                    if self.x <= self.wdt / 2:
                        self.x = 50 + random.randint(-10, 10)
                        self.dvy = -25 * random.random() - 15
                        vy[self.k] = self.dvy
                        self.dvx = random.random() * 6 - 2
                        vx[self.k] = self.dvx
                    else:
                        self.x = self.wdt - 50 + 20 * random.random() - 10
                        self.dvy = -25* random.random() - 15
                        vy[self.k] = self.dvy
                        self.dvx = random.random() * 6 - 3
                        vx[self.k] = self.dvx



                s.setGeometry(self.x, self.y, tmw, tmh)

                if vy[self.k]<0 and isspr[self.k] == 1:
                    spd[self.k]*=1.03
                    s.resize(spd[self.k],spd[self.k])
                    s.setPixmap(
                        QPixmap("./resourses/icon/sprite.png").scaled(QSize(spd[self.k], spd[self.k]), Qt.KeepAspectRatio))
                    # if self.k==0:
                    #     print(s.size().width())

                if vy[self.k] > random.randint(4,50) and isspr[self.k] == 1:
                    spd[self.k] *= .4
                    s.move(s.pos().x()+spd[self.k]/2,s.pos().y()+spd[self.k]/2)
                    # spd[self.k]*=.4
                    s.resize(spd[self.k],spd[self.k])
                    s.setPixmap(
                        QPixmap("./resourses/icon/sprite.png").scaled(QSize(spd[self.k], spd[self.k]), Qt.KeepAspectRatio))


                    if s.size().width()<5:
                        self.y = self.hgt + random.randint(10, 100)
                        s.move(self.x,self.y)
                    if s.size().width()<10 :
                        vy[self.k]=(vy[self.k]*random.random())
                        vx[self.k] = (vx[self.k] * random.random())
                        s.resize(s.size().width() * .6, s.size().height() * .6)
                self.k += 1

    def theEnd(self):
        h = self.hgt
        w = self.wdt
        while h > 5:
            time.sleep(0.0025)
            h -= 10
            self.setGeometry(0, int(self.hgt / 2 - h / 2), self.wdt, h)
        while w > 5:
            w -= 20
            time.sleep(0.0025)
            self.setGeometry(self.wdt / 2 - w / 2, self.hgt / 2, w, 3)
        self.close()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:
            self.theEnd()
            # self.close()

# if __name__ == "__main__":
#     global gwidth,gheight,kfont
#     apt = QApplication([])
#     (gwidth, gheight) = apt.screens()[0].size().toTuple()
#     kfont=gwidth/1920
#     # pyside6 splash screen

#    # from categ import getCatname
#     wnt = FinalWind(apt)
#     wnt.showFullScreen()

#     sys.exit(apt.exec())
#     sqlDB.close()
#     sqlDB.removeDatabase('QSQLITE')
#     sqlDB.removeDatabase('jep.sqlite')
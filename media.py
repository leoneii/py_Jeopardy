import sys
import os
import time
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QMovie, QIcon, QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime

from PySide6.QtCore import (QTimer, QEventLoop, QRect, Qt, QEvent, QPoint)
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient)

blc = 120
shag = 1
smx = 3
gx = 200
wdl = 1



class MoviePlayer(QWidget):

    kolend=0
    def __init__(self,fgif,fmp3,apt,butText = "-"):
        super().__init__()
        global appt 
        appt=apt
        geometry = apt.primaryScreen().availableGeometry()
        self.setGeometry(geometry)
        wdh = self.size().width()
        hgt = self.size().height()





        self.movie_screen = QLabel(self)
        self.movie = QMovie('./media/'+fgif)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(70)
        self.movie.setScaledSize(QSize(wdh, hgt))
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

        #КНОПКА ПРОДОЛЖЕНИЯ ИГРЫ
        self.contin = QPushButton(self)
        tmh = int(hgt / 15 - 5)
        fw = int((wdh / 3) / 12)
        self.contin.setGeometry(wdh * 3 / 4 - 60, hgt - hgt / 15 - 5, (wdh - 20) / 4, tmh)
        self.contin.setText(butText)
        self.contin.setStyleSheet("QPushButton { background-color: rgba(0,0,180,50) ; font: bold " + str(fw) + "px; border: 1px solid rgba(200,200,255,180);border-top-right-radius: " + str(tmh * 2) + "px " + str(tmh) + "px; border-bottom-left-radius: " + str(tmh * 2) + "px " + str(tmh) + "px} QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,180) }")
        self.contin.clicked.connect(self.theEnd)

        #Кнопка paus/play
        self.pausplay=QPushButton(self)
        self.pausplay.setGeometry(wdh / 2 - 120, hgt - hgt / 15 - 5, (wdh - 20) / 8, tmh)
        #ticon=QIcon('./img/icon/pause.png')
        #self.pausplay.setIcon(ticon)
        self.pausplay.setText(" ")
        self.pausplay.setStyleSheet("QPushButton { background-color: rgba(0,0,180,50) ; fontsize: 0; border: 1px solid rgba(200,200,255,180);border-radius: " + str(tmh/2-3) + "px } QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,180) }")
        self.pausplay.clicked.connect(self.paPl)

        pxmp=QPixmap('./img/icon/wpause.png')
        bico=QIcon(pxmp)
        self.pausplay.setIcon(bico)
        self.pausplay.setIconSize(self.pausplay.size())



        self.player = QMediaPlayer()
        self.p0 = self.player.position()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile('./media/'+fmp3))
        self.player.play()

        def scrupd():
        # Определяем окончание mp3 трека
            p1 = self.player.position()
            if p1 != self.p0:
                self.kolend=0
                self.p0 = p1
            else:
                if self.pausplay.text()!=".":
                    self.kolend+=1
                if self.kolend==20:
                    self.theEnd()
        # и выходим из модуля

        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(120)


    def paPl(self):
        if self.pausplay.text()==" ":
            self.pausplay.setText(".")
            self.player.pause()

            pxmp=QPixmap('./img/icon/wplay.png')
            bico=QIcon(pxmp)
            self.pausplay.setIcon(bico)
            self.pausplay.setIconSize(self.pausplay.size())

        else:
            self.pausplay.setText(" ")
            self.player.play()

            pxmp=QPixmap('./img/icon/wpause.png')
            bico=QIcon(pxmp)
            self.pausplay.setIcon(bico)
            self.pausplay.setIconSize(self.pausplay.size())


    def theEnd(self):
        (self.wdt, self.hgt) = appt.screens()[0].size().toTuple()
        h = self.hgt
        w = self.wdt
        while h > 5:
            time.sleep(0.0025)
            h -= 25
            self.setGeometry(0, int(self.hgt / 2 - h / 2), self.wdt, h)
        while w > 5:
            w -= 35
            time.sleep(0.0025)
            self.setGeometry(self.wdt / 2 - w / 2, self.hgt / 2, w, 3)
        self.player.stop()    
        self.close()

    def paintEvent(self, event):
        if os.path.exists("disanim"):
            self.sth = "background-color: rgba(0,40,200,200); color: #ddFFaa;"
            self.setStyleSheet(self.sth)
        else:
            global smx
            global gx
            global blc, shag
            blc += shag
            if blc >= 254 or blc <= 90:
                 shag *= -1
            self.sth = "background-color: rgba(0,0," + str(blc) + ",75); color: #ddFFaa;"
            self.setStyleSheet(self.sth)
            painter = QPainter(self)
            x = 0
            y = 0
            wd = self.size().width()
            hd = self.size().height()
            gx += smx
            if gx > wd * 1.5 or gx < 150:
                smx *= -1
            gradient = QLinearGradient(QPoint(x, y), QPoint(gx, y + 300 + wd * 300 / gx))
            gradient.setColorAt(0.0, QColor(0, 0, 80, 180))
            gradient.setColorAt(0.3, QColor(0, 120, 255, 225))
            gradient.setColorAt(1.0, QColor(0, 80, 255, 80))
            painter.setBrush(gradient)
            pen = QPen()
            pen.setWidth(1)
            pen.setColor(QColor(0, 0, 50, 10))
            painter.setPen(pen)
            painter.drawRect(x, y, wd, hd)

if __name__ == "__main__":
    global gwidth, gheight, kfont
    apt = QApplication([])
    (gwidth, gheight) = apt.screens()[0].size().toTuple()
    kfont = gwidth / 1920
    mediapl = MoviePlayer('GK.gif','short.mp3',apt)
    mediapl.showFullScreen()
    sys.exit(apt.exec())     
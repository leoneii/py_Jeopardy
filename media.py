import sys
import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QMovie
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime

from PySide6.QtCore import (QTimer, QEventLoop, QRect, Qt, QEvent, QPoint)
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient)

blc = 120
shag = 2
smx = 5
gx = 200
wdl = 1


class MoviePlayer(QWidget):
    kolend=0
    if os.path.exists("disanim"):
        pass
    else:
        def paintEvent(self, event):
            global smx
            global gx

            painter = QPainter(self)
            #  painter.begin(self)
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

            def scrupd():
                self.p1 = self.player.position()
                if self.p1 != self.p0:
                    self.kolend=0
                    self.p0 = self.p1
                    print(self.p0)
                else:
                    self.kolend+=1
                    print("end",self.kolend)
                    if self.kolend==50:
                        self.close()


                if os.path.exists("disanim"):
                    self.sth = "background-color: rgba(0,40,200,200); color: #ddFFaa;"
                else:
                    global blc, shag
                    blc += shag
                    if blc >= 254 or blc <= 90:
                        shag *= -1
                    self.sth = "background-color: rgba(0,0," + str(blc) + ",75); color: #ddFFaa;"
                self.setStyleSheet(self.sth)


            self.tmr = QTimer()  # 4
            self.p0 = self.player.position()
            self.tmr.timeout.connect(scrupd)
            self.tmr.start(40)

    def __init__(self):
        super().__init__()
        geometry = apt.primaryScreen().availableGeometry()


        self.setGeometry(geometry)
        wdh = self.size().width()
        hgt = self.size().height()

        self.movie_screen = QLabel(self)
        # self.movie_screen.setStyleSheet("background-color: rgb(0,50,100)")

        self.movie = QMovie('./media/GK.gif')
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie.setScaledSize(QSize(wdh, hgt))
        self.movie_screen.setMovie(self.movie)

        self.movie.start()



        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        # player.positionChanged.connect(self.positionChanged)
        self.player.setSource(QUrl.fromLocalFile('./media//short.mp3'))
        #self.audioOutput.setVolume(50)



        #self.player.positionChanged.connect(position_changed)

        self.player.play()



# app = QApplication([])
# player = MoviePlayer() 
# player.show() 
# app.exec()

if __name__ == "__main__":
    global gwidth, gheight, kfont
    apt = QApplication([])
    (gwidth, gheight) = apt.screens()[0].size().toTuple()
    kfont = gwidth / 1920
    mediapl = MoviePlayer()
    mediapl.showFullScreen()
    #mediapl.setStyleSheet("background-color: rgb(0,30,60)")
    sys.exit(apt.exec())     
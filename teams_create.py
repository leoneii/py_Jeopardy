import sys
# import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, QPoint, QTimer, QEvent
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient, QPixmap)
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QDialog, \
    QVBoxLayout, QButtonGroup, QHBoxLayout
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import simpleaudio as simple_audio

blc = 120
shag = 2
smx = 5
gx = 200
wdl=1


class Winteamcr(QWidget):
   
    


    def paintEvent(self, event):
        global smx,blc,shag
        global gx, wd, hd

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
        # закончили с фоном
   
    def __init__(self, parent=None):
        
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)



        global gwidth, gheight,wdl
        (gwidth, gheight) = apt.screens()[0].size().toTuple()
        super(Winteamcr, self).__init__(parent)
        wd=gwidth
        hd=gheight
        
        #запускаем анимацию фона
        def scrupd():
                self.blc+=self.shag
                if self.blc>=254 or self.blc<=60:
                    self.shag*= -1
                self.sth="background-color: rgba(0,0,255,"+str(self.blc)+"); color: #ddFFaa;"
                self.setStyleSheet(self.sth)
                
        def objupd():    
                   
                if self.wdl<wd/3:
                    self.wdl+=4
                    self.titlabel.setGeometry(wd/2-wd/6,40,self.wdl,80)
                else:
                    self.wdl=wd/3
                    if self.badd<self.wdl/2:
                         self.badd+=5
                         self.butAddTeam.setGeometry(wd/2-wd/6,125,self.badd,40)
                    

               
                    #self.tmrscrobj.stop()


        # таймер фона
        self.blc = 80
        self.shag=1
        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(40)
        # конец блока анимации

        #таймер элементов экрана
        self.tmrscrobj=QTimer()
        self.tmrscrobj.timeout.connect(objupd)
        self.tmrscrobj.start(8)
        #таймер элементов экрана

        self.titlabel=QLabel(self)
        self.titlabel.setText("Регистрация команд")
        self.titlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wdl=20
        fw = int((wd/3) / len(self.titlabel.text()))
        fnts = int(fw * (1.4-0.2*(1-kfont)))
        if fnts>60:
            fnts=60
        self.titlabel.setFont(font)
        stsh = "border:0px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,200,30); font-size: " + str(fnts) + "px"
        self.titlabel.setStyleSheet(stsh)

        self.badd=0
        self.butAddTeam=QPushButton(self)
        self.butAddTeam.setFont(font)
        self.butAddTeam.setText("Добавить команду")
        self.butAddTeam.setGeometry(wd / 2 - wd / 6, 125, self.badd, 40)
        botb = "QPushButton{font-size: " +  str(int(fnts*0.7)) + "px; border-radius: 10px; border: 1px solid rgba(200,200,255,180); background-color: rgba(0,0,200,50)} QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
        self.butAddTeam.setStyleSheet(botb)




if __name__ == "__main__":
    global gwidth,gheight,kfont
    apt = QApplication([])
    (gwidth, gheight) = apt.screens()[0].size().toTuple()
    kfont=gwidth/1920
    wteamcr = Winteamcr()
    wteamcr.showFullScreen()
    sys.exit(apt.exec())
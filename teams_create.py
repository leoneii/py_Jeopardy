import sys
# import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, QPoint, QTimer, QEvent
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient, QPixmap)
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QDialog, \
    QVBoxLayout, QButtonGroup, QHBoxLayout, QSpinBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import simpleaudio as simple_audio

blc = 120
shag = 2
smx = 5
gx = 200
wdl=1
kolteam=2


class Winteamcr(QWidget):
   
    

# Анимация фона экрана
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

        global gwidth, gheight,wdl, kolteam
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
# Эффект раскрытия объектов
        def objupd():

                if self.wdl<wd/3:
                    self.wdl+=10
                    self.titlabel.setGeometry(wd/2-wd/6,40,self.wdl,80)
                else:
                    self.wdl=wd/3
                    if self.badd<self.wdl/2:
                        self.badd+=10
                        self.butAddTeam.setGeometry(wd/2-wd/6,125,self.badd,40)
                    else:
                        self.badd=self.wdl/2
                        if self.spwt<self.wdl/2-5:
                            self.spwt+=10
                            self.spinTeamCount.setGeometry(wd / 2 + 5, 125, self.spwt, 40)
                        else:
                            self.spwt=self.wdl/2-5

                            while self.hdn < hd - 260:
                                self.hdn += 1
                                for i in range(kolteam):
                                    x = 40 + i * (wd - 80) / kolteam
                                    wdnl = (wd - 80) / kolteam - 20
                                    y = 180
                                    self.labi = self.findChild(QLabel,u"labtmname"+str(i))
                                    self.labi.setGeometry(x, y, wdnl, self.hdn)




# таймер фона
        self.blc = 80
        self.shag=1
        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(40)

#таймер элементов экрана
        self.tmrscrobj=QTimer()
        self.tmrscrobj.timeout.connect(objupd)
        self.tmrscrobj.start(20)

# Label заголовка экрана
        self.titlabel=QLabel(self)
        self.titlabel.setText("Регистрация команд")
        self.titlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wdl=20
        fw = int((wd/3) / len(self.titlabel.text()))
        fnts = int(fw * (1.4-0.2*(1-kfont)))
        if fnts>60:
            fnts=60
        self.titlabel.setFont(font)
        stsh = "border:0px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,200,40); font-size: " + str(fnts) + "px"
        self.titlabel.setStyleSheet(stsh)

# кнопка изменения количества команд
        def changeTeamCount():
            if self.butAddTeam.text()=="Изменить количество":
                self.butAddTeam.setText("Подтвердить количество")
                self.spinTeamCount.setEnabled(True)
                spstsh = "QSpinBox{border:3px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,20,130); font-size: " + str(
                    int(fnts * 0.7)) + "px}"
                self.spinTeamCount.setStyleSheet(spstsh)
            else:
                self.butAddTeam.setText("Изменить количество")
                spstsh = "QSpinBox{border:1px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,200,30); font-size: " + str(
                    int(fnts * 0.7)) + "px}"
                self.spinTeamCount.setStyleSheet(spstsh)
                self.spinTeamCount.setEnabled(False)
                kolteam=self.spinTeamCount.value()

        self.badd=0
        self.butAddTeam=QPushButton(self)
        self.butAddTeam.setText("Изменить количество")
        self.butAddTeam.setGeometry(wd / 2 - wd / 6-5, 125, self.badd, 40)
        botb = "QPushButton{font-size: " +  str(int(fnts*0.5)) + "px; border-radius: 10px; border: 1px solid rgba(200,200,255,180); background-color: rgba(0,0,200,50)} QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
        self.butAddTeam.setStyleSheet(botb)
        self.butAddTeam.clicked.connect(changeTeamCount)
# Спинер изменения количества команд
        self.spwt=0
        self.spinTeamCount=QSpinBox(self)
        self.spinTeamCount.setGeometry(wd / 2 +5, 125, self.spwt, 40)
        spstsh = "QSpinBox{border:1px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,200,30); font-size: " + str(int(fnts*0.7)) + "px}"
        self.spinTeamCount.setStyleSheet(spstsh)
        self.spinTeamCount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinTeamCount.setFont(font)
        self.spinTeamCount.setMinimum(2)
        self.spinTeamCount.setMaximum(7)
        self.spinTeamCount.setEnabled(False)
        self.spinTeamCount.show()


# Модуль изменения наименования команд и их логотипов
        def mod_chang_team_name():
            stshteamname = "border:0px solid #99aaff; border-radius: 20px; background-color: rgba(40,60,150,120); font-size: " + str(
                fnts) + "px"
            self.hdn=0
            for i in range(kolteam):
                self.lab_teamName = QLabel(self)
                self.lab_teamName.setObjectName(u"labtmname"+str(i))
                self.lab_teamName.setFont(font)
                self.lab_teamName.setStyleSheet(stshteamname)
                self.lab_teamName.setText("Команда "+str(i+1))
                x=40+i*(wd-80)/kolteam
                wdnl=(wd-80)/kolteam-20
                y=180
                self.lab_teamName.setGeometry(x,y,wdnl,self.hdn)
                self.lab_teamName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mod_chang_team_name()




if __name__ == "__main__":
    global gwidth,gheight,kfont
    apt = QApplication([])
    (gwidth, gheight) = apt.screens()[0].size().toTuple()
    kfont=gwidth/1920
    wteamcr = Winteamcr()
    wteamcr.showFullScreen()
    sys.exit(apt.exec())
import logging
import os
import sys
import re

import simpleaudio as simple_audio
from PySide6.QtCore import (Qt, QRect, QTimer, QSize, QPoint)
from PySide6.QtGui import (QFont, QPixmap, QIcon, QPainter, QLinearGradient, QColor, QPen)
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import (QLabel, QWidget,
                               QFrame, QProgressBar, QPushButton)

phyn=1 # 0-без фото, 1- с фото
testtext=" "
smx=3
gx=200


class winq(QWidget):
    font = QFont()
    font.setFamilies([u"Arial"])
    font.setBold(True)
    alignmentc=Qt.AlignmentFlag.AlignCenter


# рисуем анимацию фона

    def paintEvent(self,event):
        global smx
        global gx
        if os.path.exists("disanim"):
            pass
        else:
            painter = QPainter(self)
    #        painter.begin(self)
            x = 0
            y = 0
            wd=self.size().width()
            hd=self.size().height()
            gx+= smx
            if gx>wd*1.5 or gx<150:
                smx*=-1
            gradient = QLinearGradient(QPoint(x, y), QPoint(gx, y+300+wd*300/gx))
            gradient.setColorAt(0.0, QColor(0, 0, 50, 100))
            gradient.setColorAt(0.3, QColor(0, 100, 255, 180))
            gradient.setColorAt(1.0, QColor(0, 0, 255, 30))
            painter.setBrush(gradient)

            pen = QPen()
            pen.setWidth(1)
            pen.setColor(QColor(0, 0, 50, 10))
            painter.setPen(pen)
            painter.drawRect(x, y, wd, hd)


# закончили с фоном
    def __init__(self,apt,ynph_1,txt,ynpha_l, txta_l,ttq_l,txtp_l,cpd_l,ynpht_1,cost_l):
        #txtp текст подсказки
        #cpd цена подсказки
        global kfont,fkfont
        (gwidth, gheight) = apt.screens()[0].size().toTuple()
        kfont = gwidth / 1920
        fkfont = (1.4 - 0.2 * (1 - kfont)) / 1.4

        self.muteSound = simple_audio.WaveObject.from_wave_file( "./sound/untitled.wav" )
        self.timerSound = simple_audio.WaveObject.from_wave_file( "./sound/timer-tick.wav" )
        self.tickEndSound=simple_audio.WaveObject.from_wave_file( "./sound/tick_end.wav" )
        self.tiker = self.muteSound.play()
        self.tiker.stop()
        
        global txtp, cpd, cost
        global txta, wdt, hgt
        global ynpha, ynph, ynpht
        global ttq #время таймера
        ttq=ttq_l*10
        txta=txta_l
        ynpht=ynpht_1
        ynpha=ynpha_l
        ynph=ynph_1
        txtp=txtp_l
        cpd=cpd_l
        cost = cost_l
        super().__init__()
        geometry = apt.primaryScreen().availableGeometry()
        self.setGeometry(geometry)
        wdt=self.size().width()
        hgt=self.size().height()
        # self.setStyleSheet("""
        # background-color: rgba(0,0,60,10);
        # color: #ddFFaa;
        # font-family: Arial;
        # """)
        self.photo=QLabel(self)
        self.photo.setAlignment(self.alignmentc)
        self.photo.setGeometry(QRect(100, 20, wdt-200, hgt*2/3-120))
        self.photo.setStyleSheet("background-color: rgba(0,0,80,5)")
        #Фото
        if len(ynph) > 0:
            pixmap=QPixmap("./img/"+ynph)
            pixmap = pixmap.scaled(wdt-200, hgt*2/3-120, Qt.KeepAspectRatio)
            self.photo.setPixmap(pixmap)
#Конец фото

#текст вопроса
        self.textv = QLabel(self)
        self.textv.setObjectName(u"txtvopr")
        self.textv.setAlignment(self.alignmentc)
        if len(ynph) > 0:
            self.textv.setGeometry(QRect(130, hgt*2/3-100, wdt-260, hgt/3-20))
        else:
            self.textv.setGeometry(QRect(130, 20, wdt-260, hgt-60))
        self.textv.setWordWrap(True)
        self.textv.setText(txt)
        leghtext= len(txt)
        regex = re.findall('\n', txt)
        nstr=len(regex)
        leghtext=leghtext+nstr*int(leghtext/8)
        if leghtext>250:
            if len(ynph) > 0:
                fs = int((40 - 10*(leghtext/1000))*kfont)
            else:
                fs = int((56 - 10*(leghtext/1000))*kfont)
        elif leghtext in range(100,250):
            if len(ynph) > 0:
                fs = int((50 - 10*(leghtext/500))*kfont)
            else:
                fs = int((66-10*(leghtext/500))*kfont)
        elif leghtext in range(0,99):
            if len(ynph) > 0:
                fs = int((60-10*(leghtext/200))*kfont)
            else:
                fs = int((76-10*(leghtext/200))*kfont)

        tfs = "background-color: rgba(0,0,80,0); color: rgba(225,255,255,255); border:0px solid black;font-size:" + str(fs) + "px"
        self.textv.setFont(self.font)
        self.textv.setFrameShape(QFrame.Box)
        self.textv.setAutoFillBackground(True)
        self.textv.setStyleSheet(tfs)
#Конец модуля текста вопроса

#Прогрессбар таймера
        self.progressbar = QProgressBar(self)                   # 1
        self.progressbar.setMinimum(0)                          # 2
        self.progressbar.setMaximum(ttq)
        self.progressbar.setGeometry(10,hgt-30,wdt-20,30)
        self.progressbar.setTextVisible(False)
        self.progressbar.setStyleSheet("""
                           QProgressBar {
                               border: 2px solid rgba(33, 37, 43, 60);
                               border-radius: 12px;
                               background-color: rgba(00, 00, 200, 30);
                               color: black;
                               }
                           QProgressBar::chunk {
                               background-color: rgba(100,100,00,50);
                               }
                           """)
#экран плавно меняет фон
        def scrupd():
            if os.path.exists("disanim"):
                self.sth = "background-color: rgba(0,40,230,255); color: #ddFFaa;"
            else:
                self.blc+=self.shag
                if self.blc>=254 or self.blc<=60:
                    self.shag*= -1
                self.sth="background-color: rgba(0,0,255,"+str(self.blc)+"); color: #ddFFaa;"
            self.setStyleSheet(self.sth)
        self.blc = 80
        self.shag=1
        self.tmr = QTimer()
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(40)
        #экран

        self.step = 0
        self.timer = QTimer(self)                               # 4
        self.timer.timeout.connect(self.update_func)
        icon = QIcon("./img/icon/timerw.png")
        self.ss_button = QPushButton(icon,"", self)             # 5
        self.ss_button.clicked.connect(self.start_stop_func)
        self.nxt_button = QPushButton('Ответ', self)          # 6
        self.nxt_button.clicked.connect(self.nxt_func)

        # self.ss_button.setGeometry(15,hgt-140,120,100)
        self.ss_button.setGeometry(15, hgt - 130, 90, 90)
        self.ss_button.setIconSize(QSize(85, 85))
        cssbut = "QPushButton { background-color: rgba(0,0,200,25); color: rgba(150,200,250,255); text-align:center center; background-position: bottom center; border: 2px solid rgb(160, 180, 250); border-radius: 12px; font-size: 38px;} QPushButton::hover{background-color: #0077ff ;}"
        self.ss_button.setStyleSheet(cssbut)
        cssbut1 = "QPushButton { background-color: rgba(0,0,200,25); color: rgba(150,200,250,255); text-align:center center; background-position: bottom center; border: 2px solid rgb(160, 180, 250); border-radius: 12px; font-size: 38px;} QPushButton::hover{background-color: #0077ff ;}"
        self.nxt_button.setGeometry(wdt-210,hgt-100,200,60)
        self.nxt_button.setStyleSheet(cssbut1)

        # кнопка подсказки
        self.tl_button=QPushButton('Подсказка',self)
        self.tl_button.setGeometry((wdt - 200)/2, hgt - 100, 200, 60)
        self.tl_button.setStyleSheet(cssbut1)
        self.tl_button.clicked.connect(self.tl_func)
        if int(cpd)>0:
            self.tl_button.setVisible(True)
        else:
            self.tl_button.setVisible(False)
# Использование подсказки
    def tl_func(self):
        #self.start_stop_func()
        self.ss_button.setText('')
        self.ss_button.setIconSize(QSize(90, 90))
        self.timer.stop()
        self.tiker.stop()
        self.step = 0
        self.progressbar.setValue(self.step)
        query2 = QSqlQuery()
        if not query2.exec("UPDATE settings set tmpDat1 =" + str(int(cost) - int(cpd)) + ";"):
            logging.error("Failed to query database9")

        if len(ynpht) > 0:

            pixmap = QPixmap("./img/" + ynpht)
            if len(txtp)>0:
                self.textv.setGeometry(QRect(120, hgt*2/3-20, wdt-240, hgt/3-40))
                self.photo.setGeometry(QRect(100, 20, wdt-200, hgt*2/3-100))
                pixmap = pixmap.scaled(wdt - 200, hgt * 2 / 3 - 100, Qt.KeepAspectRatio)

            else:
                self.photo.setGeometry(QRect(120, 20, wdt - 240, hgt  - 160))
                pixmap = pixmap.scaled(wdt - 240, hgt  - 180, Qt.KeepAspectRatio)


            self.photo.setPixmap(pixmap)
            self.photo.setVisible(True)

        else:
            self.textv.setGeometry(QRect(130, 20, wdt-260, hgt-60))
            self.photo.setVisible(False) 

        self.tl_button.setVisible(False)
        leghtext = len(txtp)
        
        if leghtext>250:
            if len(ynpht) > 0:
                fs = int((40 - 10 * (leghtext / 1000)) * kfont)
            else:
                fs = int((56 - 10 * (leghtext / 1000)) * kfont)
        elif leghtext in range(100,250):
            if len(ynpht) > 0:
                fs = int((50 - 10 * (leghtext / 500)) * kfont)
            else:
                fs = int((66 - 10 * (leghtext / 500)) * kfont)
        elif leghtext in range(0,100):
            if len(ynpht) > 0:
                fs = int((60 - 10 * (leghtext / 200)) * kfont)
            else:
                fs = int((76 - 10 * (leghtext / 200)) * kfont)

        tfs = "background-color: rgba(0,0,80,0); color: rgba(225,255,255,255); border:0px solid black;font-size:" + str(fs) + "px"
        self.textv.setText(txtp)
        self.textv.setStyleSheet(tfs)
        
    def start_stop_func(self):
        self.ss_button.setIconSize(QSize(0,0))

        if self.ss_button.text() == '':
            self.ss_button.setText(' ')
            self.timer.start(100)
            self.tiker = self.timerSound.play()     
        else:
            self.ss_button.setText('')
            self.ss_button.setIconSize(QSize(90, 90))
            self.timer.stop()
            self.tiker.stop()
             
    def update_func(self):
            self.step += 1
            tob=int((ttq-self.step)/10+1)
            self.ss_button.setText(str(tob))
            self.progressbar.setValue(self.step)
            alppb=str(30+220*self.step/ttq)
            stsh= "QProgressBar {border: 2px solid rgba(33, 37, 43, 60);border-radius: 12px;text-align: center;background-color: rgba(00, 00, 200, 30);color: black;}QProgressBar::chunk {background-color: rgba(80,200,255,"+alppb+");border-radius: 12px;}"
            self.progressbar.setStyleSheet(stsh)
 
            if (ttq-self.step)/10+1==8:
                self.tickend=self.tickEndSound.play()

            if self.step >= ttq:
                self.ss_button.setText('0')
                self.timer.stop()
                self.step = 0
                self.tiker.stop()
#окно ответа
    def nxt_func(self):
        self.timer.stop()
        self.tiker.stop()

        wdt=self.size().width()
        hgt=self.size().height()
        
        if len(ynpha) > 0:
            pixmap=QPixmap("./img/"+ynpha)
            pixmap = pixmap.scaled(wdt - 240, hgt * 2 / 3 - 100, Qt.KeepAspectRatio)
            self.photo.setPixmap(pixmap)
            self.textv.setGeometry(QRect(120, hgt*2/3-20, wdt-240, hgt/3-40))
            self.photo.setVisible(True) 
        else:
            self.textv.setGeometry(QRect(120, 20, wdt-240, hgt-100))
            self.photo.setVisible(False) 

        leghtext = len(txta)
        
        if leghtext>250:
            if len(ynpha) > 0:
                fs = int((40 - 10 * (leghtext / 1000)) * kfont)
            else:
                fs = int((56 - 10 * (leghtext / 1000)) * kfont)
        elif leghtext in range(100,250):
            if len(ynpha) > 0:
                fs = int((50 - 10 * (leghtext / 500)) * kfont)
            else:
                fs = int((66 - 10 * (leghtext / 500)) * kfont)
        elif leghtext in range(0,99):
            if len(ynpha) > 0:
                fs = int((60 - 10 * (leghtext / 200)) * kfont)
            else:
                fs = int((76 - 10 * (leghtext / 200)) * kfont)
        
        tfs = "background-color: rgba(0,0,80,0); color: rgba(225,255,255,255); border:0px solid black;font-size:" + str(fs) + "px"
        self.textv.setText(txta)
        self.textv.setStyleSheet(tfs)

        self.ss_button.setVisible(False)
        self.progressbar.setVisible(False)
        self.tl_button.setVisible(False)

        self.nxt_button.setText('Далее')
        try:
            if not self.tiker:
                print ("нет tiker")
            else:
                self.tiker.stop()
        except NameError:
            print()        


        self.nxt_button.clicked.connect(self.nxta_func)
        
    def nxta_func(self):
        self.tmr.stop()
        self.ss_button.setVisible(True)
        self.progressbar.setVisible(True)
        self.close()









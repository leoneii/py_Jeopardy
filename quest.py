import logging
import sys

from PySide6 import QtCore
from PySide6.QtCore import (Qt, QRect, QTimer, QSize)
from PySide6.QtSql import QSqlQuery, QSqlDatabase
from PySide6.QtWidgets import (QApplication, QLabel,QWidget,QVBoxLayout,QHBoxLayout,
        QFrame,QProgressBar,QPushButton)
from PySide6.QtGui import (QFont, QColor, QPixmap, QIcon)

#import widget

#from widget import sqlDB
phyn=1 # 0-без фото, 1- с фото
testtext=" "
#ttq=10 #время на ответ сек.

# переменные ответа (так не должно быть, но без этого не работает вообще :(  )
#ynpha=1
#txta="kjghkjhg kjhgjhg jhgfghgf ffgh f jhgfg hjjkjg"

#global sqlDB
#appq = QApplication([])
#widget.sqlDB.open()

# global sqlDB
# QtCore.QLocale.setDefault(QtCore.QLocale("ru_RU"))
# sqlDB = QSqlDatabase.addDatabase('QSQLITE')
# sqlDB.setDatabaseName('jep.sqlite')
# sqlDB.open()


class winq(QWidget):

    font = QFont()
    font.setFamilies([u"Arial"])
    font.setBold(True)
    alignmentc=Qt.AlignmentFlag.AlignCenter
    blc = 40
    chk = 1

    def updtime(self):
        global blc, chk
        blc += chk
        if blc > 253:
            chk = -1
        elif blc < 40:
            chk = 1
        print(blc)
        sss = "background-color: rgba(0,0," + str(blc) + "); color: #ddFFaa;"
        winq.setStyleSheet(sss)

    timer = QTimer()
    timer.setInterval(100)  # msecs 100 = 1/10th sec
    timer.timeout.connect(updtime)
    timer.start()

    def __init__(self,appl,ynph,txt,ynpha_l, txta_l,ttq_l):

        global txta
        global ynpha
        global ttq #время таймера
        ttq=ttq_l*10
        txta=txta_l
        ynpha=ynpha_l




        super().__init__()
        geometry = appl.primaryScreen().availableGeometry()
        self.setGeometry(geometry)
        wdt=self.size().width()
        hgt=self.size().height()       
        # self.setStyleSheet("""
        # background-color: rgba(0,0,60,10);
        # color: #ddFFaa;
        # font-family: Arial;
        # """)

        #Фото
        if len(ynph) > 0:
            self.photo=QLabel(self)
            self.photo.setAlignment(self.alignmentc)
            self.photo.setGeometry(QRect(100, 20, wdt-200, hgt*2/3))
            pixmap=QPixmap("img/"+ynph)
            pixmap = pixmap.scaled(900, hgt*2/3, Qt.KeepAspectRatio) 
            self.photo.setPixmap(pixmap)
#Конец фото

#текст вопроса
        self.textv = QLabel(self)
        self.textv.setObjectName(u"txtvopr")
        self.textv.setAlignment(self.alignmentc)
        if len(ynph) > 0:
            self.textv.setGeometry(QRect(100, hgt*2/3+20, wdt-200, hgt/3-40))
        else:
            self.textv.setGeometry(QRect(100, 20, wdt-200, hgt-40))
        self.textv.setWordWrap(True)
        self.textv.setText(txt)
        leghtext= len(txt)
        if leghtext>250:
            if phyn==1:
                fs=48
            else:
                fs=52
        elif leghtext in range(100,250):
            if phyn==1:
                fs=60
            else:
                fs=65            
        elif leghtext in range(1,99):
            if phyn==1:
                fs=80
            else:
                fs=85            
        #tfs="border:0px solid black;font-size:"+str(fs)+"px"
        tfs = "background-color: rgba(0,0,80,10); border:0px solid black;font-size:" + str(fs) + "px"
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
        #экран
        def scrupd():
            self.blc+=self.shag
            if self.blc>=254 or self.blc<=60:
                self.shag*= -1
            #print(self.blc)
            self.sth="background-color: rgba(0,0,255,"+str(self.blc)+"); color: #ddFFaa;"
            self.setStyleSheet(self.sth)
        self.blc = 80
        self.shag=1
        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(40)
        #экран

        self.step = 0
        self.timer = QTimer(self)                               # 4
        self.timer.timeout.connect(self.update_func)
        icon = QIcon("img/icon/timerw.png")
        self.ss_button = QPushButton(icon,"", self)             # 5
        self.ss_button.clicked.connect(self.start_stop_func)
        self.nxt_button = QPushButton('Ответ', self)          # 6
        self.nxt_button.clicked.connect(self.nxt_func)

        self.ss_button.setGeometry(15,hgt-165,140,120)
        self.ss_button.setIconSize(QSize(96, 96))
        cssbut = "QPushButton { background-color: rgba(0,0,200,255); color: rgba(150,200,250,255); text-align:center center; background-position: bottom center; border: 2px solid rgb(160, 180, 250); border-radius: 12px; font-size: 68px;} QPushButton::hover{background-color: #0077ff ;}"
        self.ss_button.setStyleSheet(cssbut)
        cssbut1 = "QPushButton { background-color: rgba(0,0,200,255); color: rgba(150,200,250,255); text-align:center center; background-position: bottom center; border: 2px solid rgb(160, 180, 250); border-radius: 12px; font-size: 38px;} QPushButton::hover{background-color: #0077ff ;}"
        self.nxt_button.setGeometry(wdt-165,hgt-95,150,60)
        self.nxt_button.setStyleSheet(cssbut1)

    def start_stop_func(self):
        self.ss_button.setIconSize(QSize(0,0))
        if self.ss_button.text() == '':
            self.ss_button.setText(' ')
            self.timer.start(100)
        else:
            self.ss_button.setText('')
            self.ss_button.setIconSize(QSize(96, 96))
            self.timer.stop()
 
    def update_func(self):
            self.step += 1
            tob=int((ttq-self.step)/10+1)
            self.ss_button.setText(str(tob))
            self.progressbar.setValue(self.step)
            alppb=str(30+220*self.step/ttq)
            stsh="QProgressBar {border: 2px solid rgba(33, 37, 43, 60);border-radius: 12px;text-align: center;background-color: rgba(00, 00, 200, 30);color: black;}QProgressBar::chunk {background-color: rgba(80,200,255,"+alppb+");border-radius: 12px;}"
            self.progressbar.setStyleSheet(stsh)
 
            if self.step >= ttq:
                self.ss_button.setText('0')
                self.timer.stop()
                self.step = 0
#окно ответа
    def nxt_func(self):
            wdt=self.size().width()
            hgt=self.size().height()
            if len(ynpha) > 0:
                 pixmap=QPixmap("img/"+ynpha)
                 self.photo.setPixmap(pixmap)
                 self.textv.setText(txta)
            if len(ynpha) > 0:
                 self.textv.setGeometry(QRect(100, hgt*2/3+20, wdt-200, hgt/3-40))
            else:
                 self.textv.setGeometry(QRect(100, 20, wdt-200, hgt-40))
                 self.textv.setText(txta)

            self.ss_button.setVisible(False)
            self.progressbar.setVisible(False)

            self.nxt_button.setText('Далее')
            self.nxt_button.clicked.connect(self.nxta_func)
        
        
 
    def nxta_func(self):
        # wdt=self.size().width()
        # hgt=self.size().height()
        # if self.ynph==1:
        #     pixmap=QPixmap("img/tree.jpg")
        #     self.photo.setPixmap(pixmap)

        # if self.ynph==1:
        #     self.textv.setGeometry(QRect(100, hgt*2/3+20, wdt-200, hgt/3-40))
        # else:
        #     self.textv.setGeometry(QRect(100, 20, wdt-200, hgt-40))
        #     self.textv.setText(self.txt)
        self.tmr.stop()
        self.ss_button.setVisible(True)
        self.progressbar.setVisible(True)
        self.close()
#        self.destroy()







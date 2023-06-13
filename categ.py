import logging

from PySide6.QtCore import (QTimer, QEventLoop, QRect, Qt, QEvent, QPoint, QMetaObject)
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QFrame, QPushButton)

from widget import wnd


catname=["","","","","","","","","",""]
query = QSqlQuery()
if not query.exec(
        """
            SELECT COUNT(*) FROM Category;
        """
):
        logging.error("Failed to query database")
query.next()
ckols=int(query.value(0))

query = QSqlQuery()
if not query.exec(
        """
            SELECT * FROM Category;
        """
):
        logging.error("Failed to query database")
query.first()
for i in range(ckols):
    catname[i]=str(query.value(1))
    query.next()

blc=80
shag=1
smx=5
gx=200

global tnm

#конец блока переменных
class Category(QWidget):
    # рисуем анимацию фона

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

    def __init__(self,apt):
        #опять глобальная apt
        global appt
        appt=apt
        super().__init__()
        QMetaObject.connectSlotsByName(self)
#        geometry = apc.primaryScreen().availableGeometry()
        geometry = apt.primaryScreen().availableGeometry()
        self.setGeometry(geometry)

#Анимация фона        
        def scrupd():
            global blc, shag
            blc+=shag
            if blc>=254 or blc<=50:
                shag*= -1
            self.sth="background-color: rgba(0,0,"+str(blc)+",255); color: #ddFFaa;"
            self.setStyleSheet(self.sth)

        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(40)        
#конец анимации фона
        wd = self.size().width()-20
        hd = self.size().height()-20
        wdb=wd/3
        hdb=(hd-50)/6
        if ckols>6:
            hdb=(hd-50)/ckols
        hpos=((hd-50)-(hdb+5)*ckols)/2

        shst="QPushButton { background-color: rgba(0,0,200,100); color: rgba(220,220,255,255); text-align:center center; background-position: bottom center; border: 2px solid rgb(160, 180, 250); border-radius: 12px; font: Bold 38px} QPushButton::hover{background-color: #0077ff ;}"

        for i in range(ckols):
            self.cbut=QPushButton(catname[i],self)
            self.cbut.setGeometry(wdb,hpos+(hdb+5)*i+35,wdb,hdb)
            self.cbut.setObjectName(str(i))
            self.cbut.setStyleSheet(shst)
            self.cbut.clicked.connect(self.catchois)
            self.cbut.show()
    def catchois(self):
        global tnm
        snd = self.sender()
        catn=snd.objectName()
        query = QSqlQuery()
        if not query.exec("SELECT * FROM Category WHERE catcode="+str(int(catn)+1)+";"):
            logging.error("Failed to query database")
        query.first()
        tnm=str(query.value(1))
        tnn=str(query.value(0))
        query = QSqlQuery()
        if not query.exec("UPDATE settings set curCatCode =" + tnn+", curCatName ='"+tnm+"';"):
            logging.error("Failed to query database")
        query.exec("select * from settings")
        query.first()

        self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()


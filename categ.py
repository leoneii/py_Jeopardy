import sys
import PySide6
from PySide6 import QtCore
# import PySide6
from PySide6.QtCore import (QTimer, QEventLoop, QRect, Qt, QEvent, QPoint, QMetaObject)
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QFrame, QPushButton)
from PySide6.QtWidgets import QMessageBox
# забирать из базы данных
ckols=5
catname=["Московские бульвары","Проспекты","Набережные","Московский метрополитен","Музеи Москвы","Кино","Транспорт","Парки"]
blc=80
shag=1
smx=5
gx=200

#конец блока переменных
class Category(QWidget):

    def __init__(self):
        super().__init__()
        QMetaObject.connectSlotsByName(self)
    # def __init__(self, ckols, parent=None):
    #     super(Category, self).__init__(parent)
        geometry = apc.primaryScreen().availableGeometry()
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

        #for i in range(ckols):
        i=1
        self.cbut=QPushButton(catname[i],self)
        self.cbut.setGeometry(wdb,hpos+(hdb+5)*i+35,wdb,hdb)
        self.cbut.setObjectName("cat"+str(i))
        self.cbut.setStyleSheet(shst)
        self.cbut.clicked.connect(self.catchois(self.cbut))
        self.cbut.show()
    def catchois(self,but):
            # snd = self.sender()
        QMessageBox.about(self, "Нажматие!!!))", but.objectName())
        self.destroy()




        
 

apc=QApplication([])
wnc=Category()
wnc.showFullScreen()
sys.exit(apc.exec())
# This Python file uses the following encoding: utf-8
import logging
import sys

import PySide6
from PySide6 import QtCore
# import PySide6
from PySide6.QtCore import (QTimer, QEventLoop, QRect, Qt, QEvent)
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QFrame)
from PySide6.QtWidgets import QMessageBox

from quest import winq

#база данных
#global sqlDB
QtCore.QLocale.setDefault(QtCore.QLocale("ru_RU"))
sqlDB = QSqlDatabase.addDatabase('QSQLITE')
sqlDB.setDatabaseName('jep.sqlite')
sqlDB.open()

#переменные
continue_run = True

kolt=5
kolv=5
otst=10



#Чтение настроек из БД
query = QSqlQuery()
if not query.exec(
        """
        SELECT * from settings;
        """
):
    logging.error("Failed to query database")

query.nextResult()
query.next()
kolt = int(query.value(1))
kolv = int(query.value(2))
ttq = int(query.value(3))
otst = int(query.value(4))




#Проверка для запуска без консоли
# try:
#  kolt=int(input("количество тем: "))
#  kolv=int(input("количество вопросов в теме: "))
# except EOFError:
#     print("Exception handled")


# темы___________________________
ntem=["Анекдоты","Нам песня строить и жить помогает","Улицы в лицах","Живопись и музыка","Меценаты","Исторические анекдоты","Покорители"]
# цена вопроса
cnv=["10","20","30","40","50","60","70","80","90","100"]
# шрифт
font = QFont()
font.setFamilies([u"Serif"])
#font.setPointSize(22)
font.setBold(True)
alignmentc=Qt.AlignmentFlag.AlignCenter
css = "QLabel { background-color: rgba(0,0,180,255); color: rgba(255,255,255,255); text-align: bottom center; background-position: bottom center;}"
cssbut = "QLabel { background-color: rgba(0,0,180,255); color: rgba(255,255,255,255); text-align:center center; background-position: bottom center;} QLabel::hover{background-color: #0077ff ;}"
bgpalbut = QPalette()
bgpalbut.setColor(QPalette.Button, Qt.blue )


class wnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
#        self.continue_run =True
        self.installEventFilter(self)
        geometry = app.primaryScreen().availableGeometry()
        self.setGeometry(geometry)
        wdh=self.size().width()
        hgt=self.size().height()
#        #Расчет размеров________________
        shl=wdh/5-20
        shp=wdh-wdh/5
        gp=wdh/5
        vp=10
        wkn=(shp-(10+otst*kolv))/kolv
        hkn=(hgt-vp-(10+otst*kolt))/kolt

#       Создание запроса к БД
        query = QSqlQuery()
        if not query.exec(
                """
                SELECT * from ThemeAndQ;
                """
        ):
            logging.error("Failed to query database")
        query.next()
        rowdb=0
        for i in range (kolt):
            lg=10
            lv=vp+(hkn+otst)*i
            ltxt=str(query.value(0))
            #ltxt=ntem[i]
            self.temb = QLabel(self)
            self.temb.setObjectName(u"label"+str(i))
            self.temb.setGeometry(QRect(lg, lv, shl, hkn))
            self.temb.setWordWrap(True)
            self.temb.setText(ltxt)
            leghtext= len(ltxt)
            font.setPointSize(hgt/(leghtext+18)+5)
            self.temb.setFont(font)
            self.temb.setFrameShape(QFrame.Box)
            self.temb.setAutoFillBackground(True)
            self.temb.setStyleSheet(css)


            for j in range (kolv):
                gij=gp+(wkn+otst)*j
                vij=vp+(hkn+otst)*i
                ktxt=str(query.value(2))
                self.temb = QLabel(self)
               # self.temb.setObjectName(u"kn_"+str(i)+"_"+str(j))
                self.temb.setObjectName(str(rowdb))
                rowdb = rowdb+1

                self.temb.setGeometry(QRect(gij, vij, wkn, hkn))
            #                self.temb.setWordWrap(True)
                self.temb.setText(ktxt)
                self.temb.setAlignment(alignmentc)
                leghtext= len(ktxt)
                font.setPointSize(hgt/(leghtext+18)+20)
                self.temb.setFont(font)
                self.temb.setFrameShape(QFrame.Box)
                self.temb.setAutoFillBackground(True)
                #self.temb.setBackgroundRole()
                self.temb.setStyleSheet(cssbut)
                self.temb.installEventFilter(self)
                #цена подсказки
                cpd=str(query.value(7))
                if len(cpd)>0:
                    lbpd=QLabel(parent=self.temb)
                    lbpd.setText(cpd)
                    lbpd.setGeometry(wkn*3/4-8,hkn*3/4-8,wkn/4+2,hkn/4+2)
                    csspd = "QLabel { background-color: rgba(0,200,150,160); border: none; border-radius: 10px; color: rgba(155,255,155,255); text-align: center center; background-position: center center; font-size: 46px}"
                    lbpd.setStyleSheet(csspd)
                    lbpd.setAlignment(alignmentc)
                query.next()





    def colorchange(self):
            #for z in range(250):
        z = 1
        revers = False
        while continue_run:
            self.bgcolor(QColor(0,0,z+50))
        # self.setStyleSheet('background: rgb('+str(z+1)+',40,40);')
            q = QEventLoop(self)
            QTimer.singleShot(40, q.quit)
            q.exec()
            if revers:
                z=z-1
            else:
                z=z+1
            if z==205:
                revers=True
            if z==1:
                revers=False

    def bgcolor(self,color=Qt.red):
        bgpalette = QPalette()
        bgpalette.setColor(QPalette.Window, color)
        self.setPalette(bgpalette)

    def eventFilter(self, obj, event):
          if obj != self:
               if event.type() == QEvent.MouseButtonPress:
                        mouse_event = QMouseEvent(event)
                        if mouse_event.buttons() == Qt.LeftButton:
                    #QMessageBox.about(self,"Нажматие!!!))","Нажали левую кнопку мыши")
                            #obj.setVisible(False)

                            #запрос БД
                            query = QSqlQuery()
                            if not query.exec(
                                     """
                                      SELECT * from ThemeAndQ;
                                      """
                            ):
                                 logging.error("Failed to query database")
                            query.next()#первая строка БД
                            #QMessageBox.information(self, "Нажматие!!!))", str(obj.objectName()))
                            query.seek(int(obj.objectName())) #переходим к конкретной строке БД
                            global newwind
                            newwind = winq(app, str(query.value(3)),str(query.value(1)) , str(query.value(5)), str(query.value(4)),ttq)
                            newwind.showFullScreen()
                            # записываем текст ответа в ячейку цены вопроса
                            obj1 = self.findChild(QLabel, obj.objectName())
                            obj1.setText(str(query.value(4)))
                            ds=len(str(query.value(4)))
                            if ds<60:
                                cssa = "QLabel { background-color: rgba(0,100,255,90); border: none;color: rgba(255,255,200,255); text-align: bottom center; background-position: bottom center; font-size: 32px}"
                            elif 60<=ds<=100:
                                cssa = "QLabel { background-color: rgba(0,100,255,90); border: none;color: rgba(255,255,200,255); text-align: bottom center; background-position: bottom center; font-size: 24px}"
                            elif ds>100:
                                cssa = "QLabel { background-color: rgba(0,100,255,90); border: none;color: rgba(255,255,200,255); text-align: bottom center; background-position: bottom center; font-size: 20px}"


                            obj1.setStyleSheet(cssa)
                            obj1.setWordWrap(True)
               # elif mouse_event.buttons() == Qt.MidButton:
               #     QMessageBox.information(self,"Нажматие!!!))","Нажали среднюю кнопку мыши")
                        elif mouse_event.buttons() == Qt.RightButton:
                            QMessageBox.warning(self,"Нажматие!!!))","Нажали правую кнопку мыши "+str(obj.objectName()) )
          # elif obj == self:
          #        if event.type() == QEvent.Show:
          #          self.colorchange()

          if event.type() == QEvent.KeyPress:
              # keyEvent = QKeyEvent(event)
              # QMessageBox.warning(self,"Нажматие!!!))","Нажали правую кнопку мыши "+str(keyEvent)+" ___ "+str(event.key()) )
               if event.key() == Qt.Key_Escape:
                 # QMessageBox.warning(self,"Нажматие!!!))","Нажали правую кнопку мыши ")
                  global continue_run
                  continue_run = False
                  #sys.exit(self)
                  app.quit()
                  app.exit(0)


          return QWidget.eventFilter(self, obj, event)


if __name__ == "__main__":
    app = QApplication([])
    window = wnd()
   # newwind = winq(app,1,"текст вопроса"*5,1,"текст ответа")
    window.showFullScreen()
    window.colorchange()
    sys.exit(app.exec())
    sqlDB.close()
    sqlDB.removeDatabase('QSQLITE')
    sqlDB.removeDatabase('jep.sqlite')

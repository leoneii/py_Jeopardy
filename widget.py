# This Python file uses the following encoding: utf-8
import logging
import os
from PySide6 import QtCore
# import PySide6
from PySide6.QtCore import (QTimer, QEventLoop, QRect, Qt, QEvent, QPoint)
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QFrame)

from quest import winq
global cenv
cenv=0
#global apt

#база данных
#global sqlDB
QtCore.QLocale.setDefault(QtCore.QLocale("ru_RU"))
sqlDB = QSqlDatabase.addDatabase('QSQLITE')
sqlDB.setDatabaseName(os.path.dirname(os.path.abspath(__file__))+"/./jep.sqlite")
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
    logging.error("Failed to query database5")

query.nextResult()
query.next()
#kolt = int(query.value(1))
#kolv = int(query.value(2))
ttq = int(query.value(3))
otst = int(query.value(4))

#переменные красот экрана
smx=3
gx=200

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
cssbut1 = "QLabel { background-color: rgba(250,0,250,80); color: rgba(255,255,255,255); text-align:center center; background-position: bottom center;} QLabel::hover{background-color: #0077ff ;}"

bgpalbut = QPalette()
bgpalbut.setColor(QPalette.Button, Qt.blue )


class wnd(QWidget):


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

    # def __init__(self, parent=None):
    #     super().__init__(parent)
    def __init__(self, catname, apt, parent= None):
        #вот тут делаем apt глобальной переменной
        global appt
        appt=apt
        super(wnd, self).__init__(parent)
        #QWidget.__init__(self,parent)

        #super(wnd, self).__init__(parent, apt)
        #print(pcatname)
        #catname= catname.str.strip()
        #catn = "hjgfjhgfgh"
        #catname = str(pcatname).
        #catname=""
#       Высчитываем количество тем и вопросов
        query2 = QSqlQuery()
        if not query2.exec("SELECT COUNT(DISTINCT Theme) FROM ThemeAndQ WHERE catname = '"+ catname +"' ;"):
            logging.error("Failed to query database3")
        query2.first()
        kolt = int(query2.value(0))
        print(kolt)
        query2 = QSqlQuery()
        if not query2.exec("SELECT Theme, COUNT(*) value_count FROM ThemeAndQ WHERE catname = '"+ catname +"' GROUP BY Theme HAVING value_count > 1  ;"):
            logging.error("Failed to query database4")
        query2.first()
        kolv = int(query2.value(1))


        self.installEventFilter(self)
        geometry = apt.primaryScreen().availableGeometry()
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


#       Создание запроса к БД, создаем таблицу
        query = QSqlQuery()
        if not query.exec( "SELECT * from ThemeAndQ  WHERE Catname= '"+catname+"' ORDER BY Theme, Cost ;" ):
            logging.error("Failed to query database8")
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
            font.setPointSize(hgt/(leghtext+20))
            self.temb.setFont(font)
            self.temb.setFrameShape(QFrame.Box)
            self.temb.setAutoFillBackground(True)
            self.temb.setStyleSheet(css)


            for j in range (kolv):
                gij=gp+(wkn+otst)*j
                vij=vp+(hkn+otst)*i
                ktxt=str(query.value(2))
                self.temb = QLabel(self)
                self.temb.setObjectName(str(rowdb))
                rowdb = rowdb+1

                self.temb.setGeometry(QRect(gij, vij, wkn, hkn))
                self.temb.setText(ktxt)
                self.temb.setAlignment(alignmentc)
                leghtext= len(ktxt)
                font.setPointSize(hgt/(leghtext+20))
                self.temb.setFont(font)
                self.temb.setFrameShape(QFrame.Box)
                self.temb.setAutoFillBackground(True)
                #self.temb.setBackgroundRole()
                self.temb.setStyleSheet(cssbut)
                scbon=bool(query.value(8))
                if scbon==True:
                    self.temb.setStyleSheet(cssbut1)
                    lbbon=QLabel(parent=self.temb)
                    lbbon.setText("Бонусный вопрос")
                    lbbon.setGeometry(wkn*2/4-8,hkn*3/4-8,wkn/2+2,hkn/4+2)
                    lbbon.setAlignment(alignmentc)
                    lbbon.setVisible(True)
                self.temb.installEventFilter(self)
                self.temb.setWordWrap(False) #флаг кликабельности

                #цена подсказки
                cpd=str(query.value(7))
                if len(cpd)>0:
                    lbpd=QLabel(parent=self.temb)
                    lbpd.setObjectName("pd"+str(rowdb))
                    lbpd.setText("-"+cpd)
                    lbpd.setGeometry(wkn*3/4-8,hkn*3/4-8,wkn/4+2,hkn/4+2)
                    csspd = "QLabel { background-color: rgba(0,200,150,160); border: none; border-radius: 10px; color: rgba(155,255,155,255); text-align: center center; background-position: center center; font-size: 46px}"
                    lbpd.setStyleSheet(csspd)
                    lbpd.setAlignment(alignmentc)
                    lbpd.setVisible(True)


                query.next()

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


    def eventFilter(self, obj, event):
          obj1 = self.findChild(QLabel, obj.objectName())
          if obj != self and obj1.wordWrap()==False:
               if event.type() == QEvent.MouseButtonPress:
                        mouse_event = QMouseEvent(event)
                        if mouse_event.buttons() == Qt.LeftButton:
                    #QMessageBox.about(self,"Нажматие!!!))","Нажали левую кнопку мыши")
                            #obj.setVisible(False)
                            quecat=QSqlQuery()
                            if not quecat.exec("SELECT * from settings ;"):
                                logging.error("Failed to query database11")
                            quecat.first()
                            catname=quecat.value(8)
                            #запрос БД
                            query = QSqlQuery()
                            if not query.exec("SELECT * from ThemeAndQ  WHERE catname = '"+catname+"' ORDER BY Theme, Cost ;"):
                                logging.error("Failed to query database12")
                            query.next()#первая строка БД
                            #QMessageBox.information(self, "Нажматие!!!))", str(obj.objectName()))
                            query.seek(int(obj.objectName())) #переходим к конкретной строке БД
                            global newwind
#                            newwind = winq(app, str(query.value(3)),str(query.value(1)) , str(query.value(5)), str(query.value(4)),ttq,str(query.value(6)),str(query.value(7)))
                            newwind = winq(appt,str(query.value(3)),str(query.value(1)) , str(query.value(5)), str(query.value(4)), ttq, str(query.value(6)), str(query.value(7)), str(query.value(2)))
                            newwind.showFullScreen()
                            cnv=query.value(2)
                            query1=QSqlQuery()
                            if not query1.exec("UPDATE settings set tmpDat =" + str(cnv) + ", tmpDat1 =" + str(cnv) + ";"):
                                logging.error("Failed to query database13")

                            self.hide()
                            # записываем текст ответа в ячейку цены вопроса

                            ipd="pd"+obj.objectName()
                            obj1.setText(str(query.value(4)))
                            ds=len(str(query.value(4)))
                            if ds<60:
                                cssa = "QLabel { background-color: rgba(0,100,255,90); border: none;color: rgba(255,255,200,255); text-align: bottom center; background-position: bottom center; font-size: 32px}"
                            elif 60<=ds<=100:
                                cssa = "QLabel { background-color: rgba(0,100,255,90); border: none;color: rgba(255,255,200,255); text-align: bottom center; background-position: bottom center; font-size: 24px}"
                            elif ds>100:
                                cssa = "QLabel { background-color: rgba(0,100,255,90); border: none;color: rgba(255,255,200,255); text-align: bottom center; background-position: bottom center; font-size: 20px}"
                            obj1.setStyleSheet(cssa)
                            obj1.setWordWrap(True)# флаг "невидимости и неактивности"


                            # удаляем цену подсказки
                            lbpd=obj.findChild(QLabel)
                            if lbpd != None:
                                lbpd.setVisible(False)

                            #obj2.setVisible(False)

               # elif mouse_event.buttons() == Qt.MidButton: #средняя кнопка
               #     QMessageBox.information(self,"Нажматие!!!))","Нажали среднюю кнопку мыши")
                        #elif mouse_event.buttons() == Qt.RightButton:
                            #QMessageBox.warning(self,"Нажматие!!!))","Нажали правую кнопку мыши "+str(obj.objectName()) )


          if event.type() == QEvent.KeyPress:
               if event.key() == Qt.Key_Escape:
                   self.hide()


          return QWidget.eventFilter(self, obj, event)

# This Python file uses the following encoding: utf-8
import sys
#import PySide6
from PySide6.QtWidgets import QApplication, QWidget
import time
from PySide6.QtCore import (QCoreApplication, QTimer, QEventLoop, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QMouseEvent ,QKeyEvent,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
        QSizePolicy, QWidget, QFrame)
from knot import knoT
from clilabel import ClickedLabel

kolt=5
kolv=5
otst=10

continue_run = True

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
        shl=wdh/4-20
        shp=wdh-wdh/4
        gp=wdh/4
        vp=10
        wkn=(shp-(10+otst*kolv))/kolv
        hkn=(hgt-vp-(10+otst*kolt))/kolt
        for i in range (kolt):
            lg=10
            lv=vp+(hkn+otst)*i
            ltxt=ntem[i]
            self.temb = QLabel(self)
            self.temb.setObjectName(u"label"+str(i))
            self.temb.setGeometry(QRect(lg, lv, shl, hkn))
            self.temb.setWordWrap(True)
            self.temb.setText(ltxt)
            leghtext= len(ltxt)
            font.setPointSize(hgt/(leghtext+18)+18)
            self.temb.setFont(font)
            self.temb.setFrameShape(QFrame.Box)
            self.temb.setAutoFillBackground(True)
            self.temb.setStyleSheet(css)
            



            for j in range (kolv):
                gij=gp+(wkn+otst)*j
                vij=vp+(hkn+otst)*i
                ktxt=cnv[j]
                self.temb = QLabel(self)
                self.temb.setObjectName(u"kn_"+str(i)+"_"+str(j))
                self.temb.setGeometry(QRect(gij, vij, wkn, hkn))
            #                self.temb.setWordWrap(True)
                self.temb.setText(ktxt)
                self.temb.setAlignment(alignmentc)
                leghtext= len(ktxt)
                font.setPointSize(hgt/(leghtext+18)+18)
                self.temb.setFont(font)
                self.temb.setFrameShape(QFrame.Box)
                self.temb.setAutoFillBackground(True)
                #self.temb.setBackgroundRole()
                self.temb.setStyleSheet(cssbut)
                self.temb.installEventFilter(self)
                
                
                
               

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
                        mouseEvent = QMouseEvent(event)
                        if mouseEvent.buttons() == Qt.LeftButton:
                    #QMessageBox.about(self,"Нажматие!!!))","Нажали левую кнопку мыши")
                            obj.setVisible(False)
               # elif mouseEvent.buttons() == Qt.MidButton:
               #     QMessageBox.information(self,"Нажматие!!!))","Нажали среднюю кнопку мыши")
                        elif mouseEvent.buttons() == Qt.RightButton:
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
    window.showFullScreen()    
    window.colorchange()
    sys.exit(app.exec())

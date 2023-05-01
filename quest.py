import logging
import sys
from PySide6.QtCore import (Qt,QRect,QTimer)
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import (QApplication, QLabel,QWidget,QVBoxLayout,QHBoxLayout,
        QFrame,QProgressBar,QPushButton)
from PySide6.QtGui import (QFont, QColor,QPixmap)

phyn=1 # 0-без фото, 1- с фото
testtext="Шёл мужик попу кивал. Чем мужик попу кивал? "
ttq=10 #время на ответ сек.
ttq=ttq*10

# переменные ответа (так не должно быть, но без этого не работает вообще :(  )
ynpha=1
txta="kjghkjhg kjhgjhg jhgfghgf ffgh f jhgfg hjjkjg"


#appq = QApplication([])

class winq(QWidget):
    #Обращение к бд
    query = QSqlQuery()
    if not query.exec(
            """
            SELECT * from ThemeAndQ;
            """
    ):
        logging.error("Quest to query database")
    query.next()


    font = QFont()
    font.setFamilies([u"Arial"])
    font.setBold(True)
    #font.setItalic(True)
    alignmentc=Qt.AlignmentFlag.AlignCenter
    def __init__(self,appl,ynph,txt,ynpha,txta):
        super().__init__()
        geometry = appl.primaryScreen().availableGeometry()
        self.setGeometry(geometry)
        wdt=self.size().width()
        hgt=self.size().height()       
        self.setStyleSheet("""
        background-color: #0000cc;
        color: #ddFFaa;
        font-family: Arial;
        """)

        #Фото
        if ynph==1:
            self.photo=QLabel(self)
            self.photo.setAlignment(self.alignmentc)
            self.photo.setGeometry(QRect(100, 20, wdt-200, hgt*2/3))
            pixmap=QPixmap("img/tree.jpeg")
            pixmap = pixmap.scaled(900, hgt*2/3, Qt.KeepAspectRatio) 
            self.photo.setPixmap(pixmap)
#Конец фото

#текст вопроса
        self.textv = QLabel(self)
        self.textv.setObjectName(u"txtvopr")
        self.textv.setAlignment(self.alignmentc)
        if ynph==1:
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
        tfs="border:0px solid black;font-size:"+str(fs)+"px"
        self.textv.setFont(self.font)
        self.textv.setFrameShape(QFrame.Box)
        self.textv.setAutoFillBackground(True)
        self.textv.setStyleSheet(tfs)
#Конец модуля текста вопроса

#Прогрессбар таймера
        self.progressbar = QProgressBar(self)                   # 1
        self.progressbar.setMinimum(0)                          # 2
        self.progressbar.setMaximum(ttq)
        # self.progressbar.setRange(0, 100)
        self.progressbar.setGeometry(10,hgt-30,wdt-20,30)
        self.progressbar.setStyleSheet("""
                           QProgressBar {
                               border: 2px solid rgba(33, 37, 43, 60);
                               border-radius: 12px;
                               text-align: center;
                               background-color: rgba(00, 00, 200, 30);
                               color: black;
                               }
                           QProgressBar::chunk {
                               background-color: rgba(ff,44,00,150);
                               }
                           """)
        self.step = 0
        self.timer = QTimer(self)                               # 4
        self.timer.timeout.connect(self.update_func)
 
        self.ss_button = QPushButton('Start', self)             # 5
        self.ss_button.clicked.connect(self.start_stop_func)
        self.nxt_button = QPushButton('Ответ', self)          # 6
        self.nxt_button.clicked.connect(self.nxt_func)
        self.ss_button.setGeometry(10,hgt-65,100,30)
        self.nxt_button.setGeometry(wdt-110,hgt-65,100,30)

    def start_stop_func(self):
        
        if self.ss_button.text() == 'Start':
            self.ss_button.setText('Stop')
            self.timer.start(100)
        else:
            self.ss_button.setText('Start')
            self.timer.stop()
 
    def update_func(self):
            self.step += 1
            self.progressbar.setValue(self.step)
 
            if self.step >= ttq:
                self.ss_button.setText('Start')
                self.timer.stop()
                self.step = 0
#окно ответа 
    def nxt_func(self):
        wdt=self.size().width()
        hgt=self.size().height()  
        if ynpha==1:
            pixmap=QPixmap("img/space.jpg")
            self.photo.setPixmap(pixmap)       

        if ynpha==1:
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

        self.ss_button.setVisible(True)
        self.progressbar.setVisible(True)
        self.close()
#        self.destroy() 

         





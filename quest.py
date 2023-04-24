import sys
from PySide6.QtCore import (Qt,QRect,QTimer)
from PySide6.QtWidgets import (QApplication, QLabel,QWidget,QVBoxLayout,QHBoxLayout,
        QFrame,QProgressBar,QPushButton)
from PySide6.QtGui import (QFont, QColor,QPixmap)

phyn=1 # 0-без фото, 1- с фото
testtext="Шёл мужик попу кивал. Чем мужик попу кивал? "
ttq=10 #время на ответ сек.
ttq=ttq*10

font = QFont()
font.setFamilies([u"Arial"])
#font.setPointSize(50)
font.setBold(True)
alignmentc=Qt.AlignmentFlag.AlignCenter



app = QApplication([])

class wing(QWidget):
    def __init__(self,ynph,txt):
        super().__init__()
        geometry = app.primaryScreen().availableGeometry()
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
            self.photo.setAlignment(alignmentc)
            self.photo.setGeometry(QRect(100, 20, wdt-200, hgt/2))
            pixmap=QPixmap("img/tree.jpeg")
           # pixmap.scaledToHeight(hgt/2)
            pixmap = pixmap.scaled(900, hgt/2, Qt.KeepAspectRatio) 
          # pixmap.setDevicePixelRatio()
            #self.photo.setScaledContents(True)
            self.photo.setPixmap(pixmap)
#Конец фото

#текст вопроса
        self.textv = QLabel(self)
        self.textv.setObjectName(u"txtvopr")
        self.textv.setAlignment(alignmentc)
        if ynph==1:
            self.textv.setGeometry(QRect(100, hgt/2+20, wdt-200, hgt/2-40))
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
        self.textv.setFont(font)
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
        self.reset_button = QPushButton('Reset', self)          # 6
        self.reset_button.clicked.connect(self.reset_func)
        self.ss_button.setGeometry(10,hgt-65,100,30)
        self.reset_button.setGeometry(115,hgt-65,100,30)

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
 
    def reset_func(self):
            self.progressbar.reset()
            self.ss_button.setText('Start')
            self.timer.stop()
            self.step = 0
         
        
#Конец прогрессбара таймера

        

ques=wing(phyn,testtext*7)
ques.showFullScreen()


app.exec()
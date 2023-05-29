import sys
from PySide6.QtCore import Qt, QPoint, QTimer 
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient, QPixmap)
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QMessageBox

# забирать из базы данных
tkolt = 2
cenv = 30
tots = [0, 0, 0, 0, 0, 0]
name = ["Средняя общеобразовательная школа №1316", "Средняя общеобразовательная школа №753", "Центр образования №951",
        "СОШ №531", "Средняя общеобразовательная школа №764", "Средняя общеобразовательная школа №786"]
logo = ["1316.jpg", "", "753.jpg", "951.jpg", "531.jpg", "", ""]
blc=80
shag=2
smx=5
gx=200

#


class Wint(QWidget):
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



    def __init__(self, tkol, parent=None):
        super(Wint, self).__init__(parent)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        alignmentc = Qt.AlignmentFlag.AlignCenter
        tkol = tkolt
        snd = ""
        geometry = apt.primaryScreen().availableGeometry()
        self.setGeometry(geometry)
        wdt = self.size().width()
        twdt = (wdt - 20) / tkol - 10
        hgt = self.size().height()
        self.setAutoFillBackground(True)
        self.setStyleSheet("""
                background-color: #0000cc;
                color: #ddFFaa;
                font-family: Arial;
                """)
#Анимация фона        
        def scrupd():
            global blc, shag
            blc+=shag
            if blc>=254 or blc<=80:
                shag*= -1
            self.sth="background-color: rgba(0,0,"+str(blc)+",135); color: #ddFFaa;"
            self.setStyleSheet(self.sth)

        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(40)        
#конец анимации фона
        def cntn(self):
            apt.quit()

        for i in range(tkol):
            if len(logo[i]) > 0:
                self.logo = QLabel(self)
                self.logo.setGeometry(i * (twdt + 10) + 10, 10, twdt, hgt / 4 - 10)
                self.logo.setAlignment(alignmentc)
                pixmap = QPixmap("img/logo/" + logo[i])
                pixmap = pixmap.scaled(twdt, hgt / 4 - 20, Qt.KeepAspectRatio)
                self.logo.setPixmap(pixmap)
                self.logo.setStyleSheet("border:3px solid #bbaaff;border-top-left-radius: 22px; border-top-right-radius: 22px; font-size: 48px")
                self.logo.show()

            self.tnm = QLabel(self)
            fnts = 60 - tkolt * 5
            stsh = "border:3px solid #bbaaff;font-size: " + str(fnts) + "px"
            self.tnm.setStyleSheet(stsh)
            if len(logo[i]) > 0:
                self.tnm.setGeometry(i * (twdt + 10) + 10, 10 + hgt / 4, twdt, hgt / 3 - 20)
            else:
                self.tnm.setGeometry(i * (twdt + 10) + 10, 10, twdt, hgt / 3 + hgt / 4 - 20)
                self.tnm.setStyleSheet("border:3px solid #bbaaff;border-top-left-radius: 22px; border-top-right-radius: 22px;  font-size: "+str(fnts)+"px")
                
            self.tnm.setWordWrap(True)
            self.tnm.setText(name[i])
            self.tnm.setAlignment(alignmentc)
            self.tnm.setFont(font)

            self.tnm.show()

            self.result = QLabel(self)
            self.result.setObjectName("rst" + str(i))
            self.result.setGeometry(i * (twdt + 10) + 10, hgt / 4 + hgt / 3, twdt, hgt / 5)
            self.result.setWordWrap(True)
            self.result.setText(str(tots[i]))
            self.result.setAlignment(alignmentc)
            self.result.setFont(font)
            fnts1 = 96 - tkolt * 4
            stsh = "border:3px solid #bbaaff;border-bottom-left-radius: 22px; border-bottom-right-radius: 22px;font-size: " + str(fnts1) + "px"
            self.result.setStyleSheet(stsh)
            self.result.show()

            self.plusb = QPushButton(self)
            self.plusb.setObjectName("pls" + str(i))
            # QMessageBox.warning(self, "Нажматие!!!))", "Название объекта " + str(self.plusb.objectName()))
            self.plusb.setGeometry(i * (twdt + 10) + 10, hgt / 4 + hgt / 3 + hgt / 5 + 10, twdt / 2 - 2, hgt / 10)
            self.plusb.setText("+")
            self.plusb.setStyleSheet("font-size: " + str(fnts1) + "px; border: 1px")
            self.plusb.clicked.connect(self.sumf)
            self.plusb.show()

            self.minub = QPushButton(self)
            self.minub.setObjectName("mns" + str(i))
            self.minub.setGeometry(i * (twdt + 10) + 12 + twdt / 2, hgt / 4 + hgt / 3 + hgt / 5 + 10, twdt / 2 - 2,
                                   hgt / 10)
            self.minub.setText("-")
            self.minub.setStyleSheet("font-size: " + str(fnts1) + "px")
            self.minub.clicked.connect(self.sumf)
            self.minub.show()

        self.contin = QPushButton(self)
        self.contin.setGeometry(10, hgt - hgt / 15 - 10, wdt - 20,
                                hgt / 15)
        self.contin.setText(">>>")
        self.contin.setStyleSheet("font-size: 60px; border-top-right-radius: 120px 60px; border-bottom-left-radius: 120px 60px")
        self.contin.clicked.connect(cntn)
        self.contin.show()

    def sumf(self):
        sndr = self.sender().objectName()
        # QMessageBox.warning(self, "Нажматие!!!))", " " + str(self.sender().objectName()))
        if sndr[:3] == "pls":
            tots[int(sndr[3:])] += cenv
        else:
            tots[int(sndr[3:])] -= cenv
        # меняем значения на лейблах
        obj = self.findChild(QLabel, "rst" + sndr[3:])
        obj.setText(str(tots[int(sndr[3:])]))


apt = QApplication([])
wnt = Wint(tkolt)
#    wnt.setStyleSheet('background: black')
wnt.showFullScreen()
apt.exec()
#sys.exit(apt.exec())

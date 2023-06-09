import logging
import sys
#import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, QPoint, QTimer, QEvent
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient, QPixmap)
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QDialog, \
    QVBoxLayout, QButtonGroup, QHBoxLayout
from PySide6.QtSql import QSqlDatabase, QSqlQuery

import widget
from categ import Category
from widget import wnd, cenv

global apt
#база данных
#global sqlDB
QtCore.QLocale.setDefault(QtCore.QLocale("ru_RU"))
# sqlDB = QSqlDatabase.addDatabase('QSQLITE')
# sqlDB.setDatabaseName('jep.sqlite')
# sqlDB.open()
name=["","","","","","","",""]
logo=["","","","","","","",""]
lcnnxt=30
query = QSqlQuery()
if not query.exec(
        """
            SELECT COUNT(*) FROM Teams;
        """
):
        logging.error("Failed to query database")
query.next()
tkolt=int(query.value(0)) # количество команд

query = QSqlQuery()
if not query.exec(
        """
            SELECT * FROM Teams;
        """
):
        logging.error("Failed to query database")
query.first()

s=""
for i in range(tkolt):
    logo[i]=str(query.value(1))
    name[i]=str(query.value(2))
    s+=name[i]+" "
    query.next()
#вычисляем кол-во букв в самом длинном слове в названиях команд
maxlenw= max(s.split(), key=len)
lmaxlw=len(maxlenw)


mascat = []
tots = [0, 0, 0, 0, 0, 0]

blc=120
shag=2
smx=5
gx=200
cnttxt=""
global geometry

cenv=0

class Wint(QWidget):
    global cnttxt, cntcode
    # забираем название категории из settings


    # query = QSqlQuery()
    # if not query.exec(
    #         """
    #             SELECT * FROM settings;
    #         """
    # ):
    #     logging.error("Failed to query database")
    # query.first()
    # cnttxt = query.value(8) + "  >>>"

    # рисуем анимацию фона
    global cenv
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
        gradient.setColorAt(0.0, QColor(0, 0, 80, 180))
        gradient.setColorAt(0.3, QColor(0, 120, 255, 225))
        gradient.setColorAt(1.0, QColor(0, 80, 255, 80))
        painter.setBrush(gradient)

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor(0, 0, 50, 10))
        painter.setPen(pen)
        painter.drawRect(x, y, wd, hd)
    # закончили с фоном
        query = QSqlQuery()
        if not query.exec(
                """
                    SELECT * FROM settings;
                """
        ):
            logging.error("Failed to query database")
        query.first()
        cnttxt = query.value(8) + "  >>>"
        self.contin.setText(cnttxt)

    def __init__(self, tkol, parent=None):
        global lmaxlw
        sqlDB = QSqlDatabase.addDatabase('QSQLITE')
        sqlDB.setDatabaseName('jep.sqlite')
        sqlDB.open()
        super(Wint, self).__init__(parent)
        #super().__init__()
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
        fw=int(twdt/lmaxlw)
        hgt = self.size().height()
        self.setAutoFillBackground(True)
        # self.setStyleSheet("""
        #         background-color: #0000cc;
        #         color: #ddFFaa;
        #         font-family: Arial;
        #         """)
#Насыщенность фона        
        def scrupd():
            global blc, shag
            blc+=shag
            if blc>=254 or blc<=90:
                shag*= -1
            self.sth="background-color: rgba(0,0,"+str(blc)+",75); color: #ddFFaa;"
            self.setStyleSheet(self.sth)

        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(40)        
#конец насыщенности фона

#создаем экраны вопросов категорий
        query = QSqlQuery()
        if not query.exec(
                """
                 SELECT COUNT(*) FROM Category;
                 """
        ):
            logging.error("Failed to query database")
        query.next()

        for i in range(int(query.value(0))):
            global mascat

            # создаем виджет - один навсегда))
            cwnd = wnd(i+1,apt)
            cwnd.setVisible(False)
            cwnd.setObjectName("widget_"+str(i))
            mascat.append(cwnd)

 # конец init

        #ПРОДОЛЖИТЬ

        def cntn():
            global cntcode
            # забираем название категории из settings
            query = QSqlQuery()
            if not query.exec(
                    """
                        SELECT * FROM settings;
                    """
            ):
                logging.error("Failed to query database")
            query.first()
            cntcode = int(query.value(7)) - 1
            mascat[cntcode].showFullScreen()

        def chcat(self):
            global cnttxt, cntcode, lcnnxt

            vcat=Category(apt)
            vcat.showFullScreen()
            query = QSqlQuery()
            if not query.exec(
                    """
                        SELECT * FROM settings;
                    """
            ):
                logging.error("Failed to query database")
            query.first()
            cnttxt = query.value(8) + "  >>>"
            lcnnxt=len(cnttxt)
            cntcode = int(query.value(7)) - 1

        for i in range(tkol):
            if len(logo[i]) > 0:
                self.logo = QLabel(self)
                self.logo.setGeometry(i * (twdt + 10) + 10, 10, twdt, hgt / 4 - 10)
                self.logo.setAlignment(alignmentc)
                pixmap = QPixmap("img/logo/" + logo[i])
                pixmap = pixmap.scaled(twdt, hgt / 4 - 20, Qt.KeepAspectRatio)
                self.logo.setPixmap(pixmap)
                self.logo.setStyleSheet("border:3px solid #99aaff;border-top-left-radius: 22px; border-top-right-radius: 22px; font-size: 48px")
                self.logo.show()

            self.tnm = QLabel(self)
            #fnts = 66 - tkolt * 7
            fnts=int(fw*1.5)
            stsh = "border:3px solid #99aaff;font-size: " + str(fnts) + "px"
            self.tnm.setStyleSheet(stsh)
            if len(logo[i]) > 0:
                self.tnm.setGeometry(i * (twdt + 10) + 10, 10 + hgt / 4, twdt, hgt / 3 - 20)
            else:
                self.tnm.setGeometry(i * (twdt + 10) + 10, 10, twdt, hgt / 3 + hgt / 4 - 20)
                self.tnm.setStyleSheet("border:3px solid #9999ff;border-top-left-radius: 22px; border-top-right-radius: 22px;  font-size: "+str(fnts)+"px")
                
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
            stsh = "border:3px solid #99aaff;border-bottom-left-radius: 22px; border-bottom-right-radius: 22px;font-size: " + str(fnts1) + "px"
            botb = "QPushButton{font-size: " + str(fnts1) + "px; border: 1px solid rgba(200,200,255,180)} QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
            self.result.setStyleSheet(stsh)
            self.result.show()

            self.plusb = QPushButton(self)
            self.plusb.setObjectName("pls" + str(i))
            # QMessageBox.warning(self, "Нажматие!!!))", "Название объекта " + str(self.plusb.objectName()))
            self.plusb.setGeometry(i * (twdt + 10) + 10, hgt / 4 + hgt / 3 + hgt / 5 + 10, twdt / 2 - 2, hgt / 10)
            self.plusb.setText("+")
            self.plusb.setStyleSheet(botb)
            self.plusb.clicked.connect(self.sumf)
            self.plusb.show()

            self.minub = QPushButton(self)
            self.minub.setObjectName("mns" + str(i))
            self.minub.setGeometry(i * (twdt + 10) + 12 + twdt / 2, hgt / 4 + hgt / 3 + hgt / 5 + 10, twdt / 2 - 2,
                                   hgt / 10)
            self.minub.setText("-")
            self.minub.setStyleSheet(botb)
            self.minub.clicked.connect(self.sumf)
            self.minub.show()


        self.catch = QPushButton(self)
        self.catch.setGeometry(10, hgt - hgt / 15 - 10, (wdt - 25)/2,
                                hgt / 15)
        fs = int(1.5 * (((wdt - 25) / 2) / (lcnnxt + 2)))
        self.catch.setText("Выбор категории")
#        self.catch.setStyleSheet("font: bold 34px; border: 1px solid rgba(200,200,255,180); border-top-right-radius: 120px 60px; border-bottom-left-radius: 180px "+str(int(hgt / 15))+"px")
        shst="QPushButton { font: bold "+str(fs)+"px; border: 1px solid rgba(200,200,255,180); border-top-right-radius: 120px 60px; border-bottom-left-radius: 180px "+str(int(hgt / 15))+"px} QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
        self.catch.setStyleSheet(shst)
        self.catch.clicked.connect(chcat)
        self.catch.show()


        self.contin = QPushButton(self)
        self.contin.setGeometry((wdt - 20)/2, hgt - hgt / 15 - 10, (wdt - 25)/2, hgt / 15)
        self.contin.setText(cnttxt)


        self.contin.setStyleSheet("QPushButton {font: bold "+str(fs)+"px; border: 1px solid rgba(200,200,255,180);border-top-right-radius: 180px "+str(int(hgt / 15))+"px; border-bottom-left-radius: 120px 60px} QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }")
        self.contin.clicked.connect(cntn)
        self.contin.show()




    def sumf(self):
        # считываем цену вопроса из tmpDat settings
        quec = QSqlQuery()
        if not quec.exec(
                """
                 SELECT * from settings;
                 """
        ):
            logging.error("Failed to query database")
        quec.next()
        cenv = quec.value(5)
        cenp = quec.value(6)

        sndr = self.sender().objectName()
        # QMessageBox.warning(self, "Нажматие!!!))", " " + str(self.sender().objectName()))
        if sndr[:3] == "pls":
            tots[int(sndr[3:])] += cenp
        else:
            tots[int(sndr[3:])] -= cenv
        # меняем значения на лейблах
        obj = self.findChild(QLabel, "rst" + sndr[3:])
        obj.setText(str(tots[int(sndr[3:])]))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            # диалоговое окно выхода из программы
            def check_button(id_name):
                if button_group.id(id_name) == 1:
                    reply.close()
                    self.close()
                elif button_group.id(id_name) == 2:
                    reply.close()
                    event.ignore()

            reply = QDialog()
            reply.setWindowFlag(Qt.FramelessWindowHint)
            sth = "background-color: rgba(0,0,255,90); color: #ddFFaa; font-size: 22px;  border: 6px;"
            reply.setStyleSheet(sth)
            vbox = QVBoxLayout()
            label_dialog = QLabel()
            label_dialog.setStyleSheet("background-color: rgba(0,0,255,240);border-top-left-radius: 80px 20px; border-bottom-right-radius: 80px 20px;")
            label_dialog.setText('Вы действительно хотите закончить игру?')
            button_yes = QPushButton(reply)
            button_yes.setText("Да")
            shst = "QPushButton { background-color: rgba(0,0,200,100); color: rgba(220,220,255,255); text-align:center center; background-position: bottom center; border: 2px solid rgb(160, 180, 250); border-radius: 6px; font: Bold 22px} QPushButton::hover{background-color: #0077ff ;}"
            button_yes.setStyleSheet(shst)
            button_no = QPushButton(reply)
            button_no.setText('Нет')
            button_no.setStyleSheet(shst)
            button_group = QButtonGroup()
            button_group.addButton(button_yes, 1)
            button_group.addButton(button_no, 2)
            button_group.buttonClicked.connect(check_button)
            layout = QHBoxLayout()
            layout.addWidget(button_yes)
            layout.addWidget(button_no)
            vbox.addWidget(label_dialog)
            vbox.addSpacing(20)
            vbox.addLayout(layout)
            reply.setLayout(vbox)
            reply.exec()

if __name__ == "__main__":
    apt = QApplication([])
    wnt = Wint(tkolt)
    wnt.showFullScreen()
    sys.exit(apt.exec())
    sqlDB.close()
    sqlDB.removeDatabase('QSQLITE')
    sqlDB.removeDatabase('jep.sqlite')


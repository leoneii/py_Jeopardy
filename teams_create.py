import os
import shutil
import sys
# import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, QPoint, QTimer, QEvent, QSize
from PySide6.QtGui import (QColor, QMouseEvent, QFont, QPalette, QPainter, QPen, QLinearGradient, QPixmap, QIcon)
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QDialog, \
    QVBoxLayout, QButtonGroup, QHBoxLayout, QSpinBox, QInputDialog, QMessageBox, QFileDialog, QStyle
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import simpleaudio as simple_audio
#from pyqt6_plugins.examplebuttonplugin import QtGui

blc = 120
shag = 2
smx = 5
gx = 200
wdl=1
kolteam=2
comname = ["Команда 1", "Команда 2", "Команда 3", "Команда 4", "Команда 5", "Команда 6", "Команда 7"]
teamlogo = ["", "", "", "", "", "", ""]

class Winteamcr(QWidget):
    global comname, teamlogo
# Анимация фона экрана
    def paintEvent(self, event):
        global smx,blc,shag
        global gx, wd, hd

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
   
    def __init__(self, parent=None):
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)

        global gwidth, gheight,wdl, kolteam
        (gwidth, gheight) = apt.screens()[0].size().toTuple()
        super(Winteamcr, self).__init__(parent)
        wd=gwidth
        hd=gheight
#запускаем анимацию фона
        def scrupd():
                self.blc+=self.shag
                if self.blc>=254 or self.blc<=60:
                    self.shag*= -1
                self.sth="background-color: rgba(0,0,255,"+str(self.blc)+"); color: #ddFFFF;"
                self.setStyleSheet(self.sth)
# Эффект раскрытия объектов
        def objupd():

                if self.wdl<wd/3:
                    self.wdl+=10
                    self.titlabel.setGeometry(wd/2-wd/6,40,self.wdl,80)
                else:
                    self.wdl=wd/3
                    if self.badd<self.wdl/2-5:
                        self.badd+=10
                        self.butAddTeam.setGeometry(wd/2-wd/6,125,self.badd,40)
                    else:
                        self.badd=self.wdl/2-5
                        if self.spwt<self.wdl/2-10:
                            self.spwt+=10
                            self.spinTeamCount.setGeometry(wd / 2 + 10, 125, self.spwt, 40)
                        else:
                            self.spwt=self.wdl/2-10
                            while self.hdn < hd - 165 -hd/8:
                                self.hdn += 1
                                for i in range(kolteam):
                                    x = 40 + i * (wd - 80) / kolteam
                                    wdnl = (wd - 80) / kolteam - 10
                                    y = 180
                                    self.labi = self.findChild(QLabel,u"labtmname"+str(i))
                                    self.labi.setGeometry(x, y, wdnl, self.hdn)
                                    self.bnam=self.findChild(QPushButton,u"butname" + str(i))
                                    self.bnam.setGeometry(5, int(self.hdn / 3 + 5),
                                                             int(self.lab_teamName.width() - 5),
                                                             int(self.hdn / 1.5 - 10))
                                    self.blog = self.findChild(QPushButton, u"butlogo" + str(i))
                                    self.blog.setGeometry(5, 5,
                                                             int(self.lab_teamName.width() - 5),
                                                             int(self.hdn / 3 - 5))
                                    twdt = (wd - 20) / kolteam - 10
                                    fw = int(twdt / len("Логотип команды " + str(i + 1)))

                                    self.blog.setText("Логотип")
                                    stshbn = "QPushButton{font-size: " + str(
                                        int(fw)) + "px; border-radius: 10px; border: 1px solid rgba(200,200,255,180); background-color: rgba(0,0,200,50); color: rgba(0,100,255,100)} QPushButton::hover{background-color: #0077ff ; color: rgba(0,200,255,200)} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
                                    self.blog.setStyleSheet(stshbn)


                                    self.contin.setVisible(True)
                                    self.tmrscrobj.stop()


        # таймер фона
        self.blc = 80
        self.shag=1
        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(scrupd)
        self.tmr.start(40)

#таймер элементов экрана
        self.tmrscrobj=QTimer()
        self.tmrscrobj.timeout.connect(objupd)
        self.tmrscrobj.start(20)

# Label заголовка экрана
        self.titlabel=QLabel(self)
        self.titlabel.setText("Регистрация команд")
        self.titlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wdl=20
        fw = int((wd/3) / len(self.titlabel.text()))
        fnts = int(fw * (1.4-0.2*(1-kfont)))
        if fnts>60:
            fnts=60
        self.titlabel.setFont(font)
        stsh = "border:0px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,200,40); font-size: " + str(fnts) + "px"
        self.titlabel.setStyleSheet(stsh)

# кнопка изменения количества команд
        def changeTeamCount():
            if self.butAddTeam.text()=="Изменить количество":
                self.butAddTeam.setText("Подтвердить количество")
# не понятно, не отключается
                for i in range(7):
                    self.labi = self.findChild(QLabel, u"labtmname" + str(i))
                    self.labi.setVisible(False)

                self.spinTeamCount.setEnabled(True)
                spstsh = "QSpinBox{border:3px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,20,130); font-size: " + str(
                    int(fnts * 0.7)) + "px}"
                self.spinTeamCount.setStyleSheet(spstsh)
                self.spinTeamCount.setFocus()
            else:

                self.butAddTeam.setText("Изменить количество")
                spstsh = "QSpinBox{border:1px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,200,30); font-size: " + str(
                    int(fnts * 0.7)) + "px}"
                self.spinTeamCount.setStyleSheet(spstsh)
                self.spinTeamCount.setEnabled(False)
                kolteam=self.spinTeamCount.value()
                mod_chang_team_name(kolteam)
                self.hdn = hd - 165 -hd/8
                for j in range(7):
                    self.labi = self.findChild(QLabel, u"labtmname" + str(j))
                    self.labi.setVisible(False)
                for i in range(kolteam):
                    x = 40 + i * (wd - 80) / kolteam
                    wdnl = (wd - 80) / kolteam - 10
                    y = 180
                    self.labi = self.findChild(QLabel, u"labtmname" + str(i))
                    self.labi.setVisible(True)
                    self.labi.setGeometry(x, y, wdnl, self.hdn)
                    self.bnam = self.findChild(QPushButton, u"butname" + str(i))
                    self.bnam.setGeometry(5, int(self.hdn / 3 + 5),
                                          int(self.lab_teamName.width() - 5),
                                          int(self.hdn / 1.5 - 10))
                    self.blog = self.findChild(QPushButton, u"butlogo" + str(i))
                    self.blog.setGeometry(5, 5,
                                          int(self.lab_teamName.width() - 5),
                                          int(self.hdn / 3 - 5))
                    twdt = (wd - 20) / kolteam - 10
                    fw = int(twdt / len("Логотип команды " + str(i + 1)))
                    stshbn = "QPushButton{font-size: " + str(
                        int(fw)) + "px; border-radius: 10px; border: 1px solid rgba(200,200,255,180); background-color: rgba(0,0,200,50); color: rgba(0,100,255,100)} QPushButton::hover{background-color: #0077ff ; color: rgba(0,200,255,200)} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
                    self.blog.setStyleSheet(stshbn)
                    self.upLogo(i)

        self.badd=0
        self.butAddTeam=QPushButton(self)
        self.butAddTeam.setText("Изменить количество")
        self.butAddTeam.setGeometry(wd / 2 - wd / 6-5, 125, self.badd, 40)
        botb = "QPushButton{font-size: " +  str(int(fnts*0.5)) + "px; border-radius: 10px; border: 1px solid rgba(200,200,255,180); background-color: rgba(0,0,200,30)} QPushButton::hover{background-color: rgba(0, 155, 255, 195);} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
        self.butAddTeam.setStyleSheet(botb)
        self.butAddTeam.clicked.connect(changeTeamCount)
# Спинер изменения количества команд
        self.spwt=0
        self.spinTeamCount=QSpinBox(self)
        self.spinTeamCount.setGeometry(wd / 2 +5, 125, self.spwt, 40)
        spstsh = "QSpinBox{border:1px solid #99aaff; border-radius: 10px; background-color: rgba(0,0,200,30); font-size: " + str(int(fnts*0.7)) + "px}"
        self.spinTeamCount.setStyleSheet(spstsh)
        self.spinTeamCount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinTeamCount.setFont(font)
        self.spinTeamCount.setMinimum(2)
        self.spinTeamCount.setMaximum(7)
        self.spinTeamCount.setEnabled(False)
        #self.spinTeamCount.show()

# Модуль изменения наименования команд и их логотипов
        def mod_chang_team_name(tc):
            stshteamname = "border:0px solid #99aaff; border-radius: 20px; background-color: rgba(40,60,150,120); font-size: " + str(
                fnts) + "px"
            #self.hdn=hd - hd/3.5
            self.hdn = 0
            for i in range(tc):
                self.lab_teamName = QLabel(self)
                self.lab_teamName.setObjectName(u"labtmname"+str(i))
                self.lab_teamName.setWordWrap(True)
                self.lab_teamName.setText(comname[i])
                self.lab_teamName.setFont(font)
                self.lab_teamName.setStyleSheet(stshteamname)
                x=40+i*(wd-80)/tc
                wdnl=(wd-80)/tc-15
                y=180
                self.lab_teamName.setGeometry(x,y,wdnl,self.hdn)
                self.lab_teamName.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.butname=QPushButton(self.lab_teamName)
                self.butname.setObjectName(u"butname" + str(i))
                self.butname.setFont(font)

                stshbn = "QPushButton{font-size: " +  str(int(fnts)) + "px; border-radius: 10px; border: 1px solid rgba(200,200,255,180); background-color: rgba(0,0,200,50)} QPushButton::hover{background-color: rgba(0,120,255,100) ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
                self.butname.setStyleSheet(stshbn)
                self.butname.setGeometry(5,int(self.lab_teamName.height()/3+5),int(self.lab_teamName.width()-10),int(self.lab_teamName.height()/1.5-15))
                self.butname.installEventFilter(self)


                self.butlogo = QPushButton(self.lab_teamName)
                self.butlogo.setObjectName(u"butlogo" + str(i))
                self.butlogo.setFont(font)
                self.butlogo.installEventFilter(self)
                twdt = (wd - 20) / tc - 10
                fw = int(twdt / len("Логотип команды " + str(i + 1)))
                if len(teamlogo[i])==0:
                    self.butlogo.setText("Логотип")
                else:
                    self.butlogo.setText("")
                stshbn = "QPushButton{font-size: " + str(int(fw)) + "px; border-radius: 10px; border: 1px solid rgba(200,200,255,180); background-color: rgba(0,0,200,50); color: rgba(0,100,255,100)} QPushButton::hover{background-color: #0077ff ; color: rgba(0,200,255,200)} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,255) }"
                self.butlogo.setStyleSheet(stshbn)
                self.butlogo.setGeometry(5, 5,
                                         int(self.lab_teamName.width() - 10),
                                         int(self.lab_teamName.height() / 3 - 10))

                self.dellogo=QPushButton(self.butlogo)
                self.dellogo.setObjectName(u"delog"+str(i))
                xd = self.butlogo.width() * 5 / 6 - 5
                yd = self.butlogo.height() * 4 / 5 - 5
                wdd = self.butlogo.width() / 6
                hdd = self.butlogo.height() / 5
                self.dellogo.setGeometry(xd, yd, wdd, hdd)
                self.dellogo.setText("X")
                self.dellogo.installEventFilter(self)

                if len(teamlogo[i])==0:
                    self.dellogo.setVisible(False)
                else:
                    self.dellogo.setVisible(True)


        mod_chang_team_name(7)
        mod_chang_team_name(kolteam)

        self.contin = QPushButton(self)
        tmh=int(hd / 15 -10)
        self.contin.setGeometry(wd *3/ 4 -60, hd - hd / 15-20, (wd - 20) / 4, tmh )
        self.contin.setText("К игре")
        self.contin.setStyleSheet("QPushButton { background-color: rgba(0,0,180,50) ; font: bold " + str(
            fw) + "px; border: 1px solid rgba(200,200,255,180);border-top-right-radius: "+str(tmh*2)+"px "+str(tmh)+"px; border-bottom-left-radius: "+str(tmh*2)+"px "+str(tmh)+"px} QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,180) }")
        #self.contin.clicked.connect(cntn)
        self.contin.setVisible(False)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
                mouse_event = QMouseEvent(event)
                if mouse_event.buttons() == Qt.LeftButton:
                    if (obj.objectName()[3])== "l": #добавление лого
                        self.enterLogoPath(int(obj.objectName()[7]))
                        self.upLogo(int(obj.objectName()[7]))
                        return True     
                    
                    elif (obj.objectName()[3])== "o": #удаление лого
                        self.clearLogoPath(int(obj.objectName()[5]))
                        return True
                    
                    elif(obj.objectName()[3])== "n": #имя команды
                        self.enterName(int(obj.objectName()[7]))
                        self.labi1 = self.findChild(QLabel, u"labtmname" + str(int(obj.objectName()[7])))
                        self.labi1.setText(comname[int(obj.objectName()[7])])
                        self.upLogo(int(obj.objectName()[7]))
                        return True

        return super(Winteamcr, self).eventFilter(obj, event)
    
    def upLogo(self,numTeam):
        self.blog1 = self.findChild(QPushButton, u"butlogo" + str(numTeam))
        self.blogd1 = self.findChild(QPushButton, u"delog" + str(numTeam))
        if len(teamlogo[numTeam])==0:
            self.blog1.setText("Логотип ")
            self.blog1.setIcon(QIcon(""))
            if len(teamlogo[numTeam]) > 0:
                self.blogd1.setVisible(True)
            else:
                self.blogd1.setVisible(False)
        else:
            self.blog1.setIcon(QIcon("./img/logo/" + teamlogo[numTeam]))
            self.blog1.setIconSize((QSize(self.blog1.width()/1.3, self.blog1.height()/1.3)))
            self.blog1.setText("")
            self.blogd1 = self.findChild(QPushButton, u"delog" + str(numTeam))
            xd = self.blog1.width() * 5 / 6 - 5
            yd = self.blog1.height() * 4 / 5 - 5
            wdd = self.blog1.width() / 6
            hdd = self.blog1.height() / 5
            self.blogd1.setGeometry(xd, yd, wdd, hdd)
            if len(teamlogo[numTeam]) > 0:
                self.blogd1.setVisible(True)
            else:
                self.blogd1.setVisible(False)

    def clearLogoPath(self,numTeam):
        dlg = QMessageBox()
        dlg.setStyleSheet(
            " QWidget{ background-color: rgba(0,100,220,190); font: bold 18px; color: rgba(255,255,255,255);} QPushButton::Hover{background-color: rgba(0,180,240,150);} QPushButton::Pressed{background-color: rgba(0,200,250,100);}")
        dlg.setWindowTitle("Удаление логотипа!!!")
        dlg.setText("Уверены, что логотип необходимо удалить?")
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # dlg.setButtonText(QMessageBox.Ok, "Да")
        # dlg.setButtonText(QMessageBox.Cancel, "Нет, отказаться")
        buttonY = dlg.button(QMessageBox.Ok)
        buttonY.setText('Да')
        buttonN = dlg.button(QMessageBox.Cancel)
        buttonN.setText('Нет, отказаться')
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Ok:
            teamlogo[numTeam] = ""
            self.upLogo(numTeam)
            return True
        if button == QMessageBox.Cancel:
            return False
    def enterName(self,numTeam):
        dialog = QInputDialog()
        dialog.setStyleSheet("QPushButton { background-color: rgba(0,0,180,50) ; font: bold 14px; border: 1px solid rgba(200,200,255,180);border-top-right-radius: 40px 10px; border-bottom-left-radius: 40px 10px} QPushButton::hover{background-color: #0077ff ;} QPushButton::pressed {background-color: rgba(224, 255, 255, 195); color: rgba(0,0,255,180) } QWidget{ background-color: rgba(0,100,220,190); font: bold 18px; color: rgba(255,255,255,210);} QLineEdit{background-color: rgba(0,20,120,220); color: rgba(255,255,255,255); font: bold 18px}")
        dialog.setGeometry(gwidth/2-gwidth/6,gheight/2-gheight/10,gwidth/3,gheight/5)
        dialog.setWindowTitle("Изменяем наименование "+comname[numTeam])
        dialog.setOkButtonText("Сохранить изменение")
        dialog.setCancelButtonText("Отказаться")
        dialog.setLabelText('Текущее наименование "'+comname[numTeam]+'" изменяем на:')
        dialog.setTextValue(comname[numTeam])
        dialog.setInputMode(QInputDialog.TextInput)
        ok = dialog.exec()

        if ok:
            newName = dialog.textValue()
            if len(newName)>0:
                comname[numTeam]=str(newName)
            else:
                mesbox=QMessageBox()
                mesbox.setWindowTitle("Внимание!")
                mesbox.setStyleSheet(" QWidget{ background-color: rgba(0,100,220,190); font: bold 18px; color: rgba(255,255,255,255);}")
                mesbox.setText("Наименование команды не может быть пустым.\nВведите корректное наименование.")
                mesbox.exec()

    def enterLogoPath(self,numTeam):
        dialogL = QFileDialog()
        ofileName, filetype = dialogL.getOpenFileName(self, "Выберите изображение",  "",  "Images (*.jpeg *.jpg *.png)")
        fileName = os.path.basename(ofileName)
        if len(ofileName)>0:
            teamlogo[numTeam]=str(fileName)
            if "/img/logo/" in ofileName:
                pass
            else:
                shutil.copy2(ofileName,"./img/logo/"+fileName)

        return True

if __name__ == "__main__":
    global gwidth,gheight,kfont
    apt = QApplication([])
    (gwidth, gheight) = apt.screens()[0].size().toTuple()
    kfont=gwidth/1920
    wteamcr = Winteamcr()
    wteamcr.showFullScreen()
    sys.exit(apt.exec())
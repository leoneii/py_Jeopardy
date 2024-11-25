# This Python file uses the following encoding: utf-8
import logging
import os
import sys
import shutil
import datetime


from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

from PySide6.QtWidgets import QApplication, QInputDialog, QMainWindow, QMessageBox, QFileDialog, QDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime
import simpleaudio as simple_audio
from PySide6.QtWidgets import QSplashScreen

from mainwindow import Ui_MainWindow
from newDialog import *

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        sqlDB = QSqlDatabase.addDatabase('QSQLITE')
        sqlDB.setDatabaseName("../jep.sqlite")
        sqlDB.open()
        self.ui.setupUi(self)
        self.ui.pushButton_Save.setVisible(False)
        self.ui.pushButton_Cancel.setVisible(False)
        self.ui.pushButton_addCat.clicked.connect(self.addCat)
        self.ui.pushButton_EditCat.clicked.connect(self.editCat)
        self.ui.pushButton__delCat.clicked.connect(self.delCat)
        self.ui.comboBox_Cat.currentIndexChanged.connect(self.catChange)
        self.ui.pushButton_addTheme.clicked.connect(self.addTheme)
        self.ui.pushButton_editTheme.clicked.connect(self.editTheme)
        self.ui.pushButton_delTheme.clicked.connect(self.delTheme)
        self.ui.pushButton_editTeam.clicked.connect(self.changeTeam)
        self.ui.pushButton_delTeam.clicked.connect(self.delTeam)
        self.ui.pushButton_addTeam.clicked.connect(self.addTeam)
        self.ui.pushButton_editQ.clicked.connect(self.EditQ)
        self.ui.pushButton_Save.clicked.connect(self.SaveQ)
        self.ui.pushButton_Cancel.clicked.connect(self.CancelQ)
        self.ui.pushButton_Qup.clicked.connect(self.Qup)
        self.ui.pushButton_Qdown.clicked.connect(self.Qdown)
        self.ui.toolButton_selQpix.clicked.connect(self.selQpix)
        self.ui.toolButton_delQpix.clicked.connect(self.delQpix)
        self.ui.toolButton_selApix.clicked.connect(self.selApix)
        self.ui.toolButton_delApix.clicked.connect(self.delApix)        
        self.ui.toolButton_selTpix.clicked.connect(self.selTpix)
        self.ui.toolButton_delTpix.clicked.connect(self.delTpix)  
        self.ui.pushButton_delQ.clicked.connect(self.delQ)  
        self.ui.pushButton_addQ.clicked.connect(self.addQ)  
        self.ui.action_saveGame.triggered.connect(self.saveGame) 
        self.ui.action_newGame.triggered.connect(self.newGame)    
        self.ui.action_openGame.triggered.connect(self.openGame)  
        self.ui.testButton.clicked.connect(self.testB)
        self.ui.pushButton_addTeamLogo.clicked.connect(self.addTeamLogo)
        self.ui.pushButton_delTeamLogo.clicked.connect(self.delTeamLogo)
        self.ui.pushButton_addFinLogo.clicked.connect(self.addFinLogo)
        self.ui.pushButton_delFinLogo.clicked.connect(self.delFinLogo)
        self.ui.selectFinSound.clicked.connect(self.selectFinSound)
        self.ui.delFinSound.clicked.connect(self.delFinSound)
        self.ui.playFinSound.clicked.connect(self.playFinSound)
        self.ui.pushButton_selMusic.clicked.connect(self.selMusic)
        self.ui.commandLinkButton_Play.clicked.connect(self.playMusic)
        self.ui.pushButton_delMusic.clicked.connect(self.delQMusic)

        self.ui.pushButton_tipSelMusic.clicked.connect(self.tipSelMusic)
        self.ui.commandLinkButton_tipPlay.clicked.connect(self.tipPlayMusic)
        self.ui.pushButton_tipDelMusic.clicked.connect(self.tipDelMusic)


        self.ui.testButton.setVisible(False)
        self.ui.spinBox_costQuest.setVisible(False)
        self.textQpix = ""
        self.textApix = ""
        self.textTpix = ""
                #временный костыль, или постоянный костыль
        qAddField = QSqlQuery("ALTER TABLE ThemeAndQ ADD COLUMN MMF TEXT;")
        qAddField.exec()
        qAddField = QSqlQuery("ALTER TABLE ThemeAndQ ADD COLUMN TMMF TEXT;")
        qAddField.exec()

        self.EditMode(False)
        self.updateform()
        self.selector(0,0)
        self.player = QMediaPlayer()
        self.tmr = QTimer()  # 4
        self.tmr.timeout.connect(self.medendfile)

        homed = os.path.expanduser("~")
        global homedir 
        homedir = homed

        self.backup()

        if os.path.exists("../disanim"):
            self.ui.checkBox_disanim.setChecked(True)
        else:
            self.ui.checkBox_disanim.setChecked(False)
        self.ui.checkBox_disanim.toggled.connect(self.togAnim)

    def backup(self):
        # arh = ZipFile("popa.zip","w", compression=ZIP_DEFLATED, compresslevel=3)
        # arh.("/home/leone/test/*.*")
        # print(arh.infolist())
        #ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=6, *, strict_timestamps=True, metadata_encoding=None)
        currdate= datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
        try:
            shutil.make_archive( homedir+'/_strteam_arh/'+'arh'+currdate, 'zip', '../games/')
        except:
            print("Внимание!!! ошибка архивации")


    def medendfile(self):
        if str(self.player.mediaStatus()) == "MediaStatus.EndOfMedia":
            self.ui.playFinSound.setText("Прослушать")
            icon = QIcon()
            icon.addFile(u"../img/icon/mplay.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.commandLinkButton_tipPlay.setIcon(icon)
            self.ui.commandLinkButton_Play.setIcon(icon)
            self.tmr.stop()
    def tipDelMusic(self):
        dialog = QMessageBox()
        dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
        dialog.setWindowTitle("Внимание!")
        dialog.setDefaultButton(QMessageBox.Cancel)
        dialog.setButtonText(QMessageBox.Save, "Удалить музыкальную подсказку")
        dialog.setButtonText(QMessageBox.Cancel, "Не изменять")
        dialog.setInformativeText("Вы действительно хотите удалить музыкальную подсказку?")
        dialog.setIcon(QMessageBox.Icon.Critical)
        ok = dialog.exec()
        if ok == QMessageBox.Save:
            indexT = self.ui.tableView_themeTable.currentIndex()
            indexQ = self.ui.tableView_questTable.currentIndex()
            costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
            model = self.ui.tableView_themeTable.model()
            query = QSqlQuery(
                "UPDATE ThemeAndQ SET TMMF = NULL WHERE Cost = '" + costq + "' AND Theme = '" + str(
                    model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                        0)) + "';")
            query.exec()
            self.ui.lineEdit_tipMusicFile.setText("")
            self.selector(indexT.row(), indexQ.row())


    def tipPlayMusic(self):
        self.tmr.start()
        if self.player.isPlaying():
            self.player.stop()
            icon = QIcon()
            icon.addFile(u"../img/icon/mplay.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.commandLinkButton_tipPlay.setIcon(icon)
        else:
            self.audioOutput = QAudioOutput()
            self.player.setAudioOutput(self.audioOutput)
            self.player.setSource(QUrl.fromLocalFile('../media/' + self.ui.lineEdit_tipMusicFile.text()))
            self.player.play()
            icon = QIcon()
            icon.addFile(u"../img/icon/mstop.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.commandLinkButton_tipPlay.setIcon(icon)

    def tipSelMusic(self):
        indexT = self.ui.tableView_themeTable.currentIndex()
        indexQ = self.ui.tableView_questTable.currentIndex()
        ofileName, filetype = QFileDialog.getOpenFileName(
            self,
            "Выберите музыкальный файл",
            "",
            "Media (*.wav *.mp3 )"
        )
        fileName = os.path.basename(ofileName)

        if len(ofileName) > 0:
            try:
                self.ui.commandLinkButton_tipPlay.setEnabled(True)
                shutil.copy2(ofileName, "../media/" + fileName)
            except:
                print("апшипка tipSelMusic")
            costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
            model = self.ui.tableView_themeTable.model()
            query = QSqlQuery(
                "UPDATE ThemeAndQ SET TMMF = '" + fileName + "' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                    model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                        0)) + "';")
            query.exec()
            self.ui.lineEdit_tipMusicFile.setText(fileName)
            self.selector(indexT.row(), indexQ.row())



    def delQMusic(self):
        dialog = QMessageBox()
        dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
        dialog.setWindowTitle("Внимание!")
        dialog.setDefaultButton(QMessageBox.Cancel)
        dialog.setButtonText(QMessageBox.Save, "Удалить музыкальную часть вопроса")
        dialog.setButtonText(QMessageBox.Cancel, "Не изменять")
        dialog.setInformativeText("Вы действительно хотите удалить музыкальную часть?")
        dialog.setIcon(QMessageBox.Icon.Critical)
        ok = dialog.exec()
        if ok == QMessageBox.Save:
            indexT = self.ui.tableView_themeTable.currentIndex()
            indexQ = self.ui.tableView_questTable.currentIndex()
            costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
            model = self.ui.tableView_themeTable.model()
            query = QSqlQuery(
                "UPDATE ThemeAndQ SET MMF = NULL WHERE Cost = '" + costq + "' AND Theme = '" + str(
                    model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                        0)) + "';")
            query.exec()
            self.ui.lineEdit_MusicFile.setText("")
            self.selector(indexT.row(), indexQ.row())

    def playMusic(self):
        self.tmr.start(100)
        if self.player.isPlaying():
           self.player.stop()
           icon = QIcon()
           icon.addFile(u"../img/icon/mplay.png", QSize(), QIcon.Normal, QIcon.Off)
           self.ui.commandLinkButton_Play.setIcon(icon)
        else:
            self.audioOutput = QAudioOutput()
            self.player.setAudioOutput(self.audioOutput)
            self.player.setSource(QUrl.fromLocalFile('../media/'+self.ui.lineEdit_MusicFile.text()))
            self.player.play()
            icon = QIcon()
            icon.addFile(u"../img/icon/mstop.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.commandLinkButton_Play.setIcon(icon)

    def selMusic(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        indexQ=self.ui.tableView_questTable.currentIndex()   
        ofileName, filetype = QFileDialog.getOpenFileName(
            self,
            "Выберите музыкальный файл", 
            "", 
            "Media (*.wav *.mp3 )"
        )
        fileName = os.path.basename(ofileName)

        if len(ofileName)>0:
            try:
                self.ui.commandLinkButton_Play.setEnabled(True)
                shutil.copy2(ofileName,"../media/"+fileName)
            except:
                print("апшипка")    
            costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
            model = self.ui.tableView_themeTable.model()
            query = QSqlQuery ("UPDATE ThemeAndQ SET MMF = '" + fileName + "' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
            query.exec()
            self.ui.lineEdit_MusicFile.setText(fileName)
            self.selector(indexT.row(),indexQ.row()) 
            




    def togAnim(self):
        if self.ui.checkBox_disanim.isChecked():
            os.open("../disanim", os.O_CREAT)
        else:
            os.remove("../disanim")

    def testB(self):
        self.updateTheme()

    def finLogoUpd(self):
        self.ui.label_finLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixf=QPixmap("../img/logo/back.png").scaled(self.ui.label_finLogo.frameSize(),Qt.KeepAspectRatio)
        self.ui.label_finLogo.setPixmap(pixf)
        
    def addFinLogo(self):
        ofileName, filetype = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение", 
            "", 
            "Images (*.jpeg *.jpg *.png)"
        )

        if len(ofileName)>0:
            try:
                shutil.copy2(ofileName,"../img/logo/back.png")
            except:
                print("апшипка logo")    
        self.finLogoUpd()
    
    def delFinLogo(self):
        dialog = QMessageBox()
        dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
        dialog.setWindowTitle("Внимание!")
        dialog.setDefaultButton(QMessageBox.Cancel)
        dialog.setButtonText(QMessageBox.Save, "Сбросить фон")
        dialog.setButtonText(QMessageBox.Cancel, "Не изменять")
        dialog.setInformativeText("Вы действительно хотите вернуть фон по умолчанию?")
        dialog.setIcon(QMessageBox.Icon.Critical)
        ok = dialog.exec()
        if ok == QMessageBox.Save:
            try:
                shutil.copy2("../img/logo/defback.png","../img/logo/back.png")
                self.finLogoUpd()
            except:
                print("апшипка logo")    

    def selectFinSound(self):
        ofileName, filetype = QFileDialog.getOpenFileName(
            self,
            "Выберите звук", 
            "", 
            "Sounds (*.wav)"
        )

        if len(ofileName)>0:
            try:
                shutil.copy2(ofileName,"../sound/finalsound.wav")
            except:
                print("апшипка звук")   
    isp=0


    def playFinSound(self):
        # self.tmr = QTimer()  # 4
        # self.tmr.timeout.connect(self.medendfile)
        self.tmr.start(100)
        if str(self.player.mediaStatus())=="MediaStatus.EndOfMedia":
            self.player.stop()
            self.audioOutput = QAudioOutput()
            self.player.setAudioOutput(self.audioOutput)
            self.player.setSource(QUrl.fromLocalFile("../sound/finalsound.wav"))
            self.ui.playFinSound.setText("Стоп")
            self.player.play()

        if self.player.isPlaying():
           self.player.stop()
           self.ui.playFinSound.setText("Прослушать")
        else:
            self.audioOutput = QAudioOutput()
            self.player.setAudioOutput(self.audioOutput)
            self.player.setSource(QUrl.fromLocalFile("../sound/finalsound.wav"))
            self.ui.playFinSound.setText("Стоп")
            self.player.play()



        # self.finalSound = simple_audio.WaveObject.from_wave_file("../sound/finalsound.wav")
        # if self.isp==0:
        #     self.coda = self.finalSound.play()
        #     self.ui.playFinSound.setText("Стоп")
        #     self.isp=1
        # else:
        #     if self.coda.is_playing():
        #         self.coda.stop()
        #         self.ui.playFinSound.setText("Прослушать")
        #         self.isp=0
        #     else:
        #         self.coda=self.finalSound.play()
    
    def delFinSound(self):
        dialog = QMessageBox()
        dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
        dialog.setWindowTitle("Внимание!")
        dialog.setDefaultButton(QMessageBox.Cancel)
        dialog.setButtonText(QMessageBox.Save, "Удалить звук финала")
        dialog.setButtonText(QMessageBox.Cancel, "Не изменять")
        dialog.setInformativeText("Вы действительно хотите удалить звук финала?")
        dialog.setIcon(QMessageBox.Icon.Critical)
        ok = dialog.exec()
        if ok == QMessageBox.Save:
            try:
                shutil.copy2("../sound/mute.wav","../sound/finalsound.wav")
            except:
                print("апшипка mute")    
        
    def addTeamLogo(self):
        rown = int(self.ui.listView_teams.currentIndex().row())
        if (rown==-1):
           QMessageBox.warning(self,"Внимание!","Не выбрана команда для изменения логотипа")
           return()   
        rown+=1
        #dialog = QFileDialog()
        #dialog.setDirectory("../img/logo")
        #dialog.exec()
        ofileName, filetype = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение", 
            "", 
            "Images (*.jpeg *.jpg *.png)"
        )
        fileName = os.path.basename(ofileName)

        if len(ofileName)>0:
            try:
                shutil.copy2(ofileName,"../img/logo/"+fileName)
            except:
                print("апшипка logo")    
            query=QSqlQuery()
            txtq="UPDATE Teams SET Logo='"+str(fileName)+"' WHERE Id="+str(rown)+";"
            query.exec(txtq)
            query.first()
            self.ui.label_teamLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
            pixmap=QPixmap("../img/logo/" + fileName).scaled(self.ui.label_teamLogo.frameSize(),Qt.KeepAspectRatio)
            self.ui.label_teamLogo.setPixmap(pixmap)

            # self.ui.label_teamLogo.setPixmap(
            #     QPixmap("../img/logo" + fileName).scaled(
            #         self.ui.label_questPix.frameSize(), Qt.KeepAspectRatio))
            # self.ui.listView_teams.selectRow(rown-1)
            #self.updateform()

    def delTeamLogo(self):
        rown = int(self.ui.listView_teams.currentIndex().row())
        if (rown==-1):
           QMessageBox.warning(self,"Внимание!","Не выбрана команда для удаления логотипа")
           return()  
        rown += 1
        dialog = QMessageBox()
        dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
        dialog.setWindowTitle("Внимание!")
        dialog.setDefaultButton(QMessageBox.Cancel)
        dialog.setButtonText(QMessageBox.Save, "Удалить логотип")
        dialog.setButtonText(QMessageBox.Cancel, "Не изменять")
        #dialog.setInformativeText("Вы действительно хотите удалить логотип?")
        dialog.setIcon(QMessageBox.Icon.Critical)
        ok = dialog.exec()
        if ok == QMessageBox.Save:
            query = QSqlQuery()
            txtq = "UPDATE Teams SET Logo='"+"' WHERE Id=" + str(rown) + ";"
            query.exec(txtq)
            query.first()
        self.updTeams()

    def selector (self, themeRow, questRow):    
        if (themeRow!=None):
             self.ui.tableView_themeTable.selectRow(themeRow)
        if (questRow!=None):
             self.ui.tableView_questTable.selectRow(questRow) 

    def newGame(self):
        msbox=QMessageBox()
        msbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msbox.setButtonText(QMessageBox.Ok, "Сохранить")
        msbox.setButtonText(QMessageBox.Cancel, "Отменить")
        msbox.setWindowTitle("Осторожно!!!")
        msbox.setText("     Сохранить ли текущую игру? ")
        ok=msbox.exec()
        if ok==QMessageBox.Ok:
            self.saveGame()
        newdialog =  newDialog(self)
        newdialog.setWindowModality(Qt.WindowModal)
        newdialog.exec_() #Вот жеж, exec_ ждется, а show - нет
        #self.updateform()
        #self.catChange()
        self.ui.tableView_themeTable.selectRow(0)
        self.updateform()
        #заполняем цену подсказки нулями
        qzero=QSqlQuery()
        qzero.exec("UPDATE ThemeAndQ SET ToolCost=0 ")



        self.selector(0,0)


        
    def openGame(self):
        dialog = QFileDialog()
        dName=str(dialog.getExistingDirectory(self,"Выбрать папку","./games/"))
           
        try:
            if os.path.isdir(dName+"/img"):
                shutil.rmtree("../img")
            if os.path.isdir(dName + "/media"):
                shutil.rmtree("../media")
            if os.path.isdir(dName + "/sound"):
                shutil.rmtree("../img")
        except:
            print("нечего удалять")
        
        try:
            shutil.copytree(dName+"/img","../img",  symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
            shutil.copytree(dName + "/media", "../media", symlinks=False, ignore=None, ignore_dangling_symlinks=False,
                            dirs_exist_ok=True)
            shutil.copytree(dName + "/sound", "../sound", symlinks=False, ignore=None, ignore_dangling_symlinks=False,
                            dirs_exist_ok=True)
        except:
            print("нет копии")
        shutil.copyfile(dName+"/jep.sqlite","../jep.sqlite")
        self.updateform()
        self.selector(0,0)
        

    def saveGame(self):
        fName =str(QInputDialog.getText(None, " Сохраняем игру", "Введите название ")[0])
        try:
            shutil.rmtree("../games/"+fName)
        except:
            print("нет необходимости")
           
        try:
            shutil.copytree("../img", "../games/"+fName+"/img", symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)
        except:
            print("img games")

        try:
            shutil.copytree("../media", "../games/" + fName + "/media", symlinks=False, ignore=None,
                            ignore_dangling_symlinks=False, dirs_exist_ok=False)
        except:
            print("media games")

        try:
            shutil.copytree("../sound", "../games/" + fName + "/sound", symlinks=False, ignore=None,
                            ignore_dangling_symlinks=False, dirs_exist_ok=False)
        except:
            print("sound games")
        shutil.copyfile("../jep.sqlite","../games/"+fName+"/jep.sqlite")
        self.selector(0,0)


    def delTheme(self):
        index = self.ui.tableView_themeTable.currentIndex()
        curname = str(index.data())
        msbox=QMessageBox()
        msbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msbox.setButtonText(QMessageBox.Ok, "Удаляем")
        msbox.setButtonText(QMessageBox.Cancel, "Отменить")
        msbox.setWindowTitle("Осторожно!!!")
        msbox.setText(" Будут удалены все вопросы темы  "+curname)
        ok=msbox.exec()
        if ok==QMessageBox.Ok:
            query = QSqlQuery()
            query.exec("DELETE FROM ThemeAndQ WHERE Catname ='"+self.ui.comboBox_Cat.currentText()+"' AND Theme='"+curname+"';")
        self.updateform()
        self.selector(0,0)

    def editTheme(self):
        index=self.ui.tableView_themeTable.currentIndex()
        curname = str(index.data())
        themename =str(QInputDialog.getText(None, "Изменяем название темы "+curname, "         Введите новое наименование темы         ")[0])
        query = QSqlQuery()
        query.exec("UPDATE ThemeAndQ SET Theme='"+themename+"' WHERE Theme='"+curname+"';")
        self.updateform()
        self.selector(index.row(),0)
        
    def addTheme(self):
        curcat=str(self.ui.comboBox_Cat.currentText())
        themename = str(QInputDialog.getText(None, " Новая тема ", "Введите наименование темы")[0])
        queryCount=QSqlQuery()
        if not queryCount.exec("SELECT MAX(Cost) FROM ThemeAndQ ;"):
            logging.error("Failed to query categ")
        queryCount.first()
        kvt = int(int(queryCount.value(0))/10)
        if  (kvt == None):
            kvt=QInputDialog.getText(None, "  ", "Введите количество вопросов в теме");
            kvt=int(kvt[0])
        query = QSqlQuery()
        cost=0
        for i in range(kvt):
            cost+=10
            if not query.exec("INSERT INTO ThemeAndQ (Theme,Question,Cost,Catname,Answer) Values ('"+themename+"','Вопрос на "+str(cost)+" темы "+themename+"',"+str(cost)+",'"+str(curcat)+"','Ответ на  "+str(cost)+" темы "+themename+"');"):
                logging.error("Failed to query newTheme1")

        self.updateform()
        self.selector(self.ui.tableView_themeTable.model().rowCount()-1,0)


    def selQpix(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        indexQ=self.ui.tableView_questTable.currentIndex()
        #dialog = QFileDialog()
        #dialog.setDirectory("../img")
        #dialog.exec()
        ofileName, filetype = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение", 
            "", 
            "Images (*.jpeg *.jpg *.png)"
        )
        fileName = os.path.basename(ofileName)

        if len(ofileName)>0:
            try:
                shutil.copy2(ofileName,"../img/"+fileName)
            except:
                print("апшипка")    
            costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
            model = self.ui.tableView_themeTable.model()
            self.textQpix =  ("UPDATE ThemeAndQ SET Image = '" + fileName + "' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
            self.ui.label_questPix.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui.label_questPix.setPixmap(QPixmap("../img/"+fileName).scaled(self.ui.label_questPix.frameSize(),Qt.KeepAspectRatio))
            self.selector(indexT.row(),indexQ.row())

    def delQpix(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        indexQ=self.ui.tableView_questTable.currentIndex()
        costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
        model = self.ui.tableView_themeTable.model()
        self.textQpix = ("UPDATE ThemeAndQ SET Image = '' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
        self.ui.label_questPix.setPixmap(QPixmap(""))
        self.selector(indexT.row(),indexQ.row())
    
    def selApix(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        indexQ=self.ui.tableView_questTable.currentIndex()
        #dialog = QFileDialog()
        #dialog.setDirectory("../img")
        #dialog.exec()
        ofileName, filetype = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение", 
            "", 
            "Images (*.jpeg *.jpg *.png)"
        )
        fileName = os.path.basename(ofileName)

        if len(ofileName)>0:
            try:
                shutil.copy2(ofileName,"../img/"+fileName)
            except:
                print("апшипка")    
            costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
            model = self.ui.tableView_themeTable.model()
            self.textApix =  ("UPDATE ThemeAndQ SET ImageA = '" + fileName + "' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
            self.ui.label_answerPix.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui.label_answerPix.setPixmap(QPixmap("../img/"+fileName).scaled(self.ui.label_answerPix.frameSize(),Qt.KeepAspectRatio))
            self.selector(indexT.row(),indexQ.row())
        
    def delApix(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        indexQ=self.ui.tableView_questTable.currentIndex()        
        costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
        model = self.ui.tableView_themeTable.model()
        self.textApix = ("UPDATE ThemeAndQ SET ImageA = '' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
        self.ui.label_answerPix.setPixmap(QPixmap(""))
        self.selector(indexT.row(),indexQ.row())        
        
    def selTpix(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        indexQ=self.ui.tableView_questTable.currentIndex()   
        #dialog = QFileDialog()
        #dialog.setDirectory("../img")
        #dialog.exec()
        ofileName, filetype = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение", 
            "", 
            "Images (*.jpeg *.jpg *.png)"
        )
        fileName = os.path.basename(ofileName)

        if len(ofileName)>0:
            try:
                shutil.copy2(ofileName,"../img/"+fileName)
            except:
                print("апшипка")    
            costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
            model = self.ui.tableView_themeTable.model()
            self.textTpix =  ("UPDATE ThemeAndQ SET ToolTipImg = '" + fileName + "' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
            self.ui.label_toolPix.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui.label_toolPix.setPixmap(QPixmap("../img/"+fileName).scaled(self.ui.label_toolPix.frameSize(),Qt.KeepAspectRatio))
            self.selector(indexT.row(),indexQ.row()) 

    def delTpix(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        indexQ=self.ui.tableView_questTable.currentIndex()
        costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
        model = self.ui.tableView_themeTable.model()
        self.textTpix = ("UPDATE ThemeAndQ SET ToolTipImg = '' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
        self.ui.label_toolPix.setPixmap(QPixmap(""))        
        self.selector(indexT.row(),indexQ.row()) 
        
    def addTeam(self):
        texteam = QInputDialog.getText(None, "Новая команда", "Введите наименование команды");
        query = QSqlQuery()
        query2 = QSqlQuery()
        if not query.exec("SELECT MAX(Id) FROM Teams;"):
            logging.error("Failed to query database1")
        query.first()
        if texteam[1] == True:
            if not query2.exec(
                    "INSERT INTO Teams (ID,Name) VALUES ("+str(int(query.value(0))+1)+", '"+texteam[0]+"');"):
                logging.error("Failed to query database2")
        self.updateform()
        
        
    def delTeam(self):
        curteam=self.ui.listView_teams.model().data(self.ui.listView_teams.currentIndex())
        curin=self.ui.listView_teams.currentIndex()
        dialog = QMessageBox()
        dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
        dialog.setWindowTitle("Внимание!")
        dialog.setDefaultButton( QMessageBox.Cancel)
        dialog.setButtonText(QMessageBox.Save,"Удалить")
        dialog.setButtonText(QMessageBox.Cancel,"Отменить")
        dialog.setText("Удаляем команду: "+str(curteam))
        dialog.setInformativeText("Осторожно, восстановить команду будет невозможно")
        dialog.setIcon(QMessageBox.Icon.Critical)
        ok = dialog.exec()
        if  ok == QMessageBox.Save:
            query = QSqlQuery()
            if not query.exec("DELETE FROM Teams WHERE name  = '" + curteam + "';"):
               logging.error("ошибка бд")  
            
        else:
            logging.error("Отмена")
        self.updateform()# переделать
        # self.ui.listView_teams.setCurrentIndex(curin-1)
    
    def changeTeam(self):
        curteam=self.ui.listView_teams.model().data(self.ui.listView_teams.currentIndex())
        curin=self.ui.listView_teams.currentIndex()
        dialog = QInputDialog()
        dialog.setWindowTitle("Внимание!")
        dialog.setOkButtonText("Сохранить")
        dialog.setLabelText("Изменяем название команды: "+str(curteam))
        dialog.setTextValue(curteam)
        dialog.setInputMode(QInputDialog.TextInput)
        ok = dialog.exec()
        newval = dialog.textValue()
        if ok:
            query = QSqlQuery()
            if not query.exec("UPDATE Teams  SET Name = '" + newval + "' WHERE name  = '" + curteam + "';"):
               logging.error("ошибка бд") 
        else:
            logging.error("отмена")
        self.updateform()# переделать
        self.ui.listView_teams.setCurrentIndex(curin)

    
    
    
    def Qup(self):
        if (self.ui.tableView_themeTable.currentIndex().row()!=-1):
            if (self.ui.tableView_questTable.currentIndex().row()!=-1):
                self.ChangeCost("Up") 
            else:
                QMessageBox.warning(self,"Внимание!","Форма не готова для перемещения вопроса - вы не выбрали вопрос для перемещения")   
        else:
            QMessageBox.warning(self,"Внимание!","Форма не готова для перемещения вопроса - вы не выбрали тему для перемещения")
        
    def Qdown(self):
        if (self.ui.tableView_themeTable.currentIndex().row()!=-1):
            if (self.ui.tableView_questTable.currentIndex().row()!=-1):
                self.ChangeCost("Down")
            else:
                QMessageBox.warning(self,"Внимание!","Форма не готова для перемещения вопроса - вы не выбрали вопрос для перемещения")   
        else:
            QMessageBox.warning(self,"Внимание!","Форма не готова для перемещения вопроса - вы не выбрали тему для перемещения")
    
    def ChangeCost(self,updown):
        indexT=self.ui.tableView_themeTable.currentIndex()
        model= self.ui.tableView_themeTable.model()
        maxcost = self.ui.tableView_questTable.model().rowCount()
        costq = str(self.ui.tableView_questTable.currentIndex().row()+1)+"0"
        query=QSqlQuery()
        if (updown=="Up"):
            if (int(costq)>10):
                if not query.exec("UPDATE ThemeAndQ SET Cost = '777' WHERE Cost = '"+costq+"' AND Catname ='"+self.ui.comboBox_Cat.currentText()+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                    logging.error("Failed to query database30")  
                if not query.exec("UPDATE ThemeAndQ SET Cost = '"+str(int(costq))+"' WHERE Cost = '"+str(int(costq)-10)+"' AND Catname ='"+self.ui.comboBox_Cat.currentText()+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                    logging.error("Failed to query database31")  
                if not query.exec("UPDATE ThemeAndQ SET Cost = '"+str(int(costq)-10)+"' WHERE Cost = '777' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                    logging.error("Failed to query database30")      
                       
            else:
                QMessageBox.warning(self,"Внимание!","Невозможно понизить стоимость этого вопроса")        
        if (updown=="Down"):
            if (int(costq)<(maxcost*10)):
                if not query.exec("UPDATE ThemeAndQ SET Cost = '777' WHERE Cost = '"+costq+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"' AND  Catname ='"+self.ui.comboBox_Cat.currentText()+"';"):
                    logging.error("Failed to query database30")  
                if not query.exec("UPDATE ThemeAndQ SET Cost = '"+str(int(costq))+"' WHERE Cost = '"+str(int(costq)+10)+"' AND Catname ='"+self.ui.comboBox_Cat.currentText()+"' AND  Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                    logging.error("Failed to query database31")  
                if not query.exec("UPDATE ThemeAndQ SET Cost = '"+str(int(costq)+10)+"' WHERE Cost = '777' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                    logging.error("Failed to query database30")      
            else:
                QMessageBox.warning(self,"Внимание!","Невозможно повысить стоимость этого вопроса")            
        self.updateQuest()
        self.selector(indexT.row(),0) 
        
    def EditMode(self,Mode):
        if (Mode==True):
            self.ui.pushButton_Cancel.setVisible(True)
            self.ui.pushButton_Save.setVisible(True)
            self.ui.pushButton_addQ.setVisible(False)
            self.ui.pushButton_editQ.setVisible(False)
            self.ui.pushButton_delQ.setVisible(False)
            self.ui.textEdit_questText.setEnabled(True)
            self.ui.textEdit_answerText.setEnabled(True)
           # self.ui.label_toolPix.setEnabled(True)
           # self.ui.label_questPix.setEnabled(True)
           # self.ui.toolButton_pixA.setEnabled(True)
           # self.ui.label_answerPix.setEnabled(True)
            #self.ui.toolButton_pixQ.setEnabled(True)
         #   self.ui.groupBox_tooltip.setEnabled(True)
            #self.ui.spinBox_costQuest.setEnabled(True)
            self.ui.checkBox_isBonus.setEnabled(True)
           # self.ui.groupBox_tooltip.setEnabled(True)
            self.ui.tableView_questTable.setEnabled(False)
            self.ui.tableView_themeTable.setEnabled(False)
            self.textQpix = ""
            self.textApix = ""
            self.textTpix = ""
            self.ui.frame_Qpix.setEnabled(True)
            self.ui.frame_Apix.setEnabled(True)
            self.ui.frame_Tpix.setEnabled(True)
            self.ui.textEdit_tooltipText.setEnabled(True)
            self.ui.spinBox_costTooltip.setEnabled(True)
            self.ui.pushButton_selMusic.setEnabled(True)
            self.ui.pushButton_delMusic.setEnabled(True)
            self.ui.pushButton_tipSelMusic.setEnabled(True)
            self.ui.pushButton_tipDelMusic.setEnabled(True)
            
            
        else:
            self.ui.pushButton_Cancel.setVisible(False)
            self.ui.pushButton_Save.setVisible(False)   
            self.ui.pushButton_addQ.setVisible(True)
            self.ui.pushButton_editQ.setVisible(True)
            self.ui.pushButton_delQ.setVisible(True)
            self.ui.textEdit_questText.setEnabled(False)
            self.ui.textEdit_answerText.setEnabled(False)
           # self.ui.label_toolPix.setEnabled(False)
           # self.ui.label_questPix.setEnabled(False)
            #self.ui.toolButton_pixA.setEnabled(False)
            #self.ui.label_answerPix.setEnabled(False)
            #self.ui.toolButton_pixQ.setEnabled(False)
            #self.ui.groupBox_tooltip.setEnabled(False)
            self.ui.spinBox_costQuest.setEnabled(False)
            self.ui.checkBox_isBonus.setEnabled(False)
            #self.ui.groupBox_tooltip.setEnabled(False)
            self.ui.tableView_questTable.setEnabled(True)
            self.ui.tableView_themeTable.setEnabled(True)
            self.ui.frame_Qpix.setEnabled(False)
            self.ui.frame_Apix.setEnabled(False)
            self.ui.frame_Tpix.setEnabled(False)
            self.ui.textEdit_tooltipText.setEnabled(False)
            self.ui.spinBox_costTooltip.setEnabled(False)
            self.ui.pushButton_selMusic.setEnabled(False)
            self.ui.pushButton_delMusic.setEnabled(False)
            self.ui.pushButton_tipSelMusic.setEnabled(False)
            self.ui.pushButton_tipDelMusic.setEnabled(False)


    def CancelQ(self):    
        self.EditMode(False)
        
    def EditQ(self): 
        if (self.ui.tableView_themeTable.currentIndex().row()!=-1):
            if (self.ui.tableView_questTable.currentIndex().row()!=-1):
                self.EditMode(True) 
            else:
                QMessageBox.warning(self,"Внимание!","Форма не готова для редактирования - вы не выбрали вопрос для редактирования")   
        else:
            QMessageBox.warning(self,"Внимание!","Форма не готова для редактирования - вы не выбрали тему для редактирования")
            
    def delQ(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        #cost = str(self.ui.tableView_questTable.currentIndex().row()+1)+"0"
        cost=str((self.ui.tableView_questTable.model().rowCount()*10))
        if (self.ui.tableView_themeTable.currentIndex().row()!=-1):
            if (self.ui.tableView_questTable.currentIndex().row()!=-1):
                dialog = QMessageBox()
                dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
                dialog.setWindowTitle("Внимание!")
                dialog.setDefaultButton( QMessageBox.Cancel)
                dialog.setButtonText(QMessageBox.Save,"Удалить")
                dialog.setButtonText(QMessageBox.Cancel,"Отменить")
                dialog.setText("Удаляем ВСЕ вопросы ценой: "+cost)
                dialog.setInformativeText("Осторожно,  Удаление будет произведено во ВСЕХ темах!")
                dialog.setIcon(QMessageBox.Icon.Critical)
                #dialog.setTextValue(curteam)
                #dialog.setInputMode(QInputDialog.TextInput)
                ok = dialog.exec()
                if  ok == QMessageBox.Save:
                    query = QSqlQuery()
                    query.exec("DELETE from ThemeAndQ WHERE cost= '"+cost+"'")
                    self.updateform()
            else:
             QMessageBox.warning(self,"Внимание!","Форма не готова - вы не выбрали вопрос для удаления")   
        else:
            QMessageBox.warning(self,"Внимание!","Форма не готова - вы не выбрали тему ")

        self.selector(indexT.row(),0)    
        
    def addQ(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        if (self.ui.tableView_themeTable.currentIndex().row()!=-1):
            cost=str((self.ui.tableView_questTable.model().rowCount()*10)+10)
            dialog = QMessageBox()
            dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
            dialog.setWindowTitle("Внимание!")
            dialog.setDefaultButton( QMessageBox.Cancel)
            dialog.setButtonText(QMessageBox.Save,"Добавить вопросы")
            dialog.setButtonText(QMessageBox.Cancel,"Отменить")
            dialog.setText("Добавляем вопросы вопросы ценой: "+cost)
            dialog.setInformativeText("Внимание, Добавление вопросов будет произведено во ВСЕХ темах!")
            dialog.setIcon(QMessageBox.Icon.Critical)
            #dialog.setTextValue(curteam)
            #dialog.setInputMode(QInputDialog.TextInput)
            ok = dialog.exec()
            if  ok == QMessageBox.Save:
                curcat=str(self.ui.comboBox_Cat.currentText())
                queryTheme=QSqlQuery()
                if not queryTheme.exec("SELECT DISTINCT Theme FROM ThemeAndQ;"):
                    logging.error("Failed to query categ2")
                query = QSqlQuery()
                while queryTheme.next():
                    if not query.exec("INSERT INTO ThemeAndQ (Theme,Question,Cost,Catname,Answer) Values ('"+str(queryTheme.value(0))+"','Вопрос на "+str(cost)+" темы "+str(queryTheme.value(0))+"',"+str(cost)+",'"+str(curcat)+"','Ответ на  "+str(cost)+" темы "+str(queryTheme.value(0))+"');"):
                        logging.error("Failed to query newTheme1")
            self.updateform()
            self.selector(indexT.row(),0)
            self.selector(indexT.row(),self.ui.tableView_questTable.model().rowCount()-1) 

        else:
            QMessageBox.warning(self,"Внимание!","Форма не готова - вы не выбрали тему ")
            
        
        
    def SaveQ(self):    
        indexT=self.ui.tableView_themeTable.currentIndex()
        indexQ=self.ui.tableView_questTable.currentIndex()
        costq = str(self.ui.tableView_questTable.currentIndex().row()+1)+"0"
        query = QSqlQuery()
        model= self.ui.tableView_themeTable.model()
        if self.ui.checkBox_isBonus.isChecked():
            isBonus= str(True)
        else:
            isBonus= ""
                
        if not query.exec("UPDATE ThemeAndQ SET Question = '"+self.ui.textEdit_questText.toPlainText()+"', isBonus = '"+isBonus+"', Answer = '"+self.ui.textEdit_answerText.toPlainText()+"', Tooltip = '"+self.ui.textEdit_tooltipText.toPlainText()+"', ToolCost = '"+str(self.ui.spinBox_costTooltip.value())+"' WHERE Cost = '"+costq+"' AND Catname ='"+self.ui.comboBox_Cat.currentText()+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
            logging.error("Failed to query database")
        if (len(self.textQpix)!=0):
            if not query.exec(self.textQpix):
                logging.error("Failed to query database40")
        if (len(self.textApix)!=0):
            if not query.exec(self.textApix):
                logging.error("Failed to query database41") 
        if (len(self.textTpix)!=0):
            if not query.exec(self.textTpix):
                logging.error("Failed to query database42")                 
        self.updateQuest()
        self.EditMode(False)
        self.selector(indexT.row(),indexQ.row()) 
   
   
   
   
   
        
    def updateform(self):
        self.ui.comboBox_Cat.clear()
        query = QSqlQuery()
        if not query.exec("SELECT * FROM category;"):
            logging.error("Failed to query database")  
        while(query.next()):
            self.ui.comboBox_Cat.addItem(query.value(1))
        modelt=QSqlQueryModel()
        modelt.setQuery("SELECT Name FROM Teams")
        self.ui.listView_teams.setModel(modelt)
        self.changeTeamListRow()
        self.finLogoUpd()

    def changeTeamListRow(self):
        selectionModel = self.ui.listView_teams.selectionModel()
        selectionModel.selectionChanged.connect(self.updTeams)

    def updTeams(self):
        rown = int(self.ui.listView_teams.currentIndex().row())
        rown += 1
        query=QSqlQuery()
        query.exec("SELECT Logo FROM Teams WHERE Id="+str(rown)+";")
        query.first()
        fileName=str(query.value(0))
        pixmap = QPixmap("../img/logo/" + fileName).scaled(
            self.ui.label_teamLogo.frameSize(), Qt.KeepAspectRatio)
        self.ui.label_teamLogo.setPixmap(pixmap)

    def updateTheme(self):
        model = QSqlQueryModel()
        txtquery = "SELECT DISTINCT Theme FROM ThemeAndQ WHERE Catname ='"+self.ui.comboBox_Cat.currentText()+"';"
        model.setQuery(txtquery)
        self.ui.tableView_themeTable.setModel(model)
        self.ui.tableView_themeTable.setColumnWidth(0,650)
        selectionModel = self.ui.tableView_themeTable.selectionModel()
        selectionModel.selectionChanged.connect(self.updateQuest)
        self.updateQuest()

        

    def updateQuest(self):
        indexT=self.ui.tableView_themeTable.currentIndex()
        cindex=self.ui.tableView_themeTable.model().index(self.ui.tableView_themeTable.currentIndex().row(),0)
        catname=self.ui.comboBox_Cat.currentText()
        curtheme=self.ui.tableView_themeTable.model().data(cindex)
        modelq = QSqlQueryModel()
        modelq.setQuery("SELECT Question From ThemeAndQ WHERE Theme = '"+str(curtheme)+"' AND Catname = '"+str(catname)+"' ORDER BY Cost ;")
        self.ui.tableView_questTable.setModel(modelq)
        self.ui.tableView_questTable.setColumnWidth(0, 650)
        selectionModel = self.ui.tableView_questTable.selectionModel()
        selectionModel.selectionChanged.connect(self.updQuestText)
        self.updQuestText()
       # print(str(self.ui.tableView_questTable.model().rowCount()))
        self.selector(indexT.row(),0) 


    def updQuestText(self): 
        quetext=self.ui.tableView_questTable.model().data(self.ui.tableView_questTable.currentIndex())
        themetext=self.ui.tableView_themeTable.model().data(self.ui.tableView_themeTable.currentIndex())
        catname=self.ui.comboBox_Cat.currentText()
        self.ui.textEdit_questText.setText(quetext)
        query = QSqlQuery()
        if not query.exec("SELECT * FROM ThemeAndQ WHERE Question='"+str(quetext)+"' AND Theme='"+str(themetext)+"' AND Catname = '"+str(catname)+"';"):
            logging.error("Failed to query database") 
        query.first()

        pixQ = QPixmap("../img/" + str(query.value(3)) )
        self.ui.label_questPix.setAlignment( Qt.AlignmentFlag.AlignCenter)
        self.ui.label_questPix.setPixmap(pixQ.scaled(self.ui.label_questPix.frameSize(),Qt.KeepAspectRatio))

        pixA = QPixmap("../img/" + str(query.value(5)) )
        self.ui.label_answerPix.setAlignment( Qt.AlignmentFlag.AlignCenter)
        self.ui.label_answerPix.setPixmap(pixA.scaled(self.ui.label_questPix.frameSize(),Qt.KeepAspectRatio))

        pixT = QPixmap("../img/" + str(query.value(9)) )
        self.ui.label_toolPix.setAlignment( Qt.AlignmentFlag.AlignCenter)
        self.ui.label_toolPix.setPixmap(pixT.scaled(self.ui.label_questPix.frameSize(),Qt.KeepAspectRatio))
        
        self.ui.textEdit_answerText.setText(query.value(4))
        self.ui.textEdit_tooltipText.setText(query.value(6))
        if bool(query.value(8)):
            self.ui.checkBox_isBonus.setChecked(True)# бонус
        else:
            self.ui.checkBox_isBonus.setChecked(False)# бонус

        if str(query.value(13))!="":    #music
            self.ui.commandLinkButton_Play.setEnabled(True)
            self.ui.lineEdit_MusicFile.setText(str(query.value(13)))
        else:
            self.ui.commandLinkButton_Play.setEnabled(False)
            self.ui.lineEdit_MusicFile.setText("")

        if str(query.value(14))!="":    #tip_music
            self.ui.commandLinkButton_tipPlay.setEnabled(True)
            self.ui.lineEdit_tipMusicFile.setText(str(query.value(14)))
        else:
            self.ui.commandLinkButton_tipPlay.setEnabled(False)
            self.ui.lineEdit_tipMusicFile.setText("")

        
        if query.value(2)!=None:
            self.ui.label_questText.setText("Вопрос на  "+str(query.value(2)))
            self.ui.label_answerText.setText("Ответ на  "+str(query.value(2)))
            self.ui.label_tooltipText.setText("Подсказка ответа на  "+str(query.value(2)))
        else:
            self.ui.label_questText.setText("Выберите вопрос") 
            self.ui.label_answerText.setText("Выберите вопрос")   
            self.ui.label_tooltipText.setText("Выберите вопрос")
        if query.value(2)!=None:
            self.ui.spinBox_costQuest.setValue(int(query.value(2)))
        if query.value(7):
            self.ui.spinBox_costTooltip.setValue(int(query.value(7)))
        else:
            self.ui.spinBox_costTooltip.setValue(0)
            


    def catChange(self):

        self.updateTheme()
        self.ui.tableView_themeTable.selectRow(0)

    
    def addCat(self):
        texcat = QInputDialog.getText(None,"PyG","Введите наименование категории"); 
        query = QSqlQuery()
        query2 = QSqlQuery()
        if not query.exec("SELECT MAX(catcode) FROM category;"):
                logging.error("Failed to query database") 
        query.first()
        if texcat[1] == True:
            if not query2.exec("INSERT INTO category  VALUES ("+str(int(query.value(0))+1)+", '"+texcat[0]+"');"):
                 logging.error("Failed to query database")
        self.updateform()
        self.selector(0,0)

    def editCat(self):
        curcat=self.ui.comboBox_Cat.currentText()
        curin=self.ui.comboBox_Cat.currentIndex()
        dialog = QInputDialog()
        dialog.setWindowTitle("Внимание!")
        dialog.setOkButtonText("Сохранить")
        dialog.setLabelText("Изменяем название категории: "+curcat)
        dialog.setTextValue(curcat)
        dialog.setInputMode(QInputDialog.TextInput)
        ok = dialog.exec()
        newval = dialog.textValue()
        if ok:
            query = QSqlQuery()
            if not query.exec("UPDATE category  SET catname = '" + newval + "' WHERE catname  = '" + curcat + "';"):
                            logging.error("Failed to save category")
            if not query.exec("UPDATE ThemeAndQ  SET Catname = '" + newval + "' WHERE Catname  = '" + curcat + "';"):
                            logging.error("Failed to save category")                            

        self.updateform()
        self.ui.comboBox_Cat.setCurrentIndex(curin)
        self.selector(0,0)


    def delCat(self):
        cbcat=self.ui.comboBox_Cat.currentText()
        ret = QMessageBox.question(self, 'Внимание!', "Уверены в удалении категории "+cbcat+" ?",
                                   QMessageBox.Yes | QMessageBox.No)

        if ret == QMessageBox.Yes:
            query = QSqlQuery()
            query.exec("DELETE from category where catname = '"+cbcat+"'")
            self.updateform()
        self.selector(0,0)    
        
class newDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_Cancel.clicked.connect(self.cancel)
        self.ui.pushButton_Create.clicked.connect(self.create)
    
    def create(self):
        #берем готовую эталонную бд и заменяем ею текущую
        try:
            shutil.copy2("./etbase.sqlite","../jep.sqlite")
            sqlDB = QSqlDatabase.addDatabase('QSQLITE')
            sqlDB.setDatabaseName("../jep.sqlite")
            sqlDB.open()
        except:
                    #если не удалось, а база уже есть какая-то откуда-то) 
            print("Внимание!!! ошибка развертывания эталонной БД")
            # if not query.exec("DELETE FROM ThemeAndQ;"):
            #     logging.error("Failed to query a") 
            # if not query.exec("DELETE FROM category;"):
            #     logging.error("Failed to query a")        
            # if not query.exec("DELETE FROM Teams;"):
            #     logging.error("Failed to query a")                  
            # if not query.exec("DELETE FROM settings;"):
            #     logging.error("Failed to query a") 

        query=QSqlQuery()
        queryCat=QSqlQuery() 
        #Команды
        for team in range(int(self.ui.comboBox_teamCount.currentText())):
            # if not query.exec("INSERT INTO Teams (ID,Name) VALUES ("+str(team+1)+", 'Команда номер "+str(team+1)+"');"):
            if not query.exec("INSERT INTO Teams (ID,Name) VALUES ("+str(team)+", 'Команда номер "+str(team+1)+"');"):
                logging.error("Failed to query database2")
        #Настройки
        if not query.exec("INSERT INTO settings (NameGame,TimeSec,Pad) VALUES ('Игра', '30', '10');"):
            logging.error("Failed to query database2")
        
        #цикл категорий

        for cat in range(int(self.ui.comboBox_categCount.currentText())):
                if (int(self.ui.comboBox_categCount.currentText())<=1):
                    catname = "К вопросам"
                else:
                    catname = "Категория номер "+str(cat+1)
                if not queryCat.exec("INSERT INTO category  VALUES ("+str(cat+1)+", '"+catname+"');"):
                    logging.error("Failed to query a") 
                        
                #цикл тем
                for theme in range(int(self.ui.comboBox_themeCount.currentText())):
                    themename="Тема "+str(theme+1)+" категории "+catname
                    cost=0       #Цикл вопросов
                    for quest in range(int(self.ui.comboBox_questCount.currentText())):
                        cost+=10
                        if not query.exec("INSERT INTO ThemeAndQ (Theme,Question,Cost,Catname,Answer) Values ('"+themename+"','Вопрос на "+str(cost)+" темы "+themename+"',"+str(cost)+",'"+catname+"','Ответ на  "+str(cost)+" темы "+themename+"');"):
                            logging.error("Failed to query newTheme1")
                        
        
        QMessageBox.information(self,"Готово","Создание новой игры завершено")
        
        self.close()
        
    
    def cancel(self):
        self.close()    

if __name__ == "__main__":

    app = QApplication(sys.argv)
    splash = QSplashScreen()
    splash.setPixmap(QPixmap("../img/logo/psplash.png"))
    splash.show()
    widget = MainWindow()
    splash.finish(widget)
    widget.showMaximized()
    sys.exit(app.exec())
# This Python file uses the following encoding: utf-8
import logging
import os
import sys
import shutil

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

from PySide6.QtWidgets import QApplication, QInputDialog, QMainWindow, QMessageBox, QFileDialog, QDialog, QVBoxLayout, \
    QLabel, QPushButton, QButtonGroup, QHBoxLayout


from mainwindow import Ui_MainWindow
from newDialog import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        sqlDB = QSqlDatabase.addDatabase('QSQLITE')
        sqlDB.setDatabaseName(os.path.dirname(os.path.abspath(__file__))+"/../jep.sqlite")
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
        self.ui.testButton.setVisible(False)
        self.textQpix = ""
        self.textApix = ""
        self.textTpix = ""
        self.EditMode(False)
        self.updateform()
        self.selector(0,0)

    def testB(self):
        self.updateTheme()

    def addTeamLogo(self):
        rown = int(self.ui.listView_teams.currentIndex().row())
        rown+=1
        dialog = QFileDialog()
        dialog.setDirectory(os.path.dirname(os.path.abspath(__file__)) + "/../img/logo")
        dialog.exec()
        fileName = dialog.selectedFiles()
        if len(fileName)>0:
            s = str(fileName)
            ch = '/'
            indexes = [i for i, c in enumerate(s) if c == ch]
            rpos = max(indexes)
            fileName = s[rpos + 1:]
            l = len(fileName)
            fileName = fileName[:l - 2]
            query=QSqlQuery()
            txtq="UPDATE Teams SET Logo='"+str(fileName)+"' WHERE Id="+str(rown)+";"
            query.exec(txtq)
            query.first()
            self.ui.label_teamLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
            pixmap=QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/logo/" + fileName).scaled(self.ui.label_teamLogo.frameSize(),Qt.KeepAspectRatio)
            self.ui.label_teamLogo.setPixmap(pixmap)

            # self.ui.label_teamLogo.setPixmap(
            #     QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/logo" + fileName).scaled(
            #         self.ui.label_questPix.frameSize(), Qt.KeepAspectRatio))
            # self.ui.listView_teams.selectRow(rown-1)
            #self.updateform()

    def delTeamLogo(self):
        rown = int(self.ui.listView_teams.currentIndex().row())
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
        print(dName)
        shutil.copytree(dName+"/img",os.path.dirname(os.path.abspath(__file__))+"/../img",  symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
        shutil.copyfile(dName+"/jep.sqlite",os.path.dirname(os.path.abspath(__file__)) + "/../jep.sqlite")
        self.updateform()
        self.selector(0,0)
        

        

    def saveGame(self):
        fName =str(QInputDialog.getText(None, " Сохраняем игру", "Введите название ")[0])
        shutil.copytree(os.path.dirname(os.path.abspath(__file__))+"/../img", os.path.dirname(os.path.abspath(__file__))+"/../games/"+fName+"/img", symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)
        shutil.copyfile(os.path.dirname(os.path.abspath(__file__)) + "/../jep.sqlite",os.path.dirname(os.path.abspath(__file__))+"/../games/"+fName+"/jep.sqlite")
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
        dialog = QFileDialog()
        dialog.setDirectory(os.path.dirname(os.path.abspath(__file__))+"/../img")
        dialog.exec()
        fileName = dialog.selectedFiles()
        s = str(fileName)
        ch = '/'
        indexes = [i for i, c in enumerate(s) if c == ch]
        rpos = max(indexes)
        fileName = s[rpos + 1:]
        l = len(fileName)
        fileName = fileName[:l - 2]
        # print(fileName)
        costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
        model = self.ui.tableView_themeTable.model()
        self.textQpix =  ("UPDATE ThemeAndQ SET Image = '" + fileName + "' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
        self.ui.label_questPix.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.label_questPix.setPixmap(QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/"+fileName).scaled(self.ui.label_questPix.frameSize(),Qt.KeepAspectRatio))
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
        dialog = QFileDialog()
        dialog.setDirectory(os.path.dirname(os.path.abspath(__file__))+"/../img")
        dialog.exec()
        fileName = dialog.selectedFiles()
        s = str(fileName)
        ch = '/'
        indexes = [i for i, c in enumerate(s) if c == ch]
        rpos = max(indexes)
        fileName = s[rpos + 1:]
        l = len(fileName)
        fileName = fileName[:l - 2]
        # print(fileName)
        costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
        model = self.ui.tableView_themeTable.model()
        self.textApix =  ("UPDATE ThemeAndQ SET ImageA = '" + fileName + "' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
        self.ui.label_answerPix.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.label_answerPix.setPixmap(QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/"+fileName).scaled(self.ui.label_answerPix.frameSize(),Qt.KeepAspectRatio))
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
        dialog = QFileDialog()
        dialog.setDirectory(os.path.dirname(os.path.abspath(__file__))+"/../img")
        dialog.exec()
        fileName = dialog.selectedFiles()
        s = str(fileName)
        ch = '/'
        indexes = [i for i, c in enumerate(s) if c == ch]
        rpos = max(indexes)
        fileName = s[rpos + 1:]
        l = len(fileName)
        fileName = fileName[:l - 2]
        costq = str(self.ui.tableView_questTable.currentIndex().row() + 1) + "0"
        model = self.ui.tableView_themeTable.model()
        self.textTpix =  ("UPDATE ThemeAndQ SET ToolTipImg = '" + fileName + "' WHERE Cost = '" + costq + "' AND Theme = '" + str(
                        model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(), 0)).get(
                                0)) + "';")
        self.ui.label_toolPix.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.label_toolPix.setPixmap(QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/"+fileName).scaled(self.ui.label_toolPix.frameSize(),Qt.KeepAspectRatio))
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
        #print(str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0)))  
        #print(costq)  
        if (len(self.textQpix)!=0):
            if not query.exec(self.textQpix):
                logging.error("Failed to query database40")  
                print(self.textQpix)
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
        print(fileName)
        pixmap = QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/logo/" + fileName).scaled(
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

        pixQ = QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/" + str(query.value(3)) )
        self.ui.label_questPix.setAlignment( Qt.AlignmentFlag.AlignCenter)
        self.ui.label_questPix.setPixmap(pixQ.scaled(self.ui.label_questPix.frameSize(),Qt.KeepAspectRatio))

        pixA = QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/" + str(query.value(5)) )
        self.ui.label_answerPix.setAlignment( Qt.AlignmentFlag.AlignCenter)
        self.ui.label_answerPix.setPixmap(pixA.scaled(self.ui.label_questPix.frameSize(),Qt.KeepAspectRatio))

        pixT = QPixmap(os.path.dirname(os.path.abspath(__file__)) + "/../img/" + str(query.value(9)) )
        self.ui.label_toolPix.setAlignment( Qt.AlignmentFlag.AlignCenter)
        self.ui.label_toolPix.setPixmap(pixT.scaled(self.ui.label_questPix.frameSize(),Qt.KeepAspectRatio))
        
        self.ui.textEdit_answerText.setText(query.value(4))
        self.ui.textEdit_tooltipText.setText(query.value(6))
        if bool(query.value(8)):
            self.ui.checkBox_isBonus.setChecked(True)# бонус
        else:
            self.ui.checkBox_isBonus.setChecked(False)# бонус
            
        
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
        #       Высчитываем количество тем и вопросов
        # query2 = QSqlQuery()
        # if not query2.exec("SELECT COUNT(DISTINCT Theme) FROM ThemeAndQ WHERE Catkod = " + str(self.ui.comboBox_Cat.currentIndex()+1) + " ;"):
        #     logging.error("Failed to query database")
        # query2.first()
        # self.ui.spinBox_themes.setValue(int(query2.value(0)))

        # query3 = QSqlQuery()
        # if not query3.exec("SELECT Theme, COUNT(*) value_count FROM ThemeAndQ WHERE Catkod = " + str(self.ui.comboBox_Cat.currentIndex()+1) + " GROUP BY Theme HAVING value_count > 1  ;"):
        #     logging.error("Failed to query database")
        # query3.first()
        # self.ui.spinBox_questions.setValue(int(query3.value(1)))


        # query = QSqlQuery()
        # if not query.exec("SELECT * FROM ThemeAndQ;"):
        #     logging.error("Failed to query database")  
        # while(query.next()):
        #     print("vchjd")
        self.updateTheme()
        self.ui.tableView_themeTable.selectRow(0)
      #  self.updateform()
      #  self.selector(0,0)
        #self.updateform()
    
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
        #подготовка 
        qertyPrep=QSqlQuery()
        queryCat=QSqlQuery()
        query=QSqlQuery()
        if not query.exec("DELETE FROM ThemeAndQ;"):
            logging.error("Failed to query a") 
        if not query.exec("DELETE FROM category;"):
            logging.error("Failed to query a")        
        if not query.exec("DELETE FROM Teams;"):
            logging.error("Failed to query a")                  
        if not query.exec("DELETE FROM settings;"):
            logging.error("Failed to query a") 
        #Команды
        for team in range(int(self.ui.comboBox_teamCount.currentText())):
            if not query.exec("INSERT INTO Teams (ID,Name) VALUES ("+str(team+1)+", 'Команда номер "+str(team+1)+"');"):
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
                    logging.eror("Failed to query a") 
                        
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
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
# This Python file uses the following encoding: utf-8
import logging
import os
import sys
import shutil

from PySide6.QtCore import Qt, QModelIndex, QItemSelectionModel
from PySide6.QtGui import QPixmap
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

from PySide6.QtWidgets import QApplication, QInputDialog, QMainWindow, QMessageBox, QFileDialog, QDialog, QVBoxLayout

from teams import Ui_Dialog

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        sqlDB = QSqlDatabase.addDatabase('QSQLITE')
        sqlDB.setDatabaseName("./jep.sqlite")
        sqlDB.open()
        self.ui.setupUi(self)
        self.ui.pushButton_editTeam.clicked.connect(self.changeTeam)
        self.ui.pushButton_delTeam.clicked.connect(self.delTeam)
        self.ui.pushButton_addTeam.clicked.connect(self.addTeam)
        self.ui.pushButton_addTeamLogo.clicked.connect(self.addTeamLogo)
        self.ui.pushButton_delTeamLogo.clicked.connect(self.delTeamLogo)
        self.updateform()
        # modin=QModelIndex()
        # modin.data(2)
        #self.ui.listView_teams.rootIndex()
#        self.ui.listView_teams.selectAll()
        
    def updateform(self):
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
        pixmap = QPixmap("./img/logo/" + fileName).scaled(
            self.ui.label_teamLogo.frameSize(), Qt.KeepAspectRatio)
        self.ui.label_teamLogo.setPixmap(pixmap)
        
    def addTeamLogo(self):
        rown = int(self.ui.listView_teams.currentIndex().row())
        if (rown==-1):
           QMessageBox.warning(self,"Внимание!","Не выбрана команда для изменения логотипа")
           return()   
        rown+=1
        dialog = QFileDialog()
        dialog.setDirectory("./img/logo")
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
            pixmap=QPixmap("./img/logo/" + fileName).scaled(self.ui.label_teamLogo.frameSize(),Qt.KeepAspectRatio)
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
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
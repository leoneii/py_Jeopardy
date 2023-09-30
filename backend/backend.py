# This Python file uses the following encoding: utf-8
import logging
import os
import sys
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

from PySide6.QtWidgets import QApplication, QInputDialog, QMainWindow, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.p+*-/y
from mainwindow import Ui_MainWindow

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
        self.ui.pushButton_editTeam.clicked.connect(self.changeTeam)
        self.ui.pushButton_delTeam.clicked.connect(self.delTeam)
        self.ui.pushButton_addTeam.clicked.connect(self.addTeam)
        self.ui.pushButton_editQ.clicked.connect(self.EditQ)
        self.ui.pushButton_Save.clicked.connect(self.SaveQ)
        self.ui.pushButton_Cancel.clicked.connect(self.CancelQ)
        self.ui.pushButton_Qup.clicked.connect(self.Qup)
        self.ui.pushButton_Qdown.clicked.connect(self.Qdown)
        self.EditMode(False)
        self.updateform()


    def addTeam(self):
        texteam = QInputDialog.getText(None, "PyG", "Введите наименование команды");
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
        #dialog.setTextValue(curteam)
        #dialog.setInputMode(QInputDialog.TextInput)
        ok = dialog.exec()
        if  ok == QMessageBox.Save:
    # Save was clicked
            #print(newval + " was saved")
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
        #print(str(curteam))
        dialog = QInputDialog()
        dialog.setWindowTitle("Внимание!")
        dialog.setOkButtonText("Сохранить")
        dialog.setLabelText("Изменяем название команды: "+str(curteam))
        dialog.setTextValue(curteam)
        dialog.setInputMode(QInputDialog.TextInput)
        ok = dialog.exec()
        newval = dialog.textValue()
        if ok:
            #print(newval + " was saved")
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
        model= self.ui.tableView_themeTable.model()
        maxcost = self.ui.tableView_questTable.model().rowCount()
        costq = str(self.ui.tableView_questTable.currentIndex().row()+1)+"0"
        query=QSqlQuery()
        if (updown=="Up"):
            if (int(costq)>10):
                if not query.exec("UPDATE ThemeAndQ SET Cost = '777' WHERE Cost = '"+costq+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                     logging.error("Failed to query database30")  
                if not query.exec("UPDATE ThemeAndQ SET Cost = '"+str(int(costq))+"' WHERE Cost = '"+str(int(costq)-10)+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                     logging.error("Failed to query database31")  
                if not query.exec("UPDATE ThemeAndQ SET Cost = '"+str(int(costq)-10)+"' WHERE Cost = '777' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                     logging.error("Failed to query database30")      
                       
            else:
                QMessageBox.warning(self,"Внимание!","Невозможно понизить стоимость этого вопроса")        
        if (updown=="Down"):
            if (int(costq)<(maxcost*10)):
                if not query.exec("UPDATE ThemeAndQ SET Cost = '777' WHERE Cost = '"+costq+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                     logging.error("Failed to query database30")  
                if not query.exec("UPDATE ThemeAndQ SET Cost = '"+str(int(costq))+"' WHERE Cost = '"+str(int(costq)+10)+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                     logging.error("Failed to query database31")  
                if not query.exec("UPDATE ThemeAndQ SET Cost = '"+str(int(costq)+10)+"' WHERE Cost = '777' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
                     logging.error("Failed to query database30")      
                        
                       
            else:
                QMessageBox.warning(self,"Внимание!","Невозможно повысить стоимость этого вопроса")            
        self.updateQuest()
        
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
            self.ui.toolButton_pixA.setEnabled(True)
           # self.ui.label_answerPix.setEnabled(True)
            self.ui.toolButton_pixQ.setEnabled(True)
            self.ui.groupBox_tooltip.setEnabled(True)
            #self.ui.spinBox_costQuest.setEnabled(True)
            self.ui.checkBox_isBonus.setEnabled(True)
            self.ui.groupBox_tooltip.setEnabled(True)
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
            self.ui.toolButton_pixA.setEnabled(False)
            #self.ui.label_answerPix.setEnabled(False)
            self.ui.toolButton_pixQ.setEnabled(False)
            self.ui.groupBox_tooltip.setEnabled(False)
            self.ui.spinBox_costQuest.setEnabled(False)
            self.ui.checkBox_isBonus.setEnabled(False)
            self.ui.groupBox_tooltip.setEnabled(False)

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
            
        
    def SaveQ(self):    
        costq = str(self.ui.tableView_questTable.currentIndex().row()+1)+"0"
        query = QSqlQuery()
        model= self.ui.tableView_themeTable.model()
        if not query.exec("UPDATE ThemeAndQ SET Question = '"+self.ui.textEdit_questText.toPlainText()+"', isBonus = '"+str(self.ui.checkBox_isBonus.isChecked())+"', Answer = '"+self.ui.textEdit_answerText.toPlainText()+"', Tooltip = '"+self.ui.textEdit_tooltipText.toPlainText()+"' WHERE Cost = '"+costq+"' AND Theme = '"+str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0))+"';"):
            logging.error("Failed to query database")  
        #print(str(model.itemData(model.index(self.ui.tableView_themeTable.currentIndex().row(),0)).get(0)))  
        #print(costq)  
        self.ui.tableView_themeTable.selectRow(self.ui.tableView_themeTable.currentIndex().row())
        self.updateQuest()
        self.EditMode(False)

        
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

    def changeTeamListRow(self):
        modelt=self.ui.listView_teams.model()


        
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
        cindex=self.ui.tableView_themeTable.model().index(self.ui.tableView_themeTable.currentIndex().row(),0)
        curtheme=self.ui.tableView_themeTable.model().data(cindex)
        modelq = QSqlQueryModel()
        modelq.setQuery("SELECT Question From ThemeAndQ WHERE Theme = '"+str(curtheme)+"'  ORDER BY Cost ;")
        self.ui.tableView_questTable.setModel(modelq)
        self.ui.tableView_questTable.setColumnWidth(0, 650)
        selectionModel = self.ui.tableView_questTable.selectionModel()
        selectionModel.selectionChanged.connect(self.updQuestText)
        self.updQuestText()
       # print(str(self.ui.tableView_questTable.model().rowCount()))



    def updQuestText(self): 
        quetext=self.ui.tableView_questTable.model().data(self.ui.tableView_questTable.currentIndex())
        self.ui.textEdit_questText.setText(quetext)


        query = QSqlQuery()
        qtxt="SELECT * FROM ThemeAndQ WHERE Question='"+str(quetext)+"';"
        query.exec(qtxt)
        query.first()
        txtansw=query.value(4)
        self.ui.textEdit_answerText.setText(txtansw)
        txttot=query.value(6)
        self.ui.textEdit_tooltipText.setText(txttot)
        self.ui.checkBox_isBonus.setChecked(bool(query.value(8)))# бонус
        if query.value(2)!=None:
            self.ui.label_questText.setText("Текст вопроса на "+str(query.value(2)))
            self.ui.label_answerText.setText("Текст ответа на "+str(query.value(2)))
        else:
            self.ui.label_questText.setText("Выберите вопрос") 
            self.ui.label_answerText.setText("Выберите вопрос")   
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
            #print(newval + " was saved")
            query = QSqlQuery()
            que = "UPDATE category  SET catname = '" + newval + "' WHERE catname  = '" + curcat + "';"
            #print(que)
            query.exec(que)
        else:
            logging.error("Failed to save category")
        self.updateform()
        self.ui.comboBox_Cat.setCurrentIndex(curin)


    def delCat(self):
        cbcat=self.ui.comboBox_Cat.currentText()
        ret = QMessageBox.question(self, 'Внимание!', "Уверены в удалении категории "+cbcat+" ?",
                                   QMessageBox.Yes | QMessageBox.No)

        if ret == QMessageBox.Yes:
            query = QSqlQuery()
            query.exec("DELETE from category where catname = '"+cbcat+"'")
            self.updateform()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
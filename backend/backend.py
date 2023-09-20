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
        self.ui.pushButton_addCat.clicked.connect(self.addCat)
        self.ui.pushButton_EditCat.clicked.connect(self.editCat)
        self.ui.pushButton__delCat.clicked.connect(self.delCat)
        self.ui.comboBox_Cat.currentIndexChanged.connect(self.catChange)
        self.updateform()
        
    def updateform(self):
        self.ui.comboBox_Cat.clear()
        query = QSqlQuery()
        if not query.exec("SELECT * FROM category;"):
            logging.error("Failed to query database")  
        while(query.next()):
            self.ui.comboBox_Cat.addItem(query.value(1))
        #self.updateform()
        
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
        ridx=self.ui.tableView_themeTable.currentIndex().row()
        cindex=self.ui.tableView_themeTable.model().index(ridx,0)
        curtheme=self.ui.tableView_themeTable.model().data(cindex)
        modelq = QSqlQueryModel()
        txtqueryq="SELECT Question From ThemeAndQ WHERE Theme = '"+str(curtheme)+"';"
        modelq.setQuery(txtqueryq)
        self.ui.tableView_questTable.setModel(modelq)
        self.ui.tableView_questTable.setColumnWidth(0, 650)
        selectionModel = self.ui.tableView_questTable.selectionModel()
        selectionModel.selectionChanged.connect(self.updQuestText)
        self.updQuestText()



    def updQuestText(self):
        ridx = self.ui.tableView_questTable.currentIndex()
        quetext=self.ui.tableView_questTable.model().data(ridx)
        self.ui.textEdit_questText.setText(quetext)
        query = QSqlQuery()
        qtxt="SELECT * FROM ThemeAndQ WHERE Question='"+str(quetext)+"';"
        query.exec(qtxt)
        query.first()
        txtansw=query.value(4)
        self.ui.textEdit_answerText.setText(txtansw)
        txttot=query.value(6)
        self.ui.textEdit_tooltipText.setText(txttot)
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
        print(query.value(0))         
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
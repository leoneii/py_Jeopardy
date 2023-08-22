# This Python file uses the following encoding: utf-8
import logging
import os
import sys
from PySide6.QtSql import QSqlDatabase, QSqlQuery

from PySide6.QtWidgets import QApplication, QInputDialog, QMainWindow, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
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
        self.ui.pushButton__delCat.clicked.connect(self.delCat)
        self.ui.comboBox_Cat.currentIndexChanged.connect(self.catChange)
        self.updateform()
        print ()
        
    def updateform(self):
        self.ui.comboBox_Cat.clear()
        query = QSqlQuery()
        if not query.exec("SELECT * FROM category;"):
            logging.error("Failed to query database")  
        while(query.next()):
            self.ui.comboBox_Cat.addItem(query.value(1))
        
    def catChange(self):
        #       Высчитываем количество тем и вопросов
        query2 = QSqlQuery()
        if not query2.exec("SELECT COUNT(DISTINCT Theme) FROM ThemeAndQ WHERE Catkod = " + str(self.ui.comboBox_Cat.currentIndex()+1) + " ;"):
            logging.error("Failed to query database")
        query2.first()
        self.ui.spinBox_themes.setValue(int(query2.value(0)))

        query3 = QSqlQuery()
        if not query3.exec("SELECT Theme, COUNT(*) value_count FROM ThemeAndQ WHERE Catkod = " + str(self.ui.comboBox_Cat.currentIndex()+1) + " GROUP BY Theme HAVING value_count > 1  ;"):
            logging.error("Failed to query database")
        query3.first()
        self.ui.spinBox_questions.setValue(int(query3.value(1)))


        # query = QSqlQuery()
        # if not query.exec("SELECT * FROM ThemeAndQ;"):
        #     logging.error("Failed to query database")  
        # while(query.next()):
        #     print("vchjd")
        
    
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

    def delCat(self):
        cbcat=self.ui.comboBox_Cat.currentText()
        ret = QMessageBox.question(self, 'Внимание!', "Уверены в удалении категории "+cbcat+" ?",
                                   QMessageBox.Yes | QMessageBox.No)

        if ret == QMessageBox.Yes:
            query = QSqlQuery()
            query.exec("DELETE from category where catname = "+self.ui.comboBox_Cat.currentText())
            QSqlDatabase.commit(None)
            self.updateform()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

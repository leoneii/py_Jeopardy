import random
import sys

from PySide6.QtCore import QSize, Qt, QVariantAnimation, QObject
from PySide6.QtGui import QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel


class FinalWind(QMainWindow):

    def __init__(self, parent= None):
        super().__init__()
        (wdt, hgt) = app.screens()[0].size().toTuple()
        stsh="background-color: black"
        self.setStyleSheet(stsh)
        n=170
        k=0
        pix=QPixmap('screenshot.png')

        for i in range (n):
            for j in range(n):
                k+=1
                pix1=pix.copy(i*(wdt/n),j*(hgt/n),wdt/n,hgt/n)
                lbl=QLabel(self)
                lbl.setObjectName("lbl"+str(i+1)+"w"+str(j))
                lbl.setGeometry(i*(wdt/n),j*(hgt/n),wdt/n,hgt/n)
                lbl.setPixmap(pix1)
        for z in range (169):
            self.move("lbl"+str(z+1)+"w"+str(z+1), wdt/n, hgt/n )



    def move(self, oName, oWdt, oHgt):
        obj1 = self.findChild(QLabel,oName)
        obj1.setGeometry(random.randint(0,800),random.randint(0,500),oWdt,oHgt)


app = QApplication(sys.argv)
window = FinalWind()
window.showFullScreen()
app.exec()
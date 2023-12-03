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
        n=5
        k=0
        pix=QPixmap('screenshot.png')

        for i in range (n):
            for j in range(n):
                k+=1
                pix1=pix.copy(i*(wdt/n),j*(hgt/n),wdt/n,hgt/n)
                lbl=QLabel(self)
                lbl.setObjectName("lbl"+str(k))
                lbl.setGeometry(i*(wdt/n),j*(hgt/n),wdt/n,hgt/n)
                lbl.setPixmap(pix1)







app = QApplication(sys.argv)
window = FinalWind()
window.showFullScreen()
app.exec()
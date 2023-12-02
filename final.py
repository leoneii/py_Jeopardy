import sys

from PySide6.QtCore import QSize, Qt, QVariantAnimation
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget




class FinalWind(QMainWindow):
    def __init__(self):
        super().__init__()
        stsh="background-color: black"
        self.setStyleSheet(stsh)






app = QApplication(sys.argv)
window = FinalWind()
window.showFullScreen()
app.exec_()
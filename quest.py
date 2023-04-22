import sys
from PySide6.QtCore import (QRect)
from PySide6.QtWidgets import (QApplication, QLabel,QWidget,QVBoxLayout,QHBoxLayout,
        QFrame)
from PySide6.QtGui import QFont


testtext="Шёл мужик попу кивал. Чем мужик попу кивал? "

font = QFont()
font.setFamilies([u"Serif"])
#font.setPointSize(22)
font.setBold(True)
#alignmentc=Qt.AlignmentFlag.AlignCenter



app = QApplication([])

class wing(QWidget):
    def __init__(self,txt):
        super().__init__()
        geometry = app.primaryScreen().availableGeometry()
        self.setGeometry(geometry)
        wdt=self.size().width()
        hgt=self.size().height()       
        self.setStyleSheet("""
        background-color: #0000aa;
        color: #FFFFaa;
        font-family: Titillium;
        font-size: 48px;
        text-align:center center;
        """)
#        text_widget = QLabel(txt)
#        text_widget.resize(960, 440)
#        text_widget.setAlignment(alignmentc)
        # content_layout = QVBoxLayout()
        # content_layout.addWidget(text_widget)
        # main_widget = QWidget()
        # main_widget.setLayout(content_layout)
        # layout = QHBoxLayout()
        # layout.addWidget(main_widget, 1)
        # self.setLayout(layout)

        self.textv = QLabel(self)
        self.textv.setObjectName(u"txtvopr")
        self.textv.setGeometry(QRect(100, 50, wdt-200, hgt-100))
        self.textv.setWordWrap(True)
        self.textv.setText(txt)
        leghtext= len(txt)

        font.setPointSize(hgt/(leghtext+18)+18)
        self.textv.setFont(font)
        self.textv.setFrameShape(QFrame.Box)
        self.textv.setAutoFillBackground(True)
#        self.textv.setStyleSheet(css)


ques=wing(testtext*5)
ques.showFullScreen()


app.exec()
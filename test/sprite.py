import random
import sys
import time

from PySide6 import QtGui, QtCore
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QObject, Qt, QTimer, QPoint
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QApplication, QMainWindow, QStackedWidget, \
    QHBoxLayout, QPushButton, QLabel
from random import randint, choice
from PySide6.QtWidgets import QGraphicsColorizeEffect


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.wdt = self.screen().size().width()
        self.hgt = self.screen().size().height()
        self.setGeometry(0, 0, self.wdt, self.hgt)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: rgba(10,20,90,30)")

        global k, g, r, leavt
        r = 20
        leavt = 1
        k = 300
        g = 0.2
        self.p = []
        self.px = []
        self.py = []
        self.pvx = []
        self.pvy = []
        self.r = []
        colors = ["rgba(255, 0, 0, 15)", "rgba(255, 255, 0, 15)", "rgba(0, 255, 0, 15)", "rgba(0, 255, 255, 15)",
                  "rgba(255, 200, 255, 15)"]
        self.colorize_effect = QGraphicsColorizeEffect()
        for i in range(k):
            r = random.randint(20, 60)
            self.r.append(r)
            pm = QLabel(self)
            pm.setParent(self)
            pm.setGeometry(40, 40, r, r)
            # pix = QPixmap("sprite.png")
            # pm.setPixmap(pix.scaled(pm.frameSize(),Qt.KeepAspectRatio))
            tmcol=choice(colors)
            pm.setStyleSheet("border-image: url(../img/icon/sprite.png); background-color: "+tmcol+";")
            # Create a QGraphicsColorizeEffect and set its color

            self.colorize_effect.setColor(QColor(choice(colors)))
            pm.setGraphicsEffect(self.colorize_effect)
            # pm.show()
            self.p.append(pm)
            if i < k / 2:
                self.x = random.randint(30, 40)
            else:
                self.x = random.randint(self.wdt - 40, self.wdt - 30)
            self.px.append(self.x)
            y = random.randint(int(self.hgt) - 150, int(self.hgt) - 10)
            self.py.append(y)
            vy = random.randint(-3, 3)
            self.pvy.append(vy)
            vx = random.randint(-3, 3)
            self.pvx.append(vx)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ptclsys)
        self.timer.start()

    def ptclsys(self):
        for i in range(k):

            self.pvy[i] += g
            if self.px[i] < 0:
                self.px[i] = 1
                self.pvx[i] *= -0.99
            if self.px[i] > self.wdt:
                self.px[i] = self.wdt - 1
                self.pvx[i] *= -0.99
            if self.py[i] < 0:
                self.py[i] = 1
                self.pvy[i] *= -0.99

            if self.pvy[i] > 5:
                self.r[i] *= 0.85
                self.pvy[i] = random.randint(3, 4)
                if self.px[i] <= self.wdt / 2:
                    self.pvx[i] = random.randint(0, 1)
                else:
                    self.pvx[i] = random.randint(-1, 0)
            if self.r[i] < 4:
                self.r[i] = 0
                self.py[i] = self.hgt + 10

            if self.py[i] > self.hgt:
                self.r[i] = random.randint(20, 60)
                self.pvx[i] = random.randint(-3, 3)
                self.pvy[i] = random.randint(-21, -10)
                if self.px[i] <= self.wdt / 2:
                    self.px[i] = random.randint(10, 30)
                else:
                    self.px[i] = random.randint(self.wdt - 40, self.wdt - 30)

            self.px[i] += int(self.pvx[i])
            self.py[i] += int(self.pvy[i])
            self.p[i].setGeometry(self.px[i], self.py[i], self.r[i], self.r[i])

        # time.sleep(0.005)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QStatusBar, QTableView, QTextEdit, QToolBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1488, 931)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 100000))
        self.action_openGame = QAction(MainWindow)
        self.action_openGame.setObjectName(u"action_openGame")
        self.action_newGame = QAction(MainWindow)
        self.action_newGame.setObjectName(u"action_newGame")
        self.action_saveGame = QAction(MainWindow)
        self.action_saveGame.setObjectName(u"action_saveGame")
        self.action_exportGame = QAction(MainWindow)
        self.action_exportGame.setObjectName(u"action_exportGame")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(16777215, 20000))
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setMaximumSize(QSize(21002, 1000))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.groupBox_6 = QGroupBox(self.splitter_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy2)
        self.groupBox_6.setMinimumSize(QSize(300, 0))
        self.groupBox_6.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_Cat = QGroupBox(self.groupBox_6)
        self.groupBox_Cat.setObjectName(u"groupBox_Cat")
        self.groupBox_Cat.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_Cat.sizePolicy().hasHeightForWidth())
        self.groupBox_Cat.setSizePolicy(sizePolicy3)
        self.groupBox_Cat.setMaximumSize(QSize(16777215, 100))
        self.groupBox_Cat.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_Cat.setFlat(False)
        self.groupBox_Cat.setCheckable(True)
        self.groupBox_Cat.setChecked(False)
        self.gridLayout = QGridLayout(self.groupBox_Cat)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_addCat = QPushButton(self.groupBox_Cat)
        self.pushButton_addCat.setObjectName(u"pushButton_addCat")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_addCat.sizePolicy().hasHeightForWidth())
        self.pushButton_addCat.setSizePolicy(sizePolicy4)
        self.pushButton_addCat.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pushButton_addCat, 1, 0, 1, 1)

        self.pushButton_EditCat = QPushButton(self.groupBox_Cat)
        self.pushButton_EditCat.setObjectName(u"pushButton_EditCat")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_EditCat.sizePolicy().hasHeightForWidth())
        self.pushButton_EditCat.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.pushButton_EditCat, 1, 1, 1, 1)

        self.pushButton__delCat = QPushButton(self.groupBox_Cat)
        self.pushButton__delCat.setObjectName(u"pushButton__delCat")
        sizePolicy4.setHeightForWidth(self.pushButton__delCat.sizePolicy().hasHeightForWidth())
        self.pushButton__delCat.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton__delCat, 1, 2, 1, 1)

        self.comboBox_Cat = QComboBox(self.groupBox_Cat)
        self.comboBox_Cat.addItem("")
        self.comboBox_Cat.setObjectName(u"comboBox_Cat")
        self.comboBox_Cat.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_Cat, 0, 0, 1, 3)


        self.verticalLayout.addWidget(self.groupBox_Cat)

        self.testButton = QPushButton(self.groupBox_6)
        self.testButton.setObjectName(u"testButton")

        self.verticalLayout.addWidget(self.testButton)

        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.tableView_themeTable = QTableView(self.groupBox_6)
        self.tableView_themeTable.setObjectName(u"tableView_themeTable")
        self.tableView_themeTable.setMaximumSize(QSize(16777215, 200))
        self.tableView_themeTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_themeTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableView_themeTable)

        self.groupBox_5 = QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_addTheme = QPushButton(self.groupBox_5)
        self.pushButton_addTheme.setObjectName(u"pushButton_addTheme")

        self.horizontalLayout_5.addWidget(self.pushButton_addTheme)

        self.pushButton_editTheme = QPushButton(self.groupBox_5)
        self.pushButton_editTheme.setObjectName(u"pushButton_editTheme")

        self.horizontalLayout_5.addWidget(self.pushButton_editTheme)

        self.pushButton_delTheme = QPushButton(self.groupBox_5)
        self.pushButton_delTheme.setObjectName(u"pushButton_delTheme")

        self.horizontalLayout_5.addWidget(self.pushButton_delTheme)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 10))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.tableView_questTable = QTableView(self.groupBox_6)
        self.tableView_questTable.setObjectName(u"tableView_questTable")
        self.tableView_questTable.setMaximumSize(QSize(16777215, 250))
        self.tableView_questTable.setDragEnabled(False)
        self.tableView_questTable.setDragDropMode(QAbstractItemView.DragOnly)
        self.tableView_questTable.setDefaultDropAction(Qt.MoveAction)
        self.tableView_questTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_questTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableView_questTable)

        self.frame_2 = QFrame(self.groupBox_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_Qdown = QPushButton(self.frame_2)
        self.pushButton_Qdown.setObjectName(u"pushButton_Qdown")

        self.horizontalLayout_7.addWidget(self.pushButton_Qdown)

        self.pushButton_Qup = QPushButton(self.frame_2)
        self.pushButton_Qup.setObjectName(u"pushButton_Qup")

        self.horizontalLayout_7.addWidget(self.pushButton_Qup)


        self.verticalLayout.addWidget(self.frame_2)

        self.pushButton_addQ = QPushButton(self.groupBox_6)
        self.pushButton_addQ.setObjectName(u"pushButton_addQ")

        self.verticalLayout.addWidget(self.pushButton_addQ)

        self.pushButton_delQ = QPushButton(self.groupBox_6)
        self.pushButton_delQ.setObjectName(u"pushButton_delQ")

        self.verticalLayout.addWidget(self.pushButton_delQ)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.splitter_2.addWidget(self.groupBox_6)
        self.groupBox_4 = QGroupBox(self.splitter_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setMaximumSize(QSize(20000, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_questText = QLabel(self.groupBox_4)
        self.label_questText.setObjectName(u"label_questText")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label_questText.setFont(font)
        self.label_questText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 80), stop:1 rgba(255, 255, 255, 155));")
        self.label_questText.setTextFormat(Qt.RichText)
        self.label_questText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_questText)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.textEdit_questText = QTextEdit(self.groupBox_4)
        self.textEdit_questText.setObjectName(u"textEdit_questText")
        self.textEdit_questText.setEnabled(False)
        self.textEdit_questText.setMinimumSize(QSize(0, 100))
        self.textEdit_questText.setMaximumSize(QSize(1000, 1000))
        font1 = QFont()
        font1.setPointSize(9)
        self.textEdit_questText.setFont(font1)
        self.textEdit_questText.setStyleSheet(u"color: rgb(1, 27, 113);")

        self.horizontalLayout_11.addWidget(self.textEdit_questText)

        self.frame_4 = QFrame(self.groupBox_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(100, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_questPix = QLabel(self.frame_4)
        self.label_questPix.setObjectName(u"label_questPix")
        self.label_questPix.setMinimumSize(QSize(180, 100))
        self.label_questPix.setMaximumSize(QSize(230, 200))
        self.label_questPix.setPixmap(QPixmap(u"../testpy8/img/dog.jpg"))
        self.label_questPix.setScaledContents(False)
        self.label_questPix.setWordWrap(False)

        self.verticalLayout_11.addWidget(self.label_questPix)


        self.horizontalLayout_11.addWidget(self.frame_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_Qpix = QFrame(self.groupBox_4)
        self.frame_Qpix.setObjectName(u"frame_Qpix")
        self.frame_Qpix.setEnabled(False)
        self.frame_Qpix.setMinimumSize(QSize(0, 0))
        self.frame_Qpix.setMaximumSize(QSize(1000, 1000))
        self.frame_Qpix.setFrameShape(QFrame.StyledPanel)
        self.frame_Qpix.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_Qpix)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_quiestPict = QLabel(self.frame_Qpix)
        self.label_quiestPict.setObjectName(u"label_quiestPict")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_quiestPict.setFont(font2)
        self.label_quiestPict.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_quiestPict)

        self.toolButton_selQpix = QToolButton(self.frame_Qpix)
        self.toolButton_selQpix.setObjectName(u"toolButton_selQpix")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.toolButton_selQpix.sizePolicy().hasHeightForWidth())
        self.toolButton_selQpix.setSizePolicy(sizePolicy6)

        self.verticalLayout_7.addWidget(self.toolButton_selQpix)

        self.toolButton_delQpix = QToolButton(self.frame_Qpix)
        self.toolButton_delQpix.setObjectName(u"toolButton_delQpix")
        sizePolicy6.setHeightForWidth(self.toolButton_delQpix.sizePolicy().hasHeightForWidth())
        self.toolButton_delQpix.setSizePolicy(sizePolicy6)

        self.verticalLayout_7.addWidget(self.toolButton_delQpix)


        self.horizontalLayout.addWidget(self.frame_Qpix)


        self.horizontalLayout_11.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_isBonus = QCheckBox(self.groupBox_4)
        self.checkBox_isBonus.setObjectName(u"checkBox_isBonus")
        self.checkBox_isBonus.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.checkBox_isBonus)

        self.spinBox_costQuest = QSpinBox(self.groupBox_4)
        self.spinBox_costQuest.setObjectName(u"spinBox_costQuest")
        self.spinBox_costQuest.setEnabled(False)
        self.spinBox_costQuest.setMinimumSize(QSize(110, 0))
        self.spinBox_costQuest.setMaximumSize(QSize(60, 16777215))
        self.spinBox_costQuest.setMaximum(70)
        self.spinBox_costQuest.setSingleStep(10)
        self.spinBox_costQuest.setValue(30)

        self.horizontalLayout_3.addWidget(self.spinBox_costQuest)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_answerText = QLabel(self.groupBox_4)
        self.label_answerText.setObjectName(u"label_answerText")
        self.label_answerText.setFont(font2)
        self.label_answerText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 80), stop:1 rgba(255, 255, 255, 155));")
        self.label_answerText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_answerText)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.textEdit_answerText = QTextEdit(self.groupBox_4)
        self.textEdit_answerText.setObjectName(u"textEdit_answerText")
        self.textEdit_answerText.setEnabled(False)
        self.textEdit_answerText.setMinimumSize(QSize(0, 100))
        self.textEdit_answerText.setMaximumSize(QSize(1000, 1000))
        self.textEdit_answerText.setFont(font1)
        self.textEdit_answerText.setStyleSheet(u"color: rgb(1, 27, 113);")

        self.horizontalLayout_12.addWidget(self.textEdit_answerText)

        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(100, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_answerPix = QLabel(self.frame_5)
        self.label_answerPix.setObjectName(u"label_answerPix")
        self.label_answerPix.setMinimumSize(QSize(180, 100))
        self.label_answerPix.setMaximumSize(QSize(230, 200))
        self.label_answerPix.setPixmap(QPixmap(u"../testpy8/img/gepard.webp"))
        self.label_answerPix.setScaledContents(False)

        self.verticalLayout_12.addWidget(self.label_answerPix)


        self.horizontalLayout_12.addWidget(self.frame_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_Apix = QFrame(self.groupBox_4)
        self.frame_Apix.setObjectName(u"frame_Apix")
        self.frame_Apix.setEnabled(False)
        self.frame_Apix.setMaximumSize(QSize(1000, 1000))
        self.frame_Apix.setFrameShape(QFrame.StyledPanel)
        self.frame_Apix.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_Apix)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_answPict = QLabel(self.frame_Apix)
        self.label_answPict.setObjectName(u"label_answPict")
        self.label_answPict.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_answPict)

        self.toolButton_selApix = QToolButton(self.frame_Apix)
        self.toolButton_selApix.setObjectName(u"toolButton_selApix")
        sizePolicy6.setHeightForWidth(self.toolButton_selApix.sizePolicy().hasHeightForWidth())
        self.toolButton_selApix.setSizePolicy(sizePolicy6)

        self.verticalLayout_6.addWidget(self.toolButton_selApix)

        self.toolButton_delApix = QToolButton(self.frame_Apix)
        self.toolButton_delApix.setObjectName(u"toolButton_delApix")
        sizePolicy6.setHeightForWidth(self.toolButton_delApix.sizePolicy().hasHeightForWidth())
        self.toolButton_delApix.setSizePolicy(sizePolicy6)

        self.verticalLayout_6.addWidget(self.toolButton_delApix)


        self.horizontalLayout_2.addWidget(self.frame_Apix)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.label_tooltipText = QLabel(self.groupBox_4)
        self.label_tooltipText.setObjectName(u"label_tooltipText")
        self.label_tooltipText.setFont(font2)
        self.label_tooltipText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 80), stop:1 rgba(255, 255, 255, 155));")
        self.label_tooltipText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_tooltipText)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.textEdit_tooltipText = QTextEdit(self.groupBox_4)
        self.textEdit_tooltipText.setObjectName(u"textEdit_tooltipText")
        self.textEdit_tooltipText.setEnabled(True)
        self.textEdit_tooltipText.setMinimumSize(QSize(0, 100))
        self.textEdit_tooltipText.setMaximumSize(QSize(1000, 1000))
        self.textEdit_tooltipText.setFont(font1)
        self.textEdit_tooltipText.setStyleSheet(u"color: rgb(1, 27, 113);")

        self.horizontalLayout_13.addWidget(self.textEdit_tooltipText)

        self.frame_6 = QFrame(self.groupBox_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(100, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_toolPix = QLabel(self.frame_6)
        self.label_toolPix.setObjectName(u"label_toolPix")
        self.label_toolPix.setMinimumSize(QSize(180, 100))
        self.label_toolPix.setMaximumSize(QSize(230, 200))
        self.label_toolPix.setScaledContents(False)

        self.horizontalLayout_17.addWidget(self.label_toolPix)


        self.horizontalLayout_13.addWidget(self.frame_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_Tpix = QFrame(self.groupBox_4)
        self.frame_Tpix.setObjectName(u"frame_Tpix")
        self.frame_Tpix.setEnabled(False)
        self.frame_Tpix.setMaximumSize(QSize(1000, 1000))
        self.frame_Tpix.setFrameShape(QFrame.StyledPanel)
        self.frame_Tpix.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_Tpix)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.frame_Tpix)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_7)

        self.toolButton_selTpix = QToolButton(self.frame_Tpix)
        self.toolButton_selTpix.setObjectName(u"toolButton_selTpix")
        sizePolicy6.setHeightForWidth(self.toolButton_selTpix.sizePolicy().hasHeightForWidth())
        self.toolButton_selTpix.setSizePolicy(sizePolicy6)

        self.verticalLayout_3.addWidget(self.toolButton_selTpix)

        self.toolButton_delTpix = QToolButton(self.frame_Tpix)
        self.toolButton_delTpix.setObjectName(u"toolButton_delTpix")
        sizePolicy6.setHeightForWidth(self.toolButton_delTpix.sizePolicy().hasHeightForWidth())
        self.toolButton_delTpix.setSizePolicy(sizePolicy6)

        self.verticalLayout_3.addWidget(self.toolButton_delTpix)


        self.horizontalLayout_10.addWidget(self.frame_Tpix)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_9 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_9)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.spinBox_costTooltip = QSpinBox(self.groupBox_4)
        self.spinBox_costTooltip.setObjectName(u"spinBox_costTooltip")
        self.spinBox_costTooltip.setMinimumSize(QSize(110, 0))
        self.spinBox_costTooltip.setMaximum(100)
        self.spinBox_costTooltip.setSingleStep(5)
        self.spinBox_costTooltip.setValue(0)

        self.horizontalLayout_14.addWidget(self.spinBox_costTooltip)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.groupBox = QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_Save = QPushButton(self.groupBox)
        self.pushButton_Save.setObjectName(u"pushButton_Save")
        self.pushButton_Save.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.pushButton_Save)

        self.pushButton_editQ = QPushButton(self.groupBox)
        self.pushButton_editQ.setObjectName(u"pushButton_editQ")

        self.horizontalLayout_4.addWidget(self.pushButton_editQ)

        self.pushButton_Cancel = QPushButton(self.groupBox)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")

        self.horizontalLayout_4.addWidget(self.pushButton_Cancel)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.splitter_2.addWidget(self.groupBox_4)
        self.toolBox = QToolBox(self.splitter_2)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy7)
        self.toolBox.setMinimumSize(QSize(250, 0))
        self.toolBox.setMaximumSize(QSize(400, 1000))
        self.toolBox.setFont(font1)
        self.toolBox.setFrameShape(QFrame.WinPanel)
        self.toolBox.setFrameShadow(QFrame.Raised)
        self.toolBox.setLineWidth(2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 354, 769))
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_editTeam = QPushButton(self.groupBox_2)
        self.pushButton_editTeam.setObjectName(u"pushButton_editTeam")
        font3 = QFont()
        font3.setPointSize(8)
        self.pushButton_editTeam.setFont(font3)

        self.gridLayout_3.addWidget(self.pushButton_editTeam, 4, 0, 1, 2)

        self.listView_teams = QListView(self.groupBox_2)
        self.listView_teams.setObjectName(u"listView_teams")

        self.gridLayout_3.addWidget(self.listView_teams, 2, 0, 1, 2)

        self.pushButton_delTeam = QPushButton(self.groupBox_2)
        self.pushButton_delTeam.setObjectName(u"pushButton_delTeam")
        sizePolicy4.setHeightForWidth(self.pushButton_delTeam.sizePolicy().hasHeightForWidth())
        self.pushButton_delTeam.setSizePolicy(sizePolicy4)
        self.pushButton_delTeam.setFont(font3)

        self.gridLayout_3.addWidget(self.pushButton_delTeam, 3, 1, 1, 1)

        self.pushButton_addTeam = QPushButton(self.groupBox_2)
        self.pushButton_addTeam.setObjectName(u"pushButton_addTeam")
        sizePolicy4.setHeightForWidth(self.pushButton_addTeam.sizePolicy().hasHeightForWidth())
        self.pushButton_addTeam.setSizePolicy(sizePolicy4)
        self.pushButton_addTeam.setMinimumSize(QSize(0, 0))
        self.pushButton_addTeam.setFont(font3)

        self.gridLayout_3.addWidget(self.pushButton_addTeam, 3, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_teamLogo = QLabel(self.frame_3)
        self.label_teamLogo.setObjectName(u"label_teamLogo")
        sizePolicy1.setHeightForWidth(self.label_teamLogo.sizePolicy().hasHeightForWidth())
        self.label_teamLogo.setSizePolicy(sizePolicy1)
        self.label_teamLogo.setMinimumSize(QSize(120, 120))
        self.label_teamLogo.setMaximumSize(QSize(16777215, 200))
        self.label_teamLogo.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_teamLogo)


        self.horizontalLayout_16.addWidget(self.frame_3)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(100, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_addTeamLogo = QPushButton(self.frame)
        self.pushButton_addTeamLogo.setObjectName(u"pushButton_addTeamLogo")
        sizePolicy2.setHeightForWidth(self.pushButton_addTeamLogo.sizePolicy().hasHeightForWidth())
        self.pushButton_addTeamLogo.setSizePolicy(sizePolicy2)
        self.pushButton_addTeamLogo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_8.addWidget(self.pushButton_addTeamLogo)

        self.pushButton_delTeamLogo = QPushButton(self.frame)
        self.pushButton_delTeamLogo.setObjectName(u"pushButton_delTeamLogo")
        sizePolicy2.setHeightForWidth(self.pushButton_delTeamLogo.sizePolicy().hasHeightForWidth())
        self.pushButton_delTeamLogo.setSizePolicy(sizePolicy2)
        self.pushButton_delTeamLogo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_8.addWidget(self.pushButton_delTeamLogo)


        self.horizontalLayout_16.addWidget(self.frame)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page, u"\u041a\u043e\u043c\u0430\u043d\u0434\u044b")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 354, 769))
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 6, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 5, 2, 1, 1)

        self.spinBox_pad = QSpinBox(self.page_3)
        self.spinBox_pad.setObjectName(u"spinBox_pad")
        self.spinBox_pad.setMinimum(1)
        self.spinBox_pad.setMaximum(15)
        self.spinBox_pad.setValue(5)

        self.gridLayout_5.addWidget(self.spinBox_pad, 2, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 4, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 6, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 6, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 4, 1, 1, 1)

        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButton_cancelSet = QPushButton(self.page_3)
        self.pushButton_cancelSet.setObjectName(u"pushButton_cancelSet")

        self.gridLayout_5.addWidget(self.pushButton_cancelSet, 8, 2, 1, 1)

        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 5, 1, 1, 1)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 4, 0, 1, 1)

        self.spinBox_timer = QSpinBox(self.page_3)
        self.spinBox_timer.setObjectName(u"spinBox_timer")
        self.spinBox_timer.setValue(30)

        self.gridLayout_5.addWidget(self.spinBox_timer, 0, 2, 1, 1)

        self.pushButton_saveSet = QPushButton(self.page_3)
        self.pushButton_saveSet.setObjectName(u"pushButton_saveSet")

        self.gridLayout_5.addWidget(self.pushButton_saveSet, 8, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.toolBox.addItem(self.page_3, u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 354, 769))
        self.toolBox.addItem(self.page_2, u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442")
        self.splitter_2.addWidget(self.toolBox)

        self.verticalLayout_5.addWidget(self.splitter_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1488, 30))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_openGame)
        self.menu.addAction(self.action_newGame)
        self.menu.addAction(self.action_saveGame)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exportGame)
        self.menu.addAction(self.action_8)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_5)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_openGame.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.action_newGame.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.action_saveGame.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.action_exportGame.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.groupBox_6.setTitle("")
        self.groupBox_Cat.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.pushButton_addCat.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_EditCat.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton__delCat.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.comboBox_Cat.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))

        self.testButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u044b", None))
        self.groupBox_5.setTitle("")
        self.pushButton_addTheme.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_editTheme.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_delTheme.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441\u044b", None))
        self.pushButton_Qdown.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.pushButton_Qup.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_addQ.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443 \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432", None))
        self.pushButton_delQ.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443 \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432 \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u0446\u0435\u043d\u044b", None))
        self.groupBox_4.setTitle("")
        self.label_questText.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441", None))
        self.textEdit_questText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif';\">\u0428\u0442\u043e \u0437\u0430 \u0441\u043e\u0431\u0430\u043a\u0430</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif';\"><br /></p></body></html>", None))
        self.label_questPix.setText("")
        self.label_quiestPict.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.toolButton_selQpix.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.toolButton_delQpix.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.checkBox_isBonus.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043d\u0443\u0441\u043d\u044b\u0439 \u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.label_answerText.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442", None))
        self.textEdit_answerText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif';\">\u0421\u043e\u0431\u0430\u043a\u0430 \u043b\u0435\u0436\u0430\u043a\u0430</span></p></body></html>", None))
        self.label_answerPix.setText("")
        self.label_answPict.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.toolButton_selApix.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.toolButton_delApix.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_tooltipText.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430", None))
        self.label_toolPix.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.toolButton_selTpix.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.toolButton_delTpix.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438", None))
        self.groupBox.setTitle("")
        self.pushButton_Save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_editQ.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle("")
        self.pushButton_editTeam.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_delTeam.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_addTeam.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_teamLogo.setText("")
        self.pushButton_addTeamLogo.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.pushButton_delTeamLogo.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0442\u0443\u043f\u044b ", None))
        self.pushButton_cancelSet.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440 \u043e\u0442\u0432\u0435\u0442\u0430, \u0441\u0435\u043a.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_saveSet.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi


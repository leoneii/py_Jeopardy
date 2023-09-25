# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QSplitter, QStatusBar,
    QTableView, QTextEdit, QToolBox, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1238, 846)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.groupBox_6 = QGroupBox(self.splitter_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy1)
        self.groupBox_6.setMinimumSize(QSize(400, 0))
        self.groupBox_6.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_Cat = QGroupBox(self.groupBox_6)
        self.groupBox_Cat.setObjectName(u"groupBox_Cat")
        self.groupBox_Cat.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_Cat.sizePolicy().hasHeightForWidth())
        self.groupBox_Cat.setSizePolicy(sizePolicy2)
        self.groupBox_Cat.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_Cat.setFlat(False)
        self.groupBox_Cat.setCheckable(True)
        self.groupBox_Cat.setChecked(False)
        self.gridLayout = QGridLayout(self.groupBox_Cat)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_addCat = QPushButton(self.groupBox_Cat)
        self.pushButton_addCat.setObjectName(u"pushButton_addCat")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_addCat.sizePolicy().hasHeightForWidth())
        self.pushButton_addCat.setSizePolicy(sizePolicy3)
        self.pushButton_addCat.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pushButton_addCat, 1, 0, 1, 1)

        self.pushButton_EditCat = QPushButton(self.groupBox_Cat)
        self.pushButton_EditCat.setObjectName(u"pushButton_EditCat")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_EditCat.sizePolicy().hasHeightForWidth())
        self.pushButton_EditCat.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton_EditCat, 1, 1, 1, 1)

        self.pushButton__delCat = QPushButton(self.groupBox_Cat)
        self.pushButton__delCat.setObjectName(u"pushButton__delCat")
        sizePolicy3.setHeightForWidth(self.pushButton__delCat.sizePolicy().hasHeightForWidth())
        self.pushButton__delCat.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.pushButton__delCat, 1, 2, 1, 1)

        self.comboBox_Cat = QComboBox(self.groupBox_Cat)
        self.comboBox_Cat.addItem("")
        self.comboBox_Cat.setObjectName(u"comboBox_Cat")
        self.comboBox_Cat.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_Cat, 0, 0, 1, 3)


        self.verticalLayout.addWidget(self.groupBox_Cat)

        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.tableView_themeTable = QTableView(self.groupBox_6)
        self.tableView_themeTable.setObjectName(u"tableView_themeTable")
        self.tableView_themeTable.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout.addWidget(self.tableView_themeTable)

        self.groupBox_5 = QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
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
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.tableView_questTable = QTableView(self.groupBox_6)
        self.tableView_questTable.setObjectName(u"tableView_questTable")

        self.verticalLayout.addWidget(self.tableView_questTable)

        self.splitter_2.addWidget(self.groupBox_6)
        self.groupBox_4 = QGroupBox(self.splitter_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.groupBox_4.setMinimumSize(QSize(400, 0))
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

        self.textEdit_questText = QTextEdit(self.groupBox_4)
        self.textEdit_questText.setObjectName(u"textEdit_questText")
        self.textEdit_questText.setMinimumSize(QSize(0, 80))
        font1 = QFont()
        font1.setPointSize(9)
        self.textEdit_questText.setFont(font1)

        self.verticalLayout_2.addWidget(self.textEdit_questText)

        self.label_quiestPict = QLabel(self.groupBox_4)
        self.label_quiestPict.setObjectName(u"label_quiestPict")
        font2 = QFont()
        font2.setPointSize(8)
        self.label_quiestPict.setFont(font2)
        self.label_quiestPict.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_quiestPict)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_questImage = QLabel(self.groupBox_4)
        self.label_questImage.setObjectName(u"label_questImage")
        self.label_questImage.setMinimumSize(QSize(0, 100))
        self.label_questImage.setMaximumSize(QSize(16777215, 380))
        self.label_questImage.setPixmap(QPixmap(u"../testpy8/img/dog.jpg"))
        self.label_questImage.setScaledContents(True)
        self.label_questImage.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label_questImage)

        self.toolButton_2 = QToolButton(self.groupBox_4)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.toolButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.spinBox_costQuest = QSpinBox(self.groupBox_4)
        self.spinBox_costQuest.setObjectName(u"spinBox_costQuest")
        self.spinBox_costQuest.setMaximumSize(QSize(60, 16777215))
        self.spinBox_costQuest.setValue(30)

        self.horizontalLayout_3.addWidget(self.spinBox_costQuest)

        self.radioButton_isBonus = QRadioButton(self.groupBox_4)
        self.radioButton_isBonus.setObjectName(u"radioButton_isBonus")
        self.radioButton_isBonus.setChecked(False)

        self.horizontalLayout_3.addWidget(self.radioButton_isBonus)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_answerText = QLabel(self.groupBox_4)
        self.label_answerText.setObjectName(u"label_answerText")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_answerText.setFont(font3)
        self.label_answerText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 80), stop:1 rgba(255, 255, 255, 155));")
        self.label_answerText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_answerText)

        self.textEdit_answerText = QTextEdit(self.groupBox_4)
        self.textEdit_answerText.setObjectName(u"textEdit_answerText")
        self.textEdit_answerText.setMinimumSize(QSize(0, 80))
        self.textEdit_answerText.setFont(font1)

        self.verticalLayout_2.addWidget(self.textEdit_answerText)

        self.label_answPict = QLabel(self.groupBox_4)
        self.label_answPict.setObjectName(u"label_answPict")
        self.label_answPict.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_answPict)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_answerImage = QLabel(self.groupBox_4)
        self.label_answerImage.setObjectName(u"label_answerImage")
        self.label_answerImage.setMinimumSize(QSize(0, 100))
        self.label_answerImage.setMaximumSize(QSize(16777215, 380))
        self.label_answerImage.setPixmap(QPixmap(u"../testpy8/img/gepard.webp"))
        self.label_answerImage.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_answerImage)

        self.toolButton_3 = QToolButton(self.groupBox_4)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy5.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.toolButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.groupBox_tooltip = QGroupBox(self.groupBox_4)
        self.groupBox_tooltip.setObjectName(u"groupBox_tooltip")
        self.groupBox_tooltip.setAlignment(Qt.AlignCenter)
        self.groupBox_tooltip.setCheckable(True)
        self.gridLayout_7 = QGridLayout(self.groupBox_tooltip)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.textEdit_tooltipText = QTextEdit(self.groupBox_tooltip)
        self.textEdit_tooltipText.setObjectName(u"textEdit_tooltipText")
        self.textEdit_tooltipText.setFont(font1)

        self.gridLayout_7.addWidget(self.textEdit_tooltipText, 0, 0, 1, 3)

        self.spinBox_costTooltip = QSpinBox(self.groupBox_tooltip)
        self.spinBox_costTooltip.setObjectName(u"spinBox_costTooltip")
        self.spinBox_costTooltip.setValue(30)

        self.gridLayout_7.addWidget(self.spinBox_costTooltip, 2, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_9, 2, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_tooltip)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_tooltip)

        self.groupBox = QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_addQ = QPushButton(self.groupBox)
        self.pushButton_addQ.setObjectName(u"pushButton_addQ")

        self.horizontalLayout_4.addWidget(self.pushButton_addQ)

        self.pushButton_editQ = QPushButton(self.groupBox)
        self.pushButton_editQ.setObjectName(u"pushButton_editQ")

        self.horizontalLayout_4.addWidget(self.pushButton_editQ)

        self.pushButton_delQ = QPushButton(self.groupBox)
        self.pushButton_delQ.setObjectName(u"pushButton_delQ")

        self.horizontalLayout_4.addWidget(self.pushButton_delQ)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.splitter_2.addWidget(self.groupBox_4)
        self.toolBox = QToolBox(self.splitter_2)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy6)
        self.toolBox.setMinimumSize(QSize(300, 0))
        self.toolBox.setMaximumSize(QSize(400, 16777215))
        self.toolBox.setFont(font1)
        self.toolBox.setFrameShape(QFrame.WinPanel)
        self.toolBox.setFrameShadow(QFrame.Raised)
        self.toolBox.setLineWidth(2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 308, 699))
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.toolButton = QToolButton(self.page)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy5.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.toolButton, 2, 1, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy7)
        self.label.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.listView_teams = QListView(self.groupBox_2)
        self.listView_teams.setObjectName(u"listView_teams")

        self.gridLayout_3.addWidget(self.listView_teams, 2, 0, 1, 2)

        self.pushButton_addTeam = QPushButton(self.groupBox_2)
        self.pushButton_addTeam.setObjectName(u"pushButton_addTeam")
        sizePolicy3.setHeightForWidth(self.pushButton_addTeam.sizePolicy().hasHeightForWidth())
        self.pushButton_addTeam.setSizePolicy(sizePolicy3)
        self.pushButton_addTeam.setMinimumSize(QSize(0, 0))
        self.pushButton_addTeam.setFont(font2)

        self.gridLayout_3.addWidget(self.pushButton_addTeam, 3, 0, 1, 1)

        self.pushButton_delTeam = QPushButton(self.groupBox_2)
        self.pushButton_delTeam.setObjectName(u"pushButton_delTeam")
        sizePolicy3.setHeightForWidth(self.pushButton_delTeam.sizePolicy().hasHeightForWidth())
        self.pushButton_delTeam.setSizePolicy(sizePolicy3)
        self.pushButton_delTeam.setFont(font2)

        self.gridLayout_3.addWidget(self.pushButton_delTeam, 3, 1, 1, 1)

        self.pushButton_editTeam = QPushButton(self.groupBox_2)
        self.pushButton_editTeam.setObjectName(u"pushButton_editTeam")
        self.pushButton_editTeam.setFont(font2)

        self.gridLayout_3.addWidget(self.pushButton_editTeam, 4, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 2)

        self.toolBox.addItem(self.page, u"\u041a\u043e\u043c\u0430\u043d\u0434\u044b")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 308, 699))
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 5, 1, 1, 1)

        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.spinBox_pad = QSpinBox(self.page_3)
        self.spinBox_pad.setObjectName(u"spinBox_pad")
        self.spinBox_pad.setMinimum(1)
        self.spinBox_pad.setMaximum(15)
        self.spinBox_pad.setValue(5)

        self.gridLayout_5.addWidget(self.spinBox_pad, 2, 2, 1, 1)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 4, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 6, 1, 1, 1)

        self.spinBox_timer = QSpinBox(self.page_3)
        self.spinBox_timer.setObjectName(u"spinBox_timer")
        self.spinBox_timer.setValue(30)

        self.gridLayout_5.addWidget(self.spinBox_timer, 0, 2, 1, 1)

        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 6, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 4, 2, 1, 1)

        self.pushButton_cancelSet = QPushButton(self.page_3)
        self.pushButton_cancelSet.setObjectName(u"pushButton_cancelSet")

        self.gridLayout_5.addWidget(self.pushButton_cancelSet, 8, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 4, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 6, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 5, 2, 1, 1)

        self.pushButton_saveSet = QPushButton(self.page_3)
        self.pushButton_saveSet.setObjectName(u"pushButton_saveSet")

        self.gridLayout_5.addWidget(self.pushButton_saveSet, 8, 1, 1, 1)

        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 5, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout_5.addLayout(self.verticalLayout_3, 7, 0, 1, 1)

        self.toolBox.addItem(self.page_3, u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 308, 699))
        self.toolBox.addItem(self.page_2, u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442")
        self.splitter_2.addWidget(self.toolBox)

        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1238, 21))
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
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_8)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_5)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.groupBox_6.setTitle("")
        self.groupBox_Cat.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.pushButton_addCat.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_EditCat.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton__delCat.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.comboBox_Cat.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u044b", None))
        self.groupBox_5.setTitle("")
        self.pushButton_addTheme.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_editTheme.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_delTheme.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441\u044b", None))
        self.groupBox_4.setTitle("")
        self.label_questText.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.textEdit_questText.setDocumentTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441", None))
        self.textEdit_questText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>\u0412\u043e\u043f\u0440\u043e\u0441</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif';\">\u0428\u0442\u043e \u0437\u0430 \u0441\u043e\u0431\u0430\u043a\u0430</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif';\"><br /></p></body></html>", None))
        self.label_quiestPict.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u0432\u0440\u043f\u0440\u043e\u0441\u0430", None))
        self.label_questImage.setText("")
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"    \u0426\u0435\u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.radioButton_isBonus.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043d\u0443\u0441\u043d\u044b\u0439 \u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.label_answerText.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u043e\u0442\u0432\u0435\u0442\u0430", None))
        self.textEdit_answerText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif';\">\u0421\u043e\u0431\u0430\u043a\u0430 \u043b\u0435\u0436\u0430\u043a\u0430</span></p></body></html>", None))
        self.label_answPict.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043e\u0442\u0432\u0435\u0442\u0430", None))
        self.label_answerImage.setText("")
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_tooltip.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438", None))
        self.groupBox.setTitle("")
        self.pushButton_addQ.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_editQ.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_delQ.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText("")
        self.groupBox_2.setTitle("")
        self.pushButton_addTeam.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_delTeam.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_editTeam.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440 \u043e\u0442\u0432\u0435\u0442\u0430, \u0441\u0435\u043a.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0442\u0443\u043f\u044b ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_cancelSet.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_saveSet.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi


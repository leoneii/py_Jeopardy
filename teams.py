# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teams.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QToolBox,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 582)
        Dialog.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolBox = QToolBox(Dialog)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QSize(250, 0))
        self.toolBox.setMaximumSize(QSize(400, 1000))
        font = QFont()
        font.setPointSize(9)
        self.toolBox.setFont(font)
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.toolBox.setLineWidth(2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 388, 477))
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_3 = QGroupBox(self.page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_editTeam = QPushButton(self.groupBox_3)
        self.pushButton_editTeam.setObjectName(u"pushButton_editTeam")
        font1 = QFont()
        font1.setPointSize(8)
        self.pushButton_editTeam.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton_editTeam, 4, 0, 1, 2)

        self.listView_teams = QListView(self.groupBox_3)
        self.listView_teams.setObjectName(u"listView_teams")

        self.gridLayout_4.addWidget(self.listView_teams, 2, 0, 1, 2)

        self.pushButton_delTeam = QPushButton(self.groupBox_3)
        self.pushButton_delTeam.setObjectName(u"pushButton_delTeam")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_delTeam.sizePolicy().hasHeightForWidth())
        self.pushButton_delTeam.setSizePolicy(sizePolicy1)
        self.pushButton_delTeam.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton_delTeam, 3, 1, 1, 1)

        self.pushButton_addTeam = QPushButton(self.groupBox_3)
        self.pushButton_addTeam.setObjectName(u"pushButton_addTeam")
        sizePolicy1.setHeightForWidth(self.pushButton_addTeam.sizePolicy().hasHeightForWidth())
        self.pushButton_addTeam.setSizePolicy(sizePolicy1)
        self.pushButton_addTeam.setMinimumSize(QSize(0, 0))
        self.pushButton_addTeam.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton_addTeam, 3, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_teamLogo = QLabel(self.frame_3)
        self.label_teamLogo.setObjectName(u"label_teamLogo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_teamLogo.sizePolicy().hasHeightForWidth())
        self.label_teamLogo.setSizePolicy(sizePolicy2)
        self.label_teamLogo.setMinimumSize(QSize(120, 120))
        self.label_teamLogo.setMaximumSize(QSize(16777215, 200))
        self.label_teamLogo.setScaledContents(False)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_addTeamLogo.sizePolicy().hasHeightForWidth())
        self.pushButton_addTeamLogo.setSizePolicy(sizePolicy3)
        self.pushButton_addTeamLogo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_8.addWidget(self.pushButton_addTeamLogo)

        self.pushButton_delTeamLogo = QPushButton(self.frame)
        self.pushButton_delTeamLogo.setObjectName(u"pushButton_delTeamLogo")
        sizePolicy3.setHeightForWidth(self.pushButton_delTeamLogo.sizePolicy().hasHeightForWidth())
        self.pushButton_delTeamLogo.setSizePolicy(sizePolicy3)
        self.pushButton_delTeamLogo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_8.addWidget(self.pushButton_delTeamLogo)


        self.horizontalLayout_16.addWidget(self.frame)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page, u"\u041a\u043e\u043c\u0430\u043d\u0434\u044b")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 388, 477))
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.toolBox.addItem(self.page_3, u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 388, 477))
        self.toolBox.addItem(self.page_2, u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442")

        self.horizontalLayout.addWidget(self.toolBox)


        self.retranslateUi(Dialog)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043a\u043e\u043c\u0430\u043d\u0434", None))
        self.groupBox_3.setTitle("")
        self.pushButton_editTeam.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_delTeam.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_addTeam.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.label_teamLogo.setText("")
        self.pushButton_addTeamLogo.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.pushButton_delTeamLogo.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(530, 168)
        Dialog.setMaximumSize(QSize(530, 168))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_categCount = QComboBox(Dialog)
        self.comboBox_categCount.addItem("")
        self.comboBox_categCount.addItem("")
        self.comboBox_categCount.addItem("")
        self.comboBox_categCount.addItem("")
        self.comboBox_categCount.setObjectName(u"comboBox_categCount")

        self.gridLayout.addWidget(self.comboBox_categCount, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox_themeCount = QComboBox(Dialog)
        self.comboBox_themeCount.addItem("")
        self.comboBox_themeCount.addItem("")
        self.comboBox_themeCount.addItem("")
        self.comboBox_themeCount.addItem("")
        self.comboBox_themeCount.setObjectName(u"comboBox_themeCount")

        self.gridLayout.addWidget(self.comboBox_themeCount, 1, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.comboBox_questCount = QComboBox(Dialog)
        self.comboBox_questCount.addItem("")
        self.comboBox_questCount.addItem("")
        self.comboBox_questCount.addItem("")
        self.comboBox_questCount.addItem("")
        self.comboBox_questCount.addItem("")
        self.comboBox_questCount.setObjectName(u"comboBox_questCount")

        self.gridLayout.addWidget(self.comboBox_questCount, 2, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.comboBox_questCount_2 = QComboBox(Dialog)
        self.comboBox_questCount_2.addItem("")
        self.comboBox_questCount_2.addItem("")
        self.comboBox_questCount_2.addItem("")
        self.comboBox_questCount_2.addItem("")
        self.comboBox_questCount_2.addItem("")
        self.comboBox_questCount_2.setObjectName(u"comboBox_questCount_2")

        self.gridLayout.addWidget(self.comboBox_questCount_2, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 2, 1, 1)

        self.pushButton_Create = QPushButton(Dialog)
        self.pushButton_Create.setObjectName(u"pushButton_Create")

        self.gridLayout.addWidget(self.pushButton_Create, 0, 3, 1, 1)

        self.pushButton_Cancel = QPushButton(Dialog)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setMaximumSize(QSize(450, 110))

        self.gridLayout.addWidget(self.pushButton_Cancel, 1, 3, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0432 \u0438\u0433\u0440\u0435", None))
        self.comboBox_categCount.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_categCount.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_categCount.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))
        self.comboBox_categCount.setItemText(3, QCoreApplication.translate("Dialog", u"4", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0435\u043c \u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.comboBox_themeCount.setItemText(0, QCoreApplication.translate("Dialog", u"3", None))
        self.comboBox_themeCount.setItemText(1, QCoreApplication.translate("Dialog", u"4", None))
        self.comboBox_themeCount.setItemText(2, QCoreApplication.translate("Dialog", u"5", None))
        self.comboBox_themeCount.setItemText(3, QCoreApplication.translate("Dialog", u"6", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432 \u0432 \u0442\u0435\u043c\u0435", None))
        self.comboBox_questCount.setItemText(0, QCoreApplication.translate("Dialog", u"3", None))
        self.comboBox_questCount.setItemText(1, QCoreApplication.translate("Dialog", u"4", None))
        self.comboBox_questCount.setItemText(2, QCoreApplication.translate("Dialog", u"5", None))
        self.comboBox_questCount.setItemText(3, QCoreApplication.translate("Dialog", u"6", None))
        self.comboBox_questCount.setItemText(4, QCoreApplication.translate("Dialog", u"7", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u0430\u043d\u0434 \u0432 \u0438\u0433\u0440\u0435", None))
        self.comboBox_questCount_2.setItemText(0, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_questCount_2.setItemText(1, QCoreApplication.translate("Dialog", u"3", None))
        self.comboBox_questCount_2.setItemText(2, QCoreApplication.translate("Dialog", u"4", None))
        self.comboBox_questCount_2.setItemText(3, QCoreApplication.translate("Dialog", u"5", None))
        self.comboBox_questCount_2.setItemText(4, QCoreApplication.translate("Dialog", u"6", None))

        self.pushButton_Create.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi


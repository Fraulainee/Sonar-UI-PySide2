# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sonar_guibTkEDM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1112, 861)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent; \n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #040f13;\n"
"}\n"
"#side_menu{\n"
"	/* background-color: #071e26; */\n"
"	background-color:rgb(56,58,89);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"#main_body{\n"
"	/* background-color: #071e26; */\n"
"	background-color:rgb(56,58,89);\n"
"	border-radius: 10px;\n"
"}\n"
"#main_data, #main_data_sidebar{\n"
"	background-color:#fff;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menubtn = QPushButton(self.frame)
        self.menubtn.setObjectName(u"menubtn")
        self.menubtn.setMinimumSize(QSize(0, 35))
        self.menubtn.setMaximumSize(QSize(16777215, 35))
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn.setIcon(icon)
        self.menubtn.setIconSize(QSize(24, 24))
        self.menubtn.setCheckable(True)
        self.menubtn.setChecked(False)

        self.horizontalLayout_4.addWidget(self.menubtn, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Noto Sans Mono CJK TC")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_menu = QWidget(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setStyleSheet(u"#allBtn, #savedImgBtn{\n"
"	text-align: left;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 10, 5, 5)
        self.allBtn = QPushButton(self.frame_4)
        self.allBtn.setObjectName(u"allBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.allBtn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.allBtn)

        self.savedImgBtn = QPushButton(self.frame_4)
        self.savedImgBtn.setObjectName(u"savedImgBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.savedImgBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.savedImgBtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.side_menu)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_body = QWidget()
        self.main_body.setObjectName(u"main_body")
        self.horizontalLayout_5 = QHBoxLayout(self.main_body)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.main_data = QFrame(self.main_body)
        self.main_data.setObjectName(u"main_data")
        sizePolicy.setHeightForWidth(self.main_data.sizePolicy().hasHeightForWidth())
        self.main_data.setSizePolicy(sizePolicy)
        self.main_data.setFrameShape(QFrame.StyledPanel)
        self.main_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_data)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.main_data)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_7)

        self.mapwidget = QWidget(self.main_data)
        self.mapwidget.setObjectName(u"mapwidget")

        self.verticalLayout_4.addWidget(self.mapwidget)


        self.horizontalLayout_5.addWidget(self.main_data)

        self.main_data_sidebar = QFrame(self.main_body)
        self.main_data_sidebar.setObjectName(u"main_data_sidebar")
        self.main_data_sidebar.setMinimumSize(QSize(250, 0))
        self.main_data_sidebar.setMaximumSize(QSize(250, 16777215))
        self.main_data_sidebar.setFrameShape(QFrame.StyledPanel)
        self.main_data_sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_data_sidebar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_9 = QFrame(self.main_data_sidebar)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.main_data_sidebar)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_10)


        self.horizontalLayout_5.addWidget(self.main_data_sidebar)

        self.stackedWidget.addWidget(self.main_body)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menubtn.toggled.connect(self.frame_4.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menubtn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SONAR APP", None))
        self.allBtn.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.savedImgBtn.setText(QCoreApplication.translate("MainWindow", u"Saved Images", None))
    # retranslateUi


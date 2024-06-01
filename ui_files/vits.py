# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vits.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1187, 703)
        MainWindow.setMinimumSize(QSize(1027, 599))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(85, 170, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Active, QPalette.Link, brush7)
        brush8 = QBrush(QColor(255, 0, 127, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush9 = QBrush(QColor(44, 49, 60, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        brush10 = QBrush(QColor(210, 210, 210, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush11 = QBrush(QColor(255, 255, 255, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
        brush12 = QBrush(QColor(255, 255, 255, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"*{\n"
"background:  transparent;\n"
"border: none;\n"
"color: #fff ;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"}\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	borde"
                        "r: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border"
                        ": none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizon"
                        "tal\n"
"{\n"
"\n"
"}\n"
"QMessageBox {\n"
"    background-color: #161c21;\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: #F6F5F2;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"background-color: #05364F;")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/16x16/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle_menu.setIcon(icon)

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setStyleSheet(u"background-color: #161c21\n"
"")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_113 = QLabel(self.frame_label_top_btns)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(250, 0))
        self.label_113.setMaximumSize(QSize(150, 220))
        self.label_113.setStyleSheet(u"")
        self.label_113.setPixmap(QPixmap(u"icons/vist_trans.png"))
        self.label_113.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_113)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, 15, 9, 15)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy1.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
        self.btn_maximize_restore.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right)


        self.verticalLayout_2.addWidget(self.frame_top_btns)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy2)
        self.frame_left_menu.setMaximumSize(QSize(80, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_menus)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.btn_test = QPushButton(self.frame_menus)
        self.btn_test.setObjectName(u"btn_test")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_test.sizePolicy().hasHeightForWidth())
        self.btn_test.setSizePolicy(sizePolicy3)
        self.btn_test.setMinimumSize(QSize(62, 40))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_test.setFont(font2)
        self.btn_test.setLayoutDirection(Qt.LeftToRight)
        self.btn_test.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.btn_test)

        self.btn_test_3 = QPushButton(self.frame_menus)
        self.btn_test_3.setObjectName(u"btn_test_3")
        sizePolicy3.setHeightForWidth(self.btn_test_3.sizePolicy().hasHeightForWidth())
        self.btn_test_3.setSizePolicy(sizePolicy3)
        self.btn_test_3.setMinimumSize(QSize(62, 40))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(7)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_test_3.setFont(font3)
        self.btn_test_3.setLayoutDirection(Qt.LeftToRight)
        self.btn_test_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.btn_test_3)

        self.btn_test_5 = QPushButton(self.frame_menus)
        self.btn_test_5.setObjectName(u"btn_test_5")
        sizePolicy3.setHeightForWidth(self.btn_test_5.sizePolicy().hasHeightForWidth())
        self.btn_test_5.setSizePolicy(sizePolicy3)
        self.btn_test_5.setMinimumSize(QSize(62, 40))
        self.btn_test_5.setFont(font2)
        self.btn_test_5.setLayoutDirection(Qt.LeftToRight)
        self.btn_test_5.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.btn_test_5)

        self.btn_test_4 = QPushButton(self.frame_menus)
        self.btn_test_4.setObjectName(u"btn_test_4")
        sizePolicy3.setHeightForWidth(self.btn_test_4.sizePolicy().hasHeightForWidth())
        self.btn_test_4.setSizePolicy(sizePolicy3)
        self.btn_test_4.setMinimumSize(QSize(62, 40))
        self.btn_test_4.setFont(font2)
        self.btn_test_4.setLayoutDirection(Qt.LeftToRight)
        self.btn_test_4.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.btn_test_4)

        self.btn_test_2 = QPushButton(self.frame_menus)
        self.btn_test_2.setObjectName(u"btn_test_2")
        sizePolicy3.setHeightForWidth(self.btn_test_2.sizePolicy().hasHeightForWidth())
        self.btn_test_2.setSizePolicy(sizePolicy3)
        self.btn_test_2.setMinimumSize(QSize(62, 40))
        self.btn_test_2.setFont(font2)
        self.btn_test_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_test_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.btn_test_2)


        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy2.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy2)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_extra_menus)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_user_icon)

        self.btn_logout = QPushButton(self.frame_extra_menus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy3.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy3)
        self.btn_logout.setMinimumSize(QSize(60, 40))
        self.btn_logout.setMaximumSize(QSize(60, 40))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        self.btn_logout.setFont(font5)
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"	\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icons/16x16/cil-account-logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon4)
        self.btn_logout.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.btn_logout)

        self.btn_login = QPushButton(self.frame_extra_menus)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy3.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy3)
        self.btn_login.setMinimumSize(QSize(60, 40))
        self.btn_login.setMaximumSize(QSize(60, 40))
        self.btn_login.setFont(font5)
        self.btn_login.setLayoutDirection(Qt.LeftToRight)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"	\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icons/16x16/icons8-login-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_login.setIcon(icon5)
        self.btn_login.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.btn_login)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(248, 248, 248);\n"
"color: rgb(6, 6, 6);\n"
"")
        self.page_model = QWidget()
        self.page_model.setObjectName(u"page_model")
        self.verticalLayout_10 = QVBoxLayout(self.page_model)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_model)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_19 = QFrame(self.frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 50))
        self.frame_19.setMaximumSize(QSize(16777215, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_19)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(120, 30))
        self.pushButton_7.setMaximumSize(QSize(200, 16777215))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.lab_selected = QLabel(self.frame_19)
        self.lab_selected.setObjectName(u"lab_selected")
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.lab_selected.setFont(font6)
        self.lab_selected.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_11.addWidget(self.lab_selected)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addWidget(self.frame_19)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(200, 50))
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_name_2 = QLabel(self.frame_13)
        self.label_name_2.setObjectName(u"label_name_2")
        self.label_name_2.setFont(font6)
        self.label_name_2.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_18.addWidget(self.label_name_2)

        self.label_newmodelname = QLineEdit(self.frame_13)
        self.label_newmodelname.setObjectName(u"label_newmodelname")
        self.label_newmodelname.setMinimumSize(QSize(100, 32))

        self.horizontalLayout_18.addWidget(self.label_newmodelname)

        self.label_question_2 = QLabel(self.frame_13)
        self.label_question_2.setObjectName(u"label_question_2")
        self.label_question_2.setFont(font6)
        self.label_question_2.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_18.addWidget(self.label_question_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.pushButton_5 = QPushButton(self.frame_13)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_18.addWidget(self.pushButton_5)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border-color: rgb(22, 28, 33);")
        self.frame_15.setFrameShape(QFrame.WinPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setLineWidth(6)
        self.verticalLayout_15 = QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.image_label_2 = QLabel(self.frame_16)
        self.image_label_2.setObjectName(u"image_label_2")
        self.image_label_2.setScaledContents(True)

        self.verticalLayout_16.addWidget(self.image_label_2)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_title_bar_top_5 = QLabel(self.frame_17)
        self.label_title_bar_top_5.setObjectName(u"label_title_bar_top_5")
        self.label_title_bar_top_5.setMaximumSize(QSize(50, 16777215))
        self.label_title_bar_top_5.setFont(font6)
        self.label_title_bar_top_5.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_17.addWidget(self.label_title_bar_top_5)

        self.pushButton = QPushButton(self.frame_17)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 30))
        icon6 = QIcon()
        icon6.addFile(u":icons/20x20/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.horizontalLayout_17.addWidget(self.pushButton)

        self.good_button_2 = QPushButton(self.frame_17)
        self.good_button_2.setObjectName(u"good_button_2")
        self.good_button_2.setMinimumSize(QSize(20, 30))
        icon7 = QIcon()
        icon7.addFile(u":icons/20x20/cil-thumb-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.good_button_2.setIcon(icon7)

        self.horizontalLayout_17.addWidget(self.good_button_2)

        self.ng_button_2 = QPushButton(self.frame_17)
        self.ng_button_2.setObjectName(u"ng_button_2")
        self.ng_button_2.setMinimumSize(QSize(20, 30))
        icon8 = QIcon()
        icon8.addFile(u":icons/20x20/cil-thumb-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ng_button_2.setIcon(icon8)

        self.horizontalLayout_17.addWidget(self.ng_button_2)

        self.comboBox_4 = QComboBox(self.frame_17)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy2.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy2)
        self.comboBox_4.setMinimumSize(QSize(150, 35))
        self.comboBox_4.setMaximumSize(QSize(207, 50))
        self.comboBox_4.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.horizontalLayout_17.addWidget(self.comboBox_4)

        self.pushButton_8 = QPushButton(self.frame_17)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(20, 30))
        icon9 = QIcon()
        icon9.addFile(u":icons/20x20/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon9)

        self.horizontalLayout_17.addWidget(self.pushButton_8)


        self.verticalLayout_15.addWidget(self.frame_17)


        self.horizontalLayout_19.addWidget(self.frame_15)


        self.verticalLayout_6.addWidget(self.frame_14)


        self.verticalLayout_10.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_model)
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.verticalLayout_11 = QVBoxLayout(self.page_test)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.page_test)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(60, 60))
        self.frame_6.setMaximumSize(QSize(16777215, 72))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_title_bar_top_2 = QLabel(self.frame_6)
        self.label_title_bar_top_2.setObjectName(u"label_title_bar_top_2")
        self.label_title_bar_top_2.setFont(font6)
        self.label_title_bar_top_2.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_20.addWidget(self.label_title_bar_top_2)

        self.input_field = QLineEdit(self.frame_6)
        self.input_field.setObjectName(u"input_field")
        self.input_field.setMinimumSize(QSize(150, 0))
        self.input_field.setMaximumSize(QSize(200, 50))
        self.input_field.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_20.addWidget(self.input_field)

        self.label_title_bar_top_6 = QLabel(self.frame_6)
        self.label_title_bar_top_6.setObjectName(u"label_title_bar_top_6")
        self.label_title_bar_top_6.setFont(font6)
        self.label_title_bar_top_6.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_20.addWidget(self.label_title_bar_top_6)

        self.search_field = QLineEdit(self.frame_6)
        self.search_field.setObjectName(u"search_field")
        self.search_field.setMinimumSize(QSize(150, 0))
        self.search_field.setMaximumSize(QSize(200, 50))
        self.search_field.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_20.addWidget(self.search_field)

        self.label_title_bar_top_3 = QLabel(self.frame_6)
        self.label_title_bar_top_3.setObjectName(u"label_title_bar_top_3")
        self.label_title_bar_top_3.setFont(font6)
        self.label_title_bar_top_3.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_20.addWidget(self.label_title_bar_top_3)

        self.comboBox = QComboBox(self.frame_6)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(200, 30))
        self.comboBox.setMaximumSize(QSize(207, 50))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.horizontalLayout_20.addWidget(self.comboBox)

        self.horizontalSpacer_3 = QSpacerItem(100, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 30))
        self.pushButton_3.setMaximumSize(QSize(100, 16777215))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/16x16/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon10)

        self.horizontalLayout_20.addWidget(self.pushButton_3)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.frame_21 = QFrame(self.page_test)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_8 = QSpacerItem(917, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)


        self.verticalLayout_11.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.page_test)
        self.page_score = QWidget()
        self.page_score.setObjectName(u"page_score")
        self.horizontalLayout_29 = QHBoxLayout(self.page_score)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_24 = QFrame(self.page_score)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_24)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_23 = QFrame(self.frame_24)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_23)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_5 = QLabel(self.frame_23)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_24.addWidget(self.label_5)

        self.frame_22 = QFrame(self.frame_23)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_22)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.employee_name_frame = QFrame(self.frame_22)
        self.employee_name_frame.setObjectName(u"employee_name_frame")
        self.employee_name_frame.setFrameShape(QFrame.StyledPanel)
        self.employee_name_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.employee_name_frame)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.display_employee_name_label = QLabel(self.employee_name_frame)
        self.display_employee_name_label.setObjectName(u"display_employee_name_label")

        self.horizontalLayout_23.addWidget(self.display_employee_name_label)

        self.employee_name_label = QLabel(self.employee_name_frame)
        self.employee_name_label.setObjectName(u"employee_name_label")

        self.horizontalLayout_23.addWidget(self.employee_name_label)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_11)


        self.verticalLayout_22.addWidget(self.employee_name_frame)

        self.employee_id_frame = QFrame(self.frame_22)
        self.employee_id_frame.setObjectName(u"employee_id_frame")
        self.employee_id_frame.setFrameShape(QFrame.StyledPanel)
        self.employee_id_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.employee_id_frame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.display_employee_id_labellabel = QLabel(self.employee_id_frame)
        self.display_employee_id_labellabel.setObjectName(u"display_employee_id_labellabel")

        self.horizontalLayout_26.addWidget(self.display_employee_id_labellabel)

        self.employee_id_label = QLabel(self.employee_id_frame)
        self.employee_id_label.setObjectName(u"employee_id_label")

        self.horizontalLayout_26.addWidget(self.employee_id_label)

        self.horizontalSpacer_13 = QSpacerItem(882, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_13)


        self.verticalLayout_22.addWidget(self.employee_id_frame)

        self.department_frame = QFrame(self.frame_22)
        self.department_frame.setObjectName(u"department_frame")
        self.department_frame.setFrameShape(QFrame.StyledPanel)
        self.department_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.department_frame)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.display_dep_label = QLabel(self.department_frame)
        self.display_dep_label.setObjectName(u"display_dep_label")

        self.horizontalLayout_28.addWidget(self.display_dep_label)

        self.dep_label_2 = QLabel(self.department_frame)
        self.dep_label_2.setObjectName(u"dep_label_2")

        self.horizontalLayout_28.addWidget(self.dep_label_2)

        self.horizontalSpacer_14 = QSpacerItem(889, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_14)


        self.verticalLayout_22.addWidget(self.department_frame)

        self.total_ques_frame = QFrame(self.frame_22)
        self.total_ques_frame.setObjectName(u"total_ques_frame")
        self.total_ques_frame.setFrameShape(QFrame.StyledPanel)
        self.total_ques_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.total_ques_frame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.display_total_ques_label = QLabel(self.total_ques_frame)
        self.display_total_ques_label.setObjectName(u"display_total_ques_label")

        self.horizontalLayout_27.addWidget(self.display_total_ques_label)

        self.total_ques_label = QLabel(self.total_ques_frame)
        self.total_ques_label.setObjectName(u"total_ques_label")

        self.horizontalLayout_27.addWidget(self.total_ques_label)

        self.horizontalSpacer_15 = QSpacerItem(855, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_15)


        self.verticalLayout_22.addWidget(self.total_ques_frame)

        self.score_frame = QFrame(self.frame_22)
        self.score_frame.setObjectName(u"score_frame")
        self.score_frame.setFrameShape(QFrame.StyledPanel)
        self.score_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.score_frame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.display_score_label = QLabel(self.score_frame)
        self.display_score_label.setObjectName(u"display_score_label")

        self.horizontalLayout_25.addWidget(self.display_score_label)

        self.score_label = QLabel(self.score_frame)
        self.score_label.setObjectName(u"score_label")

        self.horizontalLayout_25.addWidget(self.score_label)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_12)


        self.verticalLayout_22.addWidget(self.score_frame)

        self.percentage_frame = QFrame(self.frame_22)
        self.percentage_frame.setObjectName(u"percentage_frame")
        self.percentage_frame.setFrameShape(QFrame.StyledPanel)
        self.percentage_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.percentage_frame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.display_percentage_label = QLabel(self.percentage_frame)
        self.display_percentage_label.setObjectName(u"display_percentage_label")

        self.horizontalLayout_22.addWidget(self.display_percentage_label)

        self.percentage_label = QLabel(self.percentage_frame)
        self.percentage_label.setObjectName(u"percentage_label")

        self.horizontalLayout_22.addWidget(self.percentage_label)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_9)


        self.verticalLayout_22.addWidget(self.percentage_frame)

        self.status_frame = QFrame(self.frame_22)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setFrameShape(QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.status_frame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.display_status_label = QLabel(self.status_frame)
        self.display_status_label.setObjectName(u"display_status_label")

        self.horizontalLayout_24.addWidget(self.display_status_label)

        self.status_label = QLabel(self.status_frame)
        self.status_label.setObjectName(u"status_label")

        self.horizontalLayout_24.addWidget(self.status_label)

        self.horizontalSpacer_16 = QSpacerItem(943, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)


        self.verticalLayout_22.addWidget(self.status_frame)

        self.submit_frame = QFrame(self.frame_22)
        self.submit_frame.setObjectName(u"submit_frame")
        self.submit_frame.setFrameShape(QFrame.StyledPanel)
        self.submit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.submit_frame)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_17 = QSpacerItem(454, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_17)

        self.submit_bts = QPushButton(self.submit_frame)
        self.submit_bts.setObjectName(u"submit_bts")
        self.submit_bts.setMinimumSize(QSize(100, 30))
        self.submit_bts.setMaximumSize(QSize(100, 16777215))
        self.submit_bts.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        self.submit_bts.setIcon(icon4)

        self.horizontalLayout_30.addWidget(self.submit_bts)

        self.horizontalSpacer_18 = QSpacerItem(454, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_18)


        self.verticalLayout_22.addWidget(self.submit_frame)


        self.verticalLayout_24.addWidget(self.frame_22)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_25)


        self.verticalLayout_23.addWidget(self.frame_23)


        self.horizontalLayout_29.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.page_score)
        self.page_adduser = QWidget()
        self.page_adduser.setObjectName(u"page_adduser")
        self.horizontalLayout_42 = QHBoxLayout(self.page_adduser)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.frame_34 = QFrame(self.page_adduser)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_34)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_33 = QFrame(self.frame_34)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_31 = QFrame(self.frame_33)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_31)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_27 = QFrame(self.frame_31)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_27)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.frame_28)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_14.addWidget(self.label_7)

        self.user_name_field_2 = QLineEdit(self.frame_28)
        self.user_name_field_2.setObjectName(u"user_name_field_2")
        self.user_name_field_2.setMinimumSize(QSize(100, 32))

        self.horizontalLayout_14.addWidget(self.user_name_field_2)


        self.verticalLayout_28.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_8 = QLabel(self.frame_29)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_32.addWidget(self.label_8)

        self.employeeID_field = QLineEdit(self.frame_29)
        self.employeeID_field.setObjectName(u"employeeID_field")
        self.employeeID_field.setMinimumSize(QSize(100, 32))

        self.horizontalLayout_32.addWidget(self.employeeID_field)


        self.verticalLayout_28.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_9 = QLabel(self.frame_30)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_31.addWidget(self.label_9)

        self.department_field = QLineEdit(self.frame_30)
        self.department_field.setObjectName(u"department_field")
        self.department_field.setMinimumSize(QSize(100, 32))

        self.horizontalLayout_31.addWidget(self.department_field)


        self.verticalLayout_28.addWidget(self.frame_30)

        self.frame_32 = QFrame(self.frame_27)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalSpacer_10 = QSpacerItem(426, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_10)

        self.pushButton_10 = QPushButton(self.frame_32)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(120, 30))
        self.pushButton_10.setMaximumSize(QSize(200, 16777215))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":icons/20x20/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon11)

        self.horizontalLayout_34.addWidget(self.pushButton_10)

        self.horizontalSpacer_19 = QSpacerItem(425, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_19)


        self.verticalLayout_28.addWidget(self.frame_32)


        self.verticalLayout_31.addWidget(self.frame_27)


        self.horizontalLayout_33.addWidget(self.frame_31)


        self.verticalLayout_32.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.verticalLayout_32.addWidget(self.frame_35)


        self.horizontalLayout_42.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.page_adduser)
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.horizontalLayout_13 = QHBoxLayout(self.page_report)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_2 = QFrame(self.page_report)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(100, 32))

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(85, 26))
        icon12 = QIcon()
        icon12.addFile(u"icons/16x16/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon12)

        self.horizontalLayout_8.addWidget(self.pushButton_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 75))
        self.frame_5.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_12.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.frame_5)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(471, 32))

        self.horizontalLayout_12.addWidget(self.comboBox_2)

        self.bt_report = QPushButton(self.frame_5)
        self.bt_report.setObjectName(u"bt_report")
        icon13 = QIcon()
        icon13.addFile(u"icons/16x16/cil-paper-plane.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_report.setIcon(icon13)

        self.horizontalLayout_12.addWidget(self.bt_report)

        self.bt_report_2 = QPushButton(self.frame_5)
        self.bt_report_2.setObjectName(u"bt_report_2")
        icon14 = QIcon()
        icon14.addFile(u"icons/16x16/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_report_2.setIcon(icon14)

        self.horizontalLayout_12.addWidget(self.bt_report_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)


        self.verticalLayout_17.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.graph_widget = QWidget(self.frame_4)
        self.graph_widget.setObjectName(u"graph_widget")

        self.verticalLayout_18.addWidget(self.graph_widget)


        self.verticalLayout_17.addWidget(self.frame_4)


        self.horizontalLayout_13.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_report)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.verticalLayout_26 = QVBoxLayout(self.page_admin)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_26 = QFrame(self.page_admin)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_26)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_6 = QLabel(self.frame_26)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_27.addWidget(self.label_6)


        self.verticalLayout_26.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.page_admin)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.horizontalLayout = QHBoxLayout(self.page_about)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_18 = QFrame(self.page_about)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setAutoFillBackground(False)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setPixmap(QPixmap(u"icons/fr1.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_10)

        self.bt_take_test = QPushButton(self.frame_18)
        self.bt_take_test.setObjectName(u"bt_take_test")
        self.bt_take_test.setMinimumSize(QSize(0, 45))
        self.bt_take_test.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_take_test.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.bt_take_test)


        self.horizontalLayout.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.page_about)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.horizontalLayout_43 = QHBoxLayout(self.page_login)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.frame_43 = QFrame(self.page_login)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_43)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_41 = QFrame(self.frame_43)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_20 = QFrame(self.frame_41)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_36 = QFrame(self.frame_20)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_3 = QLabel(self.frame_36)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_35.addWidget(self.label_3)

        self.user_name_field = QLineEdit(self.frame_36)
        self.user_name_field.setObjectName(u"user_name_field")
        self.user_name_field.setMinimumSize(QSize(100, 32))

        self.horizontalLayout_35.addWidget(self.user_name_field)


        self.verticalLayout_20.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_20)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_4 = QLabel(self.frame_37)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_36.addWidget(self.label_4)

        self.password_field = QLineEdit(self.frame_37)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setMinimumSize(QSize(100, 32))

        self.horizontalLayout_36.addWidget(self.password_field)


        self.verticalLayout_20.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_20)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_20 = QSpacerItem(174, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_20)

        self.pushButton_9 = QPushButton(self.frame_38)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 30))
        self.pushButton_9.setMaximumSize(QSize(100, 16777215))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        self.pushButton_9.setIcon(icon5)

        self.horizontalLayout_37.addWidget(self.pushButton_9)

        self.horizontalSpacer_21 = QSpacerItem(174, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_21)


        self.verticalLayout_20.addWidget(self.frame_38)


        self.horizontalLayout_40.addWidget(self.frame_20)

        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_42)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_39 = QFrame(self.frame_42)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_22 = QSpacerItem(480, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_22)


        self.verticalLayout_33.addWidget(self.frame_39)


        self.horizontalLayout_40.addWidget(self.frame_42)


        self.verticalLayout_30.addWidget(self.frame_41)

        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalSpacer_23 = QSpacerItem(977, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_23)

        self.verticalSpacer_2 = QSpacerItem(20, 349, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_41.addItem(self.verticalSpacer_2)


        self.verticalLayout_30.addWidget(self.frame_44)


        self.horizontalLayout_43.addWidget(self.frame_43)

        self.stackedWidget.addWidget(self.page_login)
        self.page_exam = QWidget()
        self.page_exam.setObjectName(u"page_exam")
        self.verticalLayout_21 = QVBoxLayout(self.page_exam)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_12 = QFrame(self.page_exam)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.name_label = QLabel(self.frame_12)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_16.addWidget(self.name_label)

        self.display_label_name = QLabel(self.frame_12)
        self.display_label_name.setObjectName(u"display_label_name")
        self.display_label_name.setMinimumSize(QSize(10, 10))
        self.display_label_name.setFont(font6)
        self.display_label_name.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_16.addWidget(self.display_label_name)

        self.dep_label = QLabel(self.frame_12)
        self.dep_label.setObjectName(u"dep_label")

        self.horizontalLayout_16.addWidget(self.dep_label)

        self.display_label_dep = QLabel(self.frame_12)
        self.display_label_dep.setObjectName(u"display_label_dep")
        self.display_label_dep.setMinimumSize(QSize(10, 10))
        self.display_label_dep.setFont(font6)
        self.display_label_dep.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_16.addWidget(self.display_label_dep)

        self.model_label = QLabel(self.frame_12)
        self.model_label.setObjectName(u"model_label")

        self.horizontalLayout_16.addWidget(self.model_label)

        self.display_label_model_name = QLabel(self.frame_12)
        self.display_label_model_name.setObjectName(u"display_label_model_name")
        self.display_label_model_name.setMinimumSize(QSize(10, 10))
        self.display_label_model_name.setFont(font6)
        self.display_label_model_name.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_16.addWidget(self.display_label_model_name)

        self.question_label = QLabel(self.frame_12)
        self.question_label.setObjectName(u"question_label")

        self.horizontalLayout_16.addWidget(self.question_label)

        self.display_label_question = QLabel(self.frame_12)
        self.display_label_question.setObjectName(u"display_label_question")
        self.display_label_question.setMinimumSize(QSize(10, 10))
        self.display_label_question.setFont(font6)
        self.display_label_question.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_16.addWidget(self.display_label_question)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)


        self.verticalLayout_21.addWidget(self.frame_12)

        self.frame_7 = QFrame(self.page_exam)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border-color: rgb(22, 28, 33);")
        self.frame_8.setFrameShape(QFrame.WinPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(6)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border: 2px solid rgb(27, 29, 35);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.image_label = QLabel(self.frame_10)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.image_label)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(60, 60))
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_title_bar_top_4 = QLabel(self.frame_11)
        self.label_title_bar_top_4.setObjectName(u"label_title_bar_top_4")
        self.label_title_bar_top_4.setMaximumSize(QSize(75, 16777215))
        self.label_title_bar_top_4.setFont(font6)
        self.label_title_bar_top_4.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;\n"
"border: 2px solid rgb(27, 29, 35);")

        self.horizontalLayout_9.addWidget(self.label_title_bar_top_4)

        self.good_button = QPushButton(self.frame_11)
        self.good_button.setObjectName(u"good_button")
        self.good_button.setMinimumSize(QSize(20, 10))
        icon15 = QIcon()
        icon15.addFile(u"icons/16x16/cil-thumb-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.good_button.setIcon(icon15)

        self.horizontalLayout_9.addWidget(self.good_button)

        self.ng_button = QPushButton(self.frame_11)
        self.ng_button.setObjectName(u"ng_button")
        self.ng_button.setMinimumSize(QSize(20, 10))
        icon16 = QIcon()
        icon16.addFile(u"icons/16x16/cil-thumb-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ng_button.setIcon(icon16)

        self.horizontalLayout_9.addWidget(self.ng_button)

        self.comboBox_3 = QComboBox(self.frame_11)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy2.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy2)
        self.comboBox_3.setMinimumSize(QSize(100, 20))
        self.comboBox_3.setMaximumSize(QSize(207, 40))
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.horizontalLayout_9.addWidget(self.comboBox_3)


        self.verticalLayout_12.addWidget(self.frame_11)


        self.horizontalLayout_15.addWidget(self.frame_8)

        self.scrollArea = QScrollArea(self.frame_7)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(200, 453))
        self.scrollArea.setMaximumSize(QSize(200, 16777215))
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(56, 56, 85);\n"
" }\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"QToolTip\n"
" {\n"
"      background: white;\n"
"	color: rgb(255, 255, 255);\n"
"    }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 200, 504))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setToolTipDuration(0)
        self.frame_9.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"\n"
"QToolTip\n"
" {\n"
"      background: white;\n"
"	color: rgb(255, 255, 255);\n"
"    }\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(44, 49, 60);\n"
"	color: rgb(6, 6, 6);\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)


        self.verticalLayout_8.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon17 = QIcon()
        icon17.addFile(u"icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon17)

        self.verticalLayout_8.addWidget(self.pushButton_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_15.addWidget(self.scrollArea)


        self.verticalLayout_21.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_exam)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(255, 125, 0);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font5)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);\n"
"color: rgb(255, 255, 255);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.verticalLayout_7.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_113.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"<p><span style=\" font-size:22pt;\">VCBT</span><span style=\" font-size:22pt; vertical-align:sub;\">Visteon Computer Based Assesment</span></p>", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"Take \n"
"Test", None))
#if QT_CONFIG(tooltip)
        self.btn_test_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:6pt;\">Create Account</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_test_3.setText(QCoreApplication.translate("MainWindow", u"Create \n"
" Account", None))
        self.btn_test_5.setText(QCoreApplication.translate("MainWindow", u"Add \n"
" Model", None))
        self.btn_test_4.setText(QCoreApplication.translate("MainWindow", u"Edit\n"
"Model", None))
        self.btn_test_2.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.label_user_icon.setText("")
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"logout", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.lab_selected.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Selected Folder:</p></body></html>", None))
        self.label_name_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_question_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Create Model", None))
        self.image_label_2.setText("")
        self.label_title_bar_top_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PREVIOUS", None))
        self.good_button_2.setText(QCoreApplication.translate("MainWindow", u"good", None))
        self.ng_button_2.setText(QCoreApplication.translate("MainWindow", u"ng", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.label_title_bar_top_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Employee ID:</p></body></html>", None))
        self.label_title_bar_top_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Search:</p></body></html>", None))
        self.label_title_bar_top_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select Model:</p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Take Test", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Test Score </span></p></body></html>", None))
        self.display_employee_name_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Employee Name:</span></p></body></html>", None))
        self.employee_name_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.display_employee_id_labellabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Employee ID:</span></p></body></html>", None))
        self.employee_id_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.display_dep_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Department:</span></p></body></html>", None))
        self.dep_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.display_total_ques_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Total Questions:</span></p></body></html>", None))
        self.total_ques_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.display_score_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Score:</span></p></body></html>", None))
        self.score_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.display_percentage_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:14pt; font-weight:600; color:#000000;\">Percentage:</span></p></body></html>", None))
        self.percentage_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.display_status_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Status:</span></p></body></html>", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.submit_bts.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"User Name  :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Employee ID:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Department :", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"CREATE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Employee ID ", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Report", None))
        self.bt_report.setText(QCoreApplication.translate("MainWindow", u"Show Report", None))
        self.bt_report_2.setText(QCoreApplication.translate("MainWindow", u"Show Chart", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">Welcome</span></p></body></html>", None))
        self.label_10.setText("")
        self.bt_take_test.setText(QCoreApplication.translate("MainWindow", u"WELCOME - Click here to start", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User Name:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password  :", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name:</span></p></body></html>", None))
        self.display_label_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.dep_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Department:</span></p></body></html>", None))
        self.display_label_dep.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.model_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Model Name:</span></p></body></html>", None))
        self.display_label_model_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.question_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Total Question:</span></p></body></html>", None))
        self.display_label_question.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.image_label.setText("")
        self.label_title_bar_top_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.good_button.setText(QCoreApplication.translate("MainWindow", u"good", None))
        self.ng_button.setText(QCoreApplication.translate("MainWindow", u"ng", None))
#if QT_CONFIG(tooltip)
        self.frame_9.setToolTip(QCoreApplication.translate("MainWindow", u"push", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi


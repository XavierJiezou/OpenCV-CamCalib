# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(461, 366)
        self.camera_address = QAction(MainWindow)
        self.camera_address.setObjectName(u"camera_address")
        self.screenshot_setting = QAction(MainWindow)
        self.screenshot_setting.setObjectName(u"screenshot_setting")
        self.about_us = QAction(MainWindow)
        self.about_us.setObjectName(u"about_us")
        self.data_collection = QAction(MainWindow)
        self.data_collection.setObjectName(u"data_collection")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.url_input = QLineEdit(self.centralwidget)
        self.url_input.setObjectName(u"url_input")
        self.url_input.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.url_input)

        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.image_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play_button = QPushButton(self.centralwidget)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.play_button)

        self.shot_button = QPushButton(self.centralwidget)
        self.shot_button.setObjectName(u"shot_button")
        self.shot_button.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.shot_button)

        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 461, 22))
        self.open = QMenu(self.menubar)
        self.open.setObjectName(u"open")
        self.settings = QMenu(self.menubar)
        self.settings.setObjectName(u"settings")
        self.help = QMenu(self.menubar)
        self.help.setObjectName(u"help")
        self.calibration = QMenu(self.menubar)
        self.calibration.setObjectName(u"calibration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.open.menuAction())
        self.menubar.addAction(self.calibration.menuAction())
        self.menubar.addAction(self.settings.menuAction())
        self.menubar.addAction(self.help.menuAction())
        self.open.addAction(self.camera_address)
        self.settings.addAction(self.screenshot_setting)
        self.help.addAction(self.data_collection)
        self.help.addAction(self.about_us)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6d41\u5a92\u4f53\u89c6\u9891\u64ad\u653e\u5668", None))
        self.camera_address.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5730\u5740(&L)", None))
#if QT_CONFIG(tooltip)
        self.camera_address.setToolTip(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5730\u5740", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.camera_address.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.screenshot_setting.setText(QCoreApplication.translate("MainWindow", u"\u622a\u56fe\u8bbe\u7f6e(&F)", None))
#if QT_CONFIG(tooltip)
        self.screenshot_setting.setToolTip(QCoreApplication.translate("MainWindow", u"\u622a\u56fe\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.about_us.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6211\u4eec(&A)", None))
#if QT_CONFIG(tooltip)
        self.about_us.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6211\u4eec", None))
#endif // QT_CONFIG(tooltip)
        self.data_collection.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u91c7\u96c6(&D)", None))
#if QT_CONFIG(tooltip)
        self.data_collection.setToolTip(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u91c7\u96c6", None))
#endif // QT_CONFIG(tooltip)
        self.url_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5730\u5740", None))
        self.image_label.setText("")
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
        self.shot_button.setText(QCoreApplication.translate("MainWindow", u"\u622a\u56fe", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.open.setTitle(QCoreApplication.translate("MainWindow", u"\u6253\u5f00(&O)", None))
        self.settings.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e(&S)", None))
        self.help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
        self.calibration.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a(&C)", None))
    # retranslateUi


################################################################################
## Form generated from reading UI file 'chessboard_calibration.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QTabWidget,
    QTextBrowser,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog:
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(460, 393)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.groupBox)
        self.toolButton.setObjectName("toolButton")

        self.horizontalLayout.addWidget(self.toolButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(9)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox_2 = QSpinBox(self.groupBox_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setValue(6)

        self.horizontalLayout_3.addWidget(self.spinBox_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.addWidget(self.groupBox_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(False)

        self.verticalLayout.addWidget(self.checkBox)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_7 = QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")

        self.horizontalLayout_7.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textBrowser_2 = QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.horizontalLayout_8.addWidget(self.textBrowser_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textBrowser_3 = QTextBrowser(self.tab_3)
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.horizontalLayout_9.addWidget(self.textBrowser_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.textBrowser_4 = QTextBrowser(self.tab_4)
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.horizontalLayout_10.addWidget(self.textBrowser_4)

        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "\u68cb\u76d8\u6807\u5b9a", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("Dialog", "\u6807\u5b9a\u8bbe\u7f6e", None)
        )
        self.label.setText(
            QCoreApplication.translate("Dialog", "\u9009\u62e9\u6570\u636e", None)
        )
        self.toolButton.setText(QCoreApplication.translate("Dialog", "...", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Dialog", "\u6807\u5b9a\u677f\u5c3a\u5bf8", None)
        )
        self.label_2.setText(QCoreApplication.translate("Dialog", "\u884c", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "\u5217", None))
        self.label_4.setText(
            QCoreApplication.translate("Dialog", "\u68cb\u76d8\u683c\u5927\u5c0f", None)
        )
        # if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lineEdit_2.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", "1", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Dialog", "\u5355\u4f4d\uff1amm", None)
        )
        self.checkBox.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u663e\u793a\u6807\u5b9a\u8fc7\u7a0b\uff08\u7ed8\u5236\u68c0\u6d4b\u7684\u89d2\u70b9\uff09",
                None,
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate("Dialog", "\u5f00\u59cb", None)
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate("Dialog", "\u6807\u5b9a\u7ed3\u679c", None)
        )
        self.textBrowser.setHtml(
            QCoreApplication.translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("Dialog", "\u76f8\u673a\u5185\u53c2", None),
        )
        self.textBrowser_2.setHtml(
            QCoreApplication.translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("Dialog", "\u7578\u53d8\u7cfb\u6570", None),
        )
        self.textBrowser_3.setHtml(
            QCoreApplication.translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("Dialog", "\u76f8\u673a\u5916\u53c2", None),
        )
        self.textBrowser_4.setHtml(
            QCoreApplication.translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4),
            QCoreApplication.translate("Dialog", "\u8bc4\u4f30\u6307\u6807", None),
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("Dialog", "\u4fdd\u5b58", None)
        )

    # retranslateUi

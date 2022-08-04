################################################################################
## Form generated from reading UI file 'distortion_correction.ui'
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
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog:
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton = QToolButton(Dialog)
        self.toolButton.setObjectName("toolButton")

        self.horizontalLayout.addWidget(self.toolButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.toolButton_2 = QToolButton(Dialog)
        self.toolButton_2.setObjectName("toolButton_2")

        self.horizontalLayout_2.addWidget(self.toolButton_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.100000000000000)
        self.doubleSpinBox.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "\u7578\u53d8\u7ea0\u6b63", None)
        )
        self.label.setText(
            QCoreApplication.translate("Dialog", "\u9009\u62e9\u6570\u636e", None)
        )
        self.toolButton.setText(QCoreApplication.translate("Dialog", "...", None))
        self.label_2.setText(
            QCoreApplication.translate("Dialog", "\u76f8\u673a\u53c2\u6570", None)
        )
        self.toolButton_2.setText(QCoreApplication.translate("Dialog", "...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "Alpha", None))
        self.doubleSpinBox.setSuffix("")
        self.checkBox.setText(
            QCoreApplication.translate("Dialog", "\u88c1\u526a\u8fb9\u7f18", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("Dialog", "\u5f00\u59cb", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("Dialog", "\u4fdd\u5b58", None)
        )

    # retranslateUi

################################################################################
## Form generated from reading UI file 'screenshot_setting.ui'
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
    QAbstractButton,
    QApplication,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QRadioButton,
    QSizePolicy,
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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.toolButton = QToolButton(Dialog)
        self.toolButton.setObjectName("toolButton")

        self.horizontalLayout_2.addWidget(self.toolButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(Dialog)
        self.radioButton_3.setObjectName("radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "\u622a\u56fe\u8bbe\u7f6e", None)
        )
        self.label.setText(
            QCoreApplication.translate("Dialog", "\u4fdd\u5b58\u4f4d\u7f6e", None)
        )
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "Dialog",
                "\u9ed8\u8ba4\u4fdd\u5b58\u5230\u4e0e\u7a0b\u5e8f\u540c\u7ea7\u7684\u76ee\u5f55\u4e0b",
                None,
            )
        )
        self.toolButton.setText(QCoreApplication.translate("Dialog", "...", None))
        self.label_2.setText(
            QCoreApplication.translate("Dialog", "\u4fdd\u5b58\u683c\u5f0f", None)
        )
        self.radioButton.setText(QCoreApplication.translate("Dialog", "BMP", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", "PNG", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", "JPG", None))

    # retranslateUi

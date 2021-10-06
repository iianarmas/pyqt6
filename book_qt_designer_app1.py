# ========== MAIN.PY ========== #

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

from test import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor('black'))
        palette.setColor(QPalette.ColorRole.WindowText, QColor('white'))

        self.setPalette(palette)

        self.setupUi(self)

        self.generate_button.released.connect(self.generate_random)

    def generate_random(self):
        self.label.setText(f'Generated Number: {randint(0, 100)}')


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

# ========== TEST.PY ========== #

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setDefault(False)
        self.generate_button.setFlat(False)
        self.generate_button.setObjectName("generate_button")
        self.verticalLayout.addWidget(self.generate_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Generate a Random Number"))
        self.generate_button.setText(_translate("MainWindow", "GENERATE"))

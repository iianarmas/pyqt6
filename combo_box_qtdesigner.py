from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 529)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.combo_1 = QtWidgets.QComboBox(self.centralwidget)
        self.combo_1.setGeometry(QtCore.QRect(70, 100, 291, 131))

        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)

        self.combo_1.setFont(font)
        self.combo_1.setObjectName("combo_1")
        self.combo_1.addItem("")
        self.combo_1.addItem("")

        self.combo_2 = QtWidgets.QComboBox(self.centralwidget)
        self.combo_2.setGeometry(QtCore.QRect(490, 100, 291, 131))

        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)

        self.combo_2.setFont(font)
        self.combo_2.setObjectName("combo_2")
        self.combo_2.addItem("")
        self.combo_2.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 350, 201, 101))

        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 260, 211, 51))

        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 27))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.released.connect(self.pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_1.setItemText(0, _translate("MainWindow", "0"))
        self.combo_1.setItemText(1, _translate("MainWindow", "1"))
        self.combo_2.setItemText(0, _translate("MainWindow", "0"))
        self.combo_2.setItemText(1, _translate("MainWindow", "1"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "X XOR Y ="))

    def pressed(self):
        cb_1 = int(self.combo_1.currentText())
        cb_2 = int(self.combo_2.currentText())

        answer = 0 if cb_1 == 0 == cb_2 else 1
        self.label.setText(f'X XOR Y = {answer}')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

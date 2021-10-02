from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 633)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(310, 390, 161, 51))
        self.button.setCheckable(False)
        self.button.setFlat(False)
        self.button.setObjectName("button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 27))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button.released.connect(self.show_message)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "SHOW MESSAGE"))

    def show_message(self):
        message = QMessageBox()
        message.setWindowTitle('PyQt6 Tutorial')
        message.setText('This is the main text!\n\nJust adding more words to see how how this window will respond.\n'
                        'So the height and width of the window responds to the number of text characters that it has.\n'
                        '\nI wonder what the maximum height of this window is.')
        message.setIcon(message.Icon.Information)
        message.setStandardButtons(message.StandardButton.Cancel | message.StandardButton.Ok)
        message.setDefaultButton(message.StandardButton.Ok)
        message.setInformativeText('This is informative!')

        message.setDetailedText('Here are the details of the message.')

        message.buttonClicked.connect(self.pop_up)

        message.exec()

    def pop_up(self, i):
        if i.text() == 'Cancel':
            print('Cancelled Message')
        else:
            print('Feeling good!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

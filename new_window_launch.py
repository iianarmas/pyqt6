# =========== MAIN.PY =========== #

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QPushButton
from dialog import Ui_Dialog
from dash import Ui_MainWindow
from sheet import style

from qt_material import apply_stylesheet

"""with open('my_style.qss', 'r') as s:
    style = s.read()"""


class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(style)

        self.setupUi(self)

        self.button_okay.released.connect(self.on_button_okay)

        self.main_window = MainWindow()

    def on_button_okay(self):
        self.hide()
        self.main_window.show()

        message = QMessageBox()
        """message.critical(self, 'Success',
                                    'Congratulations!\nYou are logged in!\nPlease proceed on creating your account')"""

        message.setWindowTitle('PyQt6 Tutorial')
        message.setText('This is the main text!\n\nJust adding more words to see how how this window will respond.\n'
                        'So the height and width of the window responds to the number of text characters that it has.\n'
                        '\nI wonder what the maximum height of this window is.')
        message.setIcon(message.Icon.Information)
        message.setStandardButtons(message.StandardButton.Ok)
        message.setDefaultButton(message.StandardButton.Ok)
        message.setInformativeText('This is informative!')

        message.setDetailedText('Here are the details of the message.')

        message.setStyleSheet(style)
        message.exec()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = DialogWindow()
    # apply_stylesheet(app, theme='dark_blue.xml')

    window.show()

    sys.exit(app.exec())

    
# =========== DIALOG.PY =========== #

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 175)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 0, 331, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.button_okay = QtWidgets.QPushButton(Dialog)
        self.button_okay.setGeometry(QtCore.QRect(340, 120, 90, 37))
        self.button_okay.setObjectName("button_okay")

        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setGeometry(QtCore.QRect(440, 120, 90, 37))
        self.button_cancel.setObjectName("button_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Press okay to continue"))
        self.button_okay.setText(_translate("Dialog", "OKAY"))
        self.button_cancel.setText(_translate("Dialog", "CANCEL"))

# =========== DASH.PY =========== #

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(290, 150, 251, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome!"))
        
# =========== SHEET.PY =========== #
    
style = '''
QPushButton {
  color: white;
  background-color: #5e19ff;
  border-radius: 4px;
  padding: 8px 16px ;
  height: 18px;
  text-transform: uppercase;
  font-weight: bold;
} 

QPushButton:checked,
QPushButton:pressed {
  color: #ffffff;
  background-color: #e4c047;
}

QPushButton.success:checked,
QPushButton.success:pressed {
  color: #ffffff;

}

QPushButton:hover {
  background-color: #e4c047;
}

QIcon {
    color: #ffffff;
}
'''

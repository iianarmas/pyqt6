from PyQt6 import QtCore, QtGui, QtWidgets
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # setup the central window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 170, 231, 161))
        self.font = QtGui.QFont()
        self.font.setFamily("Lato Heavy")
        self.font.setPointSize(36)
        self.font.setBold(True)
        self.font.setItalic(False)
        self.font.setWeight(75)
        self.label.setFont(self.font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(330, 340, 171, 61))
        self.button.setStyleSheet('background-color: white;'
                                  'border-radius: 15')
        self.button.setObjectName('button_1')

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 27))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName('actionCut')

        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")


        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)

        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNew.triggered.connect(lambda: self.on_button_release('New was clicked'))
        self.actionSave.triggered.connect(lambda: self.on_button_release('Save was clicked'))
        self.actionExit.triggered.connect(lambda: self.on_button_release('Exit was clicked'))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Iian's PyQt6 App"))

        self.label.setText(_translate("MainWindow", "Iian"))

        self.button.setText(_translate('MainWindow', 'Click Here'))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create New File"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Quit Application"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy File"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionCut.setText(_translate('MainWindow', 'Cut'))
        self.actionCut.setStatusTip(_translate('MainWindow', 'Cut File'))
        self.actionCut.setShortcut(_translate('MainWindow', 'Ctrl+X'))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste File"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))

    def on_button_release(self, text):
        self.label.setText(text)
        self.label.adjustSize()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

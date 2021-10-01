from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 633)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 821, 510))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../ffsc_sched_v2/images/ffsc_cover.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.photo.setObjectName("photo")

        self.image_1 = QtWidgets.QPushButton(self.centralwidget)
        self.image_1.setGeometry(QtCore.QRect(110, 550, 161, 51))
        self.image_1.setObjectName("image_1")

        self.image_2 = QtWidgets.QPushButton(self.centralwidget)
        self.image_2.setGeometry(QtCore.QRect(520, 550, 161, 51))
        self.image_2.setObjectName("image_2")



        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 27))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.image_1.clicked.connect(self.image_1_click)
        self.image_2.clicked.connect(self.image_2_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.image_1.setText(_translate("MainWindow", "Image 1"))
        self.image_2.setText(_translate("MainWindow", "Image 2"))

    def image_1_click(self):
        self.photo.setPixmap(QtGui.QPixmap("../ffsc_sched_v2/images/ffsc_cover.jpg"))

    def image_2_click(self):
        self.photo.setPixmap(QtGui.QPixmap("../ffsc_sched_v2/images/events_cover.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

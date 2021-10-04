from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QCheckBox, QWidget, QMainWindow, QLabel, QLineEdit, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')
        

        widget = QCheckBox('This is a checkbox')
        widget.setCheckState(Qt.CheckState.Unchecked)

        widget.stateChanged.connect(self.showstate)


        self.setCentralWidget(widget)

    def showstate(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)
        if s == 2:
            print('this is true')
        else:
            print('this is false')



if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

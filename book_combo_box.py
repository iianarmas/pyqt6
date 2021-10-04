from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        widget = QComboBox()

        widget.addItems(['One', 'Two', 'Three'])

        widget.setEditable(True)
        #widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAtCurrent)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

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

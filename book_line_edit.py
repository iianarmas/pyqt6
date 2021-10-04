from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Enter your name')

        # widget.setReadOnly(True) # to make it read only

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print('Return pressed!')
        self.centralWidget().setText('BOOM!')

    def selection_changed(self):
        print('Selection changed')
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print('Text changed...')
        print(s)

    def text_edited(self, s):
        print('Text edited...')
        print(s)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

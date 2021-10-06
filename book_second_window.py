from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QWidget
from random import randint


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        # to make a window persistent, create its instance in the init and call it
        # using a function
        self.new = SecondWindow()  # -> window is only created once

        # for non persistent, initialize it in the function itself
        # self.new = None

        button = QPushButton('OPEN WINDOW')
        button.clicked.connect(self.button_clicked)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.new.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    # recreate the same window and destroy previous
    """def button_clicked(self):
        self.new = SecondWindow()
        self.new.show()"""

    # show window one time and not recreate it
    """def button_clicked(self):
        if self.new is None:
            self.new = SecondWindow()
            self.new.show()

        # this can be discarded to show window only once
        else:
            self.new.close()
            self.new = None"""

    # check if window is already visible
    def button_clicked(self):
        if self.new.isVisible():
            self.new.hide()
        else:
            self.new.show()


class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('New Window')

        self.label = QLabel(f'This is the second window. {randint(0, 100)}')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.label)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

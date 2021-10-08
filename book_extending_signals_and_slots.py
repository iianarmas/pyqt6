from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    message = pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Extended Signals')

        self.container = QWidget()
        layout = QHBoxLayout()

        self.button = QPushButton()
        self.button.setText('CLICK HERE')

        self.button_2 = QPushButton()
        self.button_2.setText('CLICK HERE')

        self.button.clicked.connect(lambda checked: self.fire_away(checked, self.button))
        self.button_2.clicked.connect(lambda checked: self.fire_away(checked, self.button_2))

        layout.addWidget(self.button)
        layout.addWidget(self.button_2)

        self.counter_1 = 1
        self.counter_2 = 1

        self.container.setLayout(layout)
        self.container.mousePressEvent = lambda event: self.fire_away(event, self.container)

        self.setCentralWidget(self.container)

    def fire_away(self, check, widget):
        match widget:
            case self.button:
                print(f'button 1 was clicked {self.counter_1} time(s)')
                self.counter_1 += 1
            case self.button_2:
                print(f'button 2 was clicked {self.counter_2} time(s)')
                self.counter_2 += 1
            case self.container:
                print('Layout was clicked')


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

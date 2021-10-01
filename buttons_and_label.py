from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

button_text = 'Click Here'

# create class that extends QWidget
class Window(QWidget):
    def __init__(self):
        super().__init__()

        # window title
        self.setWindowTitle('PyQt6 Window')

        # add icon
        self.setWindowIcon(QIcon('newlogo.png'))

        # fix window width and height
        """ resizing window will not be possible after setting this
            even maximizing window won't be possible"""
        # self.setFixedWidth(780)
        # self.setFixedHeight(460)

        # set geometry of window (x_position, y_position, width, height)
        # Geometry sets the widgets position
        self.setGeometry(400, 200, 780, 460)

        # set background color (2 ways)
        # first
        # self.setStyleSheet('background-color:#f4f3f5')

        # second - create a qt stylesheet and setting it
        stylesheet = (
            'background-color: #f4f3f5'
        )

        self.setStyleSheet(stylesheet)

        self.my_widgets()


        self.counter = 1


    def my_widgets(self):
        label = QLabel('My Label', self)
        label.move(int(290 + 171/5.2), 80)
        label.setStyleSheet('color: #191a18')
        label.setFont(QFont('Arial', 20))

        button = QPushButton(button_text, self)
        """button.move(290, 300)
        button.setFixedWidth(171)
        button.setFixedHeight(61)"""
        button.setGeometry(290, 300, 171, 61)
        stylesheet = (
            'background-color: white;'
            'border-radius: 15'
        )

        button.setStyleSheet(stylesheet)
        button.setIcon(QIcon('newlogo.png'))
        button.released.connect(self.button_click)



    def button_click(self):
        print(f'Button click {self.counter}')
        self.counter += 1

# create QApplication object
app = QApplication([])

# create class Window object
window = Window()

# show window
window.show()

# exit
sys.exit(app.exec())

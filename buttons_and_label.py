from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QIcon, QFont, QColor

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
            'background-color: #fcfcfc;'
            'border-radius: 15'
        )

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(24)
        shadow.setXOffset(0)
        shadow.setYOffset(8)
        shadow.setColor(QColor('#e4e3e5'))  # also accepts rgba values with syntax QColor(63, 63, 63, 180)

        button.setStyleSheet(stylesheet)
        button.setIcon(QIcon('newlogo.png'))
        button.setGraphicsEffect(shadow)



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



# ==================================================================
# CLEANER VERSION WITH LABEL ADJUSTMENT METHOD

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QIcon, QFont, QColor

import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(400, 200, 780, 460)
        self.setWindowTitle('Iian')
        self.setStyleSheet('background-color: #f4f3f5')

        self.label = QLabel(self)
        self.btn_1 = QPushButton(self)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(24)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(8)
        self.shadow.setColor(QColor('#e4e3e5'))

        self.btn_1_counter = 1
        self.initUI()

    def initUI(self):
        self.label.setText('Hello World')
        self.label.move(int(290 + 171/5.2), 80)
        self.label.setStyleSheet('color: #191a18')
        self.label.setFont(QFont('Arial', 20))

        btn_stylesheet = (
            'background-color: #fcfcfc;'
            'border-radius: 15'
        )

        self.btn_1.setText('Click Here')
        self.btn_1.setGeometry(290, 300, 171, 61)
        self.btn_1.setStyleSheet(btn_stylesheet)
        self.btn_1.setIcon(QIcon('newlogo.png'))
        self.btn_1.setGraphicsEffect(self.shadow)
        self.btn_1.released.connect(self.on_btn_1_release)

    def on_btn_1_release(self):
        self.btn_1.setText('Click Here Again')
        num = 'time' if self.btn_1_counter == 1 else 'times'
        self.label.setText(f'Clicked {self.btn_1_counter} {num}')
        self.update()
        self.btn_1_counter += 1

    def update(self):
        # this will adjust the size of the label container to fit the new character numbers
        self.label.adjustSize()


def start_app():

    app = QApplication(sys.argv)

    win = Window()

    win.show()

    sys.exit(app.exec())


start_app()


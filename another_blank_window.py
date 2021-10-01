from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


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
        #self.setFixedWidth(780)
        #self.setFixedHeight(460)

        # set geometry of window (x_position, y_position, width, height)
        self.setGeometry(400, 200, 780, 460)

        # set background color (2 ways)
        # first
        # self.setStyleSheet('background-color:#f4f3f5')

        # second - create a qt stylesheet and setting it
        stylesheet = (
            'background-color: #f4f3f5'
        )

        self.setStyleSheet(stylesheet)

# create QApplication object
app = QApplication([])

# create class Window object
window = Window()

# show window
window.show()

# exit
sys.exit(app.exec())

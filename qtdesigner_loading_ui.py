from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys

""" first is to save a QTDesign as a ui file,
then load it on to python file using uic.loadUi('filename.py', self)"""

class Ui(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('back.ui', self)


# create QApplication object
app = QApplication([])

# create class Window object
window = Ui()

# show window
window.show()

# exit
sys.exit(app.exec())


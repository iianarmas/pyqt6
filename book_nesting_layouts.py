# ============ MAIN.PY ============

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout)
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        # setting layout margins and spacing
        layout1.setSpacing(20)
        layout1.setContentsMargins(0, 0, 0, 0)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout3.addWidget(Color('yellow'))
        layout3.addWidget(Color('red'))
       
        layout1.addLayout(layout2)
        layout1.addWidget(Color('green'))
        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()


    
# ============ LAYOUT_COLORWIDGET.PY ============

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super().__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

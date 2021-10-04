# ========== MAIN.PY ==========

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedLayout,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
    )
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacked_layout = QStackedLayout()

        button1 = QPushButton()
        button2 = QPushButton()
        button3 = QPushButton()
        button4 = QPushButton()

        button1.setText('RED')
        button2.setText('YELLOW')
        button3.setText('BLUE')
        button4.setText('GREEN')

        button1.pressed.connect(self.activate_tab_1)
        button2.pressed.connect(self.activate_tab_2)
        button3.pressed.connect(self.activate_tab_3)
        button4.pressed.connect(self.activate_tab_4)

        self.stacked_layout.addWidget(Color('red'))
        self.stacked_layout.addWidget(Color('yellow'))
        self.stacked_layout.addWidget(Color('blue'))
        self.stacked_layout.addWidget(Color('green'))

        self.stacked_layout.setCurrentIndex(0)

        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        button_layout.addWidget(button4)

        main_layout.addLayout(button_layout)
        main_layout.addLayout(self.stacked_layout)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        self.setWindowTitle('Iian App')

    def activate_tab_1(self):
        self.stacked_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacked_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacked_layout.setCurrentIndex(2)

    def activate_tab_4(self):
        self.stacked_layout.setCurrentIndex(3)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()
    
# ========== LAYOUT_COLORWIDGET.PY ==========

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super().__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedLayout)
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QStackedLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('yellow'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('pink'))

        layout.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.setWindowTitle('Iian App')


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

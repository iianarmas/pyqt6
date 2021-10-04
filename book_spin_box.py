from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        widget = QSpinBox()
        # or: widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)

        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

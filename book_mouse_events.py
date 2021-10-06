from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QWidget
from random import randint


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        self.label = QLabel('Click this window')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setMouseTracking(True)

        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText('mousePressEvent LEFT')

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('mousePressEvent MIDDLE')

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('mousePressEvent RIGHT')

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText('mouseReleaseEvent LEFT')

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('mouseReleaseEvent MIDDLE')

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('mouseReleaseEvent RIGHT')

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText('mouseDoubleClickEvent LEFT')

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('mouseDoubleClickEvent MIDDLE')

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('mouseDoubleClickEvent RIGHT')


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

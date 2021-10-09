from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)

        self.label.setPixmap(self.canvas)

        self.setCentralWidget(self.label)

        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.canvas)
        painter.drawLine(10, 10, 300, 200)
        painter.end()
        self.label.setPixmap(self.canvas)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QPixmap, QPen, QColor
from numpy.random import randint, choice


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
        colors = ["#FFD141", "#376F9F", "#0D1F2D", "#E9EBEF",
                  "#EB5160"]

        painter = QPainter(self.canvas)
        pen = QPen()            # to change the color and thickness
        pen.setWidth(8)
        pen.setColor(QColor('red'))

        painter.setPen(pen)
        # painter.drawLine(10, 10, 300, 200)
        # painter.drawPoint(200, 150)

        for i in range(10000):
            pen.setColor(QColor(choice(colors)))
            pen.setWidth(randint(3, 5))
            painter.setPen(pen)
            painter.drawPoint(200 + randint(-100, 100), 150 + randint(-100, 100))

        painter.end()
        self.label.setPixmap(self.canvas)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

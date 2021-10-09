from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QPixmap, QPen, QColor, QBrush, QImage
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
        pen.setWidth(3)
        pen.setColor(QColor('violet'))

        image = QImage('resources/icons/icons8-tick-16.png')

        brush = QBrush()
        brush.setColor(QColor('#FFD141'))

        brush.setTextureImage(image)
        # brush.setStyle(Qt.BrushStyle.SolidPattern)        # set a solid fill

        painter.setBrush(brush)

        painter.setPen(pen)

        # drawing a Line
        # painter.drawLine(100, 100, 300, 200)
        # or -----------------
        # painter.drawLine(QPoint(100, 100), QPoint(300, 200))

        # drawing a rectangle
        # drawRect(x, y, w, h)
        painter.drawRect(200, 50, 100, 150)

        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRoundedRect(70, 150, 100, 100, 16, 16)  # drawRoundRect(x, y, w, h, rx, ry)

        painter.drawEllipse(10, 10, 100, 100)   # drawEllipse(x, y, w, h)

        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        painter.drawEllipse(QPoint(100, 100), 80, 80)   # this takes the center of the circle as the first param

        painter.end()
        self.label.setPixmap(self.canvas)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class _Bar(QtWidgets.QWidget):
    def __init__(self, steps):
        super().__init__()

        # to fill all possible available space
        # Tag::start
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding
        )

        if isinstance(steps, list):
            # list of colors
            self.n_steps = len(steps)
            self.steps = steps

        elif isinstance(steps, int):
            # int number of bars, default to red
            self.n_steps = steps
            self.steps = ['red'] * steps
        else:
            raise TypeError('steps must be a list or int')

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor('black')
        self._padding = 4  # n-pixel gap around edge

    def sizeHint(self):  # this will set the minimum possible size of the widget
        return QtCore.QSize(40, 120)
        # ::end

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Get current state
        dial = self.parent()._dial  # this will access the parent's (PowerBar()) ._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        # determine the number of steps to draw
        # ::start
        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * self.n_steps)
        # ::end

        # tag::dimensions[]
        # padding = 5

        # define canvas
        d_width = painter.device().width() - (self._padding * 2)
        d_height = painter.device().height() - (self._padding * 2)
        # end::dimensions[]

        # tag::layout[]
        step_size = d_height / self.n_steps
        bar_height = step_size * self._bar_solid_percent
        # end::layout[]

        # tag::draw[]
        # brush.setColor(QtGui.QColor('yellow'))

        for n in range(n_steps_to_draw):
            brush.setColor(QtGui.QColor(self.steps[n]))
            ypos = (1 + n) * step_size
            rect = QtCore.QRect(
                self._padding,
                self._padding + d_height - int(ypos),
                d_width,
                int(bar_height)
            )
            painter.fillRect(rect, brush)
        # end::draw[]
        painter.end()

        """# test to Get current state
        # ::start
        dial = self.parent()._dial      # this will access the parent's (PowerBar()) ._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)

        font = painter.font()
        font.setFamily('Times')
        font.setPointSize(18)
        painter.setFont(font)

        # determine the number of steps to draw
        # ::start
        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * 5)
        # ::end

        painter.drawText(25, 25, '{}'.format(n_steps_to_draw))
        painter.end()
        # ::end"""

    def _trigger_refresh(self):
        self.update()


class PowerBar(QtWidgets.QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, parent=None, steps=5):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar(steps)

        layout.addWidget(self._bar)

        self._dial = QtWidgets.QDial()
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

        self.setLayout(layout)

    def setColor(self, color):
        self._bar.steps = [color] * self._bar.n_steps
        self._bar.update()

    def setColors(self, colors):
        self._bar.n_steps = len(colors)
        self._bar.steps = colors
        self._bar.update()

    def setBarPadding(self, i):
        self._bar._padding = int(i)
        self._bar.update()

    def setBarSolidPercent(self, f):
        self._bar._bar_solid_percent = float(f)
        self._bar.update()

    def setBackgroundColor(self, color):
        self._bar._background_color = QtGui.QColor(color)
        self._bar.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    bar = PowerBar()
    bar.setColors(
        ["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f",
         "#9e0142"])
    #bar.setColor('yellow')
    bar.setBarPadding(2)
    # bar.setBarSolidPercent(0.9)
    bar.setBackgroundColor('gray')
    bar.show()
    app.exec()

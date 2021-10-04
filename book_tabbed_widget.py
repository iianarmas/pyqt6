from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTabWidget
    )
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)

        tabs.setMovable(True)

        for n, color in enumerate(['red', 'yellow', 'blue', 'green']):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)



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

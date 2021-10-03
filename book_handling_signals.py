from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt

from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'

]


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.n__times_cliked = 0

        self.setWindowTitle('Iian App')

        self.button = QPushButton('Click Here')
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(100, 80))
        self.setMaximumSize(QSize(400, 300))

    def the_button_was_clicked(self):
        self.button.setText('Changed!')
        new_window_title = choice(window_titles)
        print(f'Setting title: {new_window_title}')
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f'Window title changed: {window_title}')

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

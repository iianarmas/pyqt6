from dial import CustomDialog
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

"""
Toolbars accept any widgets
"""


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        button = QPushButton('OPEN DIALOG')
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self):
        """dlg = QMessageBox(self)
        dlg.setWindowTitle('Hello')
        dlg.setText('Are you sure you want to exit?')
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Abort)
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.exec()"""

        # to make things easier:
        dlg = QMessageBox.question(self, 'Hello', 'Are you sure you want to exit?',
                                   defaultButton=QMessageBox.StandardButton.No)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

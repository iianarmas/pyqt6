# =========== MAIN.PY ===========

from dial import CustomDialog
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

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
        dlg = CustomDialog(self)
        dlg.setWindowTitle('Hello')
        dlg.exec()


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

# =========== DIAL.PY ===========

from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('Custom Dialog')

        q_btn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.button_box = QDialogButtonBox(q_btn)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('Something happened, is that OK?')
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)

    def accept(self):
        print('Accepted!')
        self.hide()

    def reject(self) -> None:
        print('Rejected!')
        self.hide()

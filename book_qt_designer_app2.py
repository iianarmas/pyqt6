from test import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QCheckBox, QComboBox, QSpinBox, \
    QLabel, QLineEdit, QPushButton, QWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QSS Tester')

        self.editor = QPlainTextEdit()
        self.editor.textChanged.connect(self.update_styles)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)

        # Define a set of simple widgets
        check_box = QCheckBox('Check this box')
        layout.addWidget(check_box)

        combo_box = QComboBox()
        combo_box.setObjectName('combo')
        combo_box.addItems(['First', 'Second', 'Third', 'Fourth'])
        layout.addWidget(combo_box)

        spin_box = QSpinBox()
        spin_box.setRange(0, 9999)
        layout.addWidget(spin_box)

        label = QLabel()
        label.setText('This is a label')
        layout.addWidget(label)

        line_edit = QLineEdit()
        line_edit.setObjectName('lineedit')
        layout.addWidget(line_edit)

        button = QPushButton()
        button.setText('CLICK HERE')
        layout.addWidget(button)

        self.container = QWidget()
        self.container.setLayout(layout)

        self.setCentralWidget(self.container)

    def update_styles(self):
        qss = self.editor.toPlainText()
        self.setStyleSheet(qss)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

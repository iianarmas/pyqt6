from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QTableView,
    QVBoxLayout,
    QWidget,
    QLabel,
)

import re

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('resources/db/sample_db.sqlite')
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        layout = QVBoxLayout()
        label = QLabel()

        label.setText('Search Name')

        self.search = QLineEdit()
        self.search.textChanged.connect(self.update_filter)

        self.table = QTableView()
        self.model = QSqlTableModel(db=db)

        self.table.setModel(self.model)

        self.model.setTable('Track')
        self.model.select()

        layout.addWidget(self.table)
        layout.addWidget(label)
        layout.addWidget(self.search)
        container.setLayout(layout)

        self.setMinimumSize(QSize(1024, 600))

        self.setCentralWidget(container)

    def update_filter(self, text):
        # text = re.sub("[\W_]+", "", text)
        filter_string = 'Name LIKE "%{}%"'.format(text)
        self.model.setFilter(filter_string)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

# ========== MAIN.PY ========== #

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QTableView,
    QVBoxLayout,
    QWidget,
    QLabel, QPushButton, QListView,
)

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('resources/db/sample_db.sqlite')
db.open()

temp = ''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        layout = QVBoxLayout()
        label = QLabel()

        label.setText('Search Name')

        self.search = QLineEdit()
        self.search.textChanged.connect(self.update_filter)

        # self.table = QTableView()
        self.table = QListView()
        self.model = QSqlQueryModel()

        self.table.setModel(self.model)
        self.query = QSqlQuery(db=db)

        self.query.prepare(
            'SELECT Name FROM Track WHERE Name LIKE "%" || :name || "%"'
        )

        layout.addWidget(self.table)
        layout.addWidget(label)
        layout.addWidget(self.search)
        container.setLayout(layout)

        self.setMinimumSize(QSize(1024, 600))

        self.update_filter()

        self.setCentralWidget(container)

    def execute_query(self):
        self.query.exec()
        self.model.setQuery(self.query)

    def update_filter(self, text=None):
        name = text
        if name == '':
            name = None
            self.query.bindValue(":name", name)

            self.execute_query()
        else:
            self.query.bindValue(":name", name)

            self.execute_query()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

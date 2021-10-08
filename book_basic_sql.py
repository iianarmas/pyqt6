# =============== MAIN.PY =============== #

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from db import db


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.table = QTableView()

        # create the model
        self.model = QSqlTableModel(db=db)

        self.model.setTable('Track')
        self.table.setModel(self.model)

        # sorting
        # index = self.model.fieldIndex('Name')
        # self.model.setSort(index, Qt.SortOrder.DescendingOrder)

        # setting column names
        """self.model.setHeaderData(1, Qt.Orientation.Horizontal, 'Name')
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, 'Album (ID)')
        self.model.setHeaderData(3, Qt.Orientation.Horizontal, 'Media Type (ID)')
        self.model.setHeaderData(4, Qt.Orientation.Horizontal, 'Genre (ID)')
        self.model.setHeaderData(5, Qt.Orientation.Horizontal, 'Composer')"""

        # OR ---------
        column_titles = {
            'Name': 'Name',
            'AlbumId': 'Album (ID)',
            'MediaType': 'Media Type (ID)',
            'GenreId': 'Genre (ID)',
            'Composer': 'Composer',
        }

        for name, text in column_titles.items():
            index = self.field_index(name)
            self.model.setHeaderData(index, Qt.Orientation.Horizontal, text)

        self.model.select()

        self.setMinimumSize(QSize(1024, 600))

        self.setCentralWidget(self.table)

    # since this is used very often, better create a method for it
    def field_index(self, value):
        return self.model.fieldIndex(value)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    
# =============== DB.PY =============== #

from PyQt6.QtSql import QSqlDatabase

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('resources/db/sample_db.sqlite')
db.open()

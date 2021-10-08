# ============= MAIN.PY ============= #

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

import numpy as np


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index: QModelIndex, role: int = ...):
        value = self._data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            return str(value)

        if role == Qt.ItemDataRole.TextAlignmentRole:
            if str(value).isnumeric() or str(value).isascii():
                return Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight

    def rowCount(self, parent: QModelIndex = ...):
        return self._data.shape[0]

    def columnCount(self, parent: QModelIndex = ...):
        return self._data.shape[1]


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QTableView')

        self.table = QTableView()

        data = np.array([
            [1, 9, 2],
            [1, 0, -1],
            [3, 5, 2],
            [3, 3, 2],
            [5, 8, 9],
        ])

        self.model = TableModel(data)
        self.table.setModel(self.model)

        # manually print the row, column, and value of selected item
        # self.table.pressed.connect(self.index_print)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 300, 400, 200)

    # manually print the row, column, and value of selected item
    """def index_print(self, index):
        print(f'Row: {index.row() + 1}\nColumn: {index.column() + 1}')
        print(f'Value: {self.model._data[index.row()][index.column()]}')"""


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

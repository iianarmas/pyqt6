# ============= MAIN.PY ============= #

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

        if role == Qt.ItemDataRole.BackgroundRole and self._data[index.row()][index.column()] >= 5:
            return QColor(Qt.GlobalColor.cyan)

        if role == Qt.ItemDataRole.BackgroundRole and self._data[index.row()][index.column()] < 1:
            return QColor(Qt.GlobalColor.red)

        if role == Qt.ItemDataRole.ForegroundRole and self._data[index.row()][index.column()] < 1:
            return QColor(Qt.GlobalColor.yellow)

    def rowCount(self, parent: QModelIndex = ...):
        return len(self._data)

    def columnCount(self, parent: QModelIndex = ...):
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QTableView')

        self.table = QTableView()

        data = [
            [4, 9, 2],
            [1, -1, -1],
            [3, 5, -5],
            [3, 3, 2],
            [7, 8, 9]
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        # manually print the row, column, and value of selected item
        # self.table.pressed.connect(self.index_print)

        self.setCentralWidget(self.table)

    # manually print the row, column, and value of selected item
    """def index_print(self, index):
        print(f'Row: {index.row() + 1}\nColumn: {index.column() + 1}')
        print(f'Value: {self.model._data[index.row()][index.column()]}')"""



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

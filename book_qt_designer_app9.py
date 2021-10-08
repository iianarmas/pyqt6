from PyQt6.QtCore import QSize
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QTableView,
    QVBoxLayout,
    QWidget,
    QLabel, QHBoxLayout,
)

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('resources/db/sample_db.sqlite')
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        layout_search = QHBoxLayout()

        label = QLabel()
        label.setText('Search')

        self.track = QLineEdit()
        self.track.setPlaceholderText('Track Name...')
        self.track.textChanged.connect(self.update_query)

        self.composer = QLineEdit()
        self.composer.setPlaceholderText('Artist Name...')
        self.composer.textChanged.connect(self.update_query)

        self.album = QLineEdit()
        self.album.setPlaceholderText('Album Title...')
        self.album.textChanged.connect(self.update_query)

        layout_search.addWidget(self.track)
        layout_search.addWidget(self.composer)
        layout_search.addWidget(self.album)

        layout_view = QVBoxLayout()
        layout_view.addWidget(label)
        layout_view.addLayout(layout_search)

        self.table = QTableView()
        layout_view.addWidget(self.table)

        container.setLayout(layout_view)

        self.model = QSqlQueryModel()
        self.table.setModel(self.model)

        self.query = QSqlQuery(db=db)

        self.query.prepare(
            "SELECT Name, Composer, Album.Title FROM Track "
            "INNER JOIN Album ON Track.AlbumId=Album.AlbumId WHERE "
            "Track.Name LIKE '%' || :track_name || '%' AND "
            "Track.Composer LIKE '%' || :track_composer || '%' AND "
            "Album.Title LIKE '%' || :album_title || '%'"
        )

        self.update_query()

        self.setMinimumSize(QSize(1024, 600))

        self.setCentralWidget(container)

    def execute_query(self):
        self.query.exec()
        self.model.setQuery(self.query)

    def update_query(self, text=None):
        track_name = self.track.text()
        track_composer = self.composer.text()
        album_title = self.album.text()

        # to populate table with all values at start up
        """self.query.bindValue(':track_name', track_name)
        self.query.bindValue(':track_composer', track_composer)
        self.query.bindValue(':album_title', album_title)"""

        # to show blank table on start up
        if track_name == '' and track_composer == '' and album_title == '':
            track_name, track_composer, album_title = None, None, None
            self.query.bindValue(':track_name', track_name)
            self.query.bindValue(':track_composer', track_composer)
            self.query.bindValue(':album_title', album_title)

            self.execute_query()
        else:
            self.query.bindValue(':track_name', track_name)
            self.query.bindValue(':track_composer', track_composer)
            self.query.bindValue(':album_title', album_title)

            self.execute_query()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

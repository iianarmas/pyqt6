from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

    # signal-based approach
        """self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        save_action = QAction('Save', self)
        save_action.setShortcut(QKeySequence('Ctrl+S'))
        context.addAction(save_action)
        context.addAction(QAction('test 2', self))
        context.addAction(QAction('test 3', self))
        context.exec(self.mapToGlobal(pos))"""

    # direct approach
    def contextMenuEvent(self, e):
        context = QMenu(self)
        save_action = QAction('Save', self)
        save_action.setShortcut(QKeySequence('Ctrl+S'))
        context.addAction(save_action)
        context.addAction(QAction('test 2', self))
        context.addAction(QAction('test 3', self))
        context.exec(e.globalPos())


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox

"""
Toolbars accept any widgets
"""


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Iian App')

        label = QLabel()
        label.setText('Hello World!')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        # creating tool bar
        toolbar = QToolBar('My Tool Bar')
        # set icon size for icons not to have lots of paddings
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        # adding tool bar to windows
        self.addToolBar(toolbar)

        # creating tool bar actions
        self.file_action = QAction(QIcon('icons-shadowless/bug.png'), 'Debug', self)
        self.file_action.setStatusTip('This contains all your files')
        self.file_action.triggered.connect(self.on_my_file_toolbar_click)

        # make action toggleable
        self.file_action.setCheckable(True)

        self.edit_action = QAction(QIcon('icons-shadowless/anchor.png'), 'Edit', self)
        self.edit_action.setStatusTip('Edit your files')
        self.edit_action.triggered.connect(self.on_my_edit_toolbar_click)

        # make action toggleable
        self.edit_action.setCheckable(True)

        toolbar.addWidget(QLabel('Just a Label for the Toolbar'))

        toolbar.addSeparator()

        toolbar.addAction(self.file_action)

        toolbar.addSeparator()

        toolbar.addAction(self.edit_action)

        toolbar.addSeparator()

        toolbar.addWidget(QCheckBox('Check here'))

        self.setStatusBar(QStatusBar(self))

        # creating menu bar
        menu = self.menuBar()

        file_menu = menu.addMenu('&File')

        # creating actions
        new_file = QAction('New File', self)
        new_file.setStatusTip('Create new file')
        new_file.setShortcut(QKeySequence('Ctrl+Alt+Shift+N'))
        new_file.triggered.connect(self.new)

        # creating a sub menu ========================

        open_file = QAction('Open File', self)
        open_file.setStatusTip('Open File')
        open_file.setShortcut(QKeySequence('Ctrl+O'))
        open_file.triggered.connect(self.open_file)

        open_folder = QAction('Open Folder', self)
        open_folder.setStatusTip('Open Folder')
        open_folder.setShortcut(QKeySequence('Ctrl+Shift+O'))
        open_folder.triggered.connect(self.open_file)

        # ============================================

        save = QAction('&Save', self)
        save.setStatusTip('Save current file')
        save.setShortcut(QKeySequence('Ctrl+S'))
        save.triggered.connect(self.save_file)

        # adding menus
        file_menu.addAction(new_file)
        file_menu.addAction(save)

        # adding a sub menu
        open_menu = file_menu.addMenu('&Open')
        open_menu.addAction(open_file)
        open_menu.addAction(open_folder)

        file_menu.addSeparator()
        file_menu.addAction(self.file_action)
        file_menu.addAction(self.edit_action)

        # creating second menu
        edit_menu = menu.addMenu('&Edit')

    def open_file(self):
        print('Openned!')

    def new(self):
        print('Created New File!')

    def save_file(self):
        print('Saved!')

    def on_my_file_toolbar_click(self, s):
        print(f'File {s}')
        self.edit_action.setCheckable(False)

    def on_my_edit_toolbar_click(self, s):
        print(f'Edit {s}')


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()

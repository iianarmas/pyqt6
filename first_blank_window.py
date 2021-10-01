from PyQt6.QtWidgets import QApplication, QWidget
import sys

# create QAppication Object
app = QApplication(sys.argv)

# create QWidget Object
window = QWidget()

# then show window
window.show()

# exit window
sys.exit(app.exec())

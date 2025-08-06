import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('My First PyQt5 App')
window.setGeometry(100, 100, 300, 200)

label = QLabel('Hello, PyQt5!', window)
label.move(100, 80)

window.show()
sys.exit(app.exec_())

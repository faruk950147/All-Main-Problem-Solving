from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import sys

def on_click():
    label.setText("Button clicked!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5 Button Example')
window.setGeometry(100, 100, 300, 200)

label = QLabel('Hello, PyQt5!', window)
label.move(100, 50)

button = QPushButton('Click Me', window)
button.move(100, 100)
button.clicked.connect(on_click)

window.show()
sys.exit(app.exec_())

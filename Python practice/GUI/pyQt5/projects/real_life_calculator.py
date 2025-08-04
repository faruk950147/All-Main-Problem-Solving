import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt

class RealLifeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; height: 40px;")

        # Button labels
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        # Grid layout
        grid = QGridLayout()

        # Add buttons
        positions = [(i, j) for i in range(4) for j in range(4)]
        for position, button_text in zip(positions, buttons):
            button = QPushButton(button_text)
            button.setFixedSize(60, 40)
            button.setStyleSheet("font-size: 16px;")
            button.clicked.connect(self.on_click)
            grid.addWidget(button, *position)

        # Overall layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.display)
        vbox.addLayout(grid)

        self.setLayout(vbox)
        self.setWindowTitle('Real Life PyQt5 Calculator')
        self.show()

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = RealLifeCalculator()
    sys.exit(app.exec_())

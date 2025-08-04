import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGridLayout,
    QVBoxLayout, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe - PyQt6")
        self.setFixedSize(320, 400)

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.status_label = QLabel(f"Player {self.current_player}'s turn")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 18px; margin: 10px;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.status_label)

        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)

        self.restart_btn = QPushButton("🔁 Restart")
        self.restart_btn.setStyleSheet("font-size: 16px; height: 40px;")
        self.restart_btn.clicked.connect(self.restart_game)
        self.layout.addWidget(self.restart_btn)

        self.setLayout(self.layout)

        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = QPushButton("")
                btn.setFixedSize(90, 90)
                btn.setStyleSheet("font-size: 28px;")
                btn.clicked.connect(lambda checked, r=row, c=col: self.handle_click(r, c))
                self.grid.addWidget(btn, row, col)
                self.buttons[row][col] = btn

    def handle_click(self, row, col):
        if self.buttons[row][col].text() == "" and not self.check_winner(self.current_player):
            self.buttons[row][col].setText(self.current_player)
            self.board[row][col] = self.current_player

            if self.check_winner(self.current_player):
                self.status_label.setText(f"🎉 Player {self.current_player} wins!")
                self.disable_board()
                QMessageBox.information(self, "Game Over", f"🎉 Player {self.current_player} wins!")
            elif self.is_full():
                self.status_label.setText("🤝 It's a draw!")
                QMessageBox.information(self, "Game Over", "🤝 It's a draw!")
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.setText(f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        b = self.board
        return (
            any(all(cell == player for cell in row) for row in b) or
            any(all(b[r][c] == player for r in range(3)) for c in range(3)) or
            all(b[i][i] == player for i in range(3)) or
            all(b[i][2 - i] == player for i in range(3))
        )

    def is_full(self):
        return all(cell != "" for row in self.board for cell in row)

    def disable_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setDisabled(True)

    def restart_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.status_label.setText(f"Player {self.current_player}'s turn")

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")
                self.buttons[row][col].setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())

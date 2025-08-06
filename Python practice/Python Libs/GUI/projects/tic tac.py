import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Tkinter GUI")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.root, text="", font=('Helvetica', 20), width=6, height=2,
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner(self.current_player):
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player

            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"🎉 Player {self.current_player} wins!")
                self.disable_all_buttons()
            elif self.is_full():
                messagebox.showinfo("Game Over", "🤝 It's a draw!")
                self.disable_all_buttons()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

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

    def disable_all_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["state"] = "disabled"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

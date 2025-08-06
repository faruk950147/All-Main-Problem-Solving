class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        print("\n")
        for row in self.board: # print row   
            print(" | ".join(row)) # print column
            print("-" * 10) # print horizontal line for each row
        print("\n")

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row): # check all cells in row are same
                return True
        # Check columns
        for col in range(3):
            if all( self.board[row][col] == player for row in range(3)): # check all cells in column are same
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)): # check all cells in diagonal are same
            return True
        if all(self.board[i][2 - i] == player for i in range(3)): # check all cells in reverse diagonal are same
            return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row) # check all cells are not empty

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X" # switch player

    def play(self):
        print("Tic Tac Toe - Two Player Game")
        self.print_board()

        while True:
            try:
                row = int(input(f"Player {self.current_player}, enter row (0-2): "))
                col = int(input(f"Player {self.current_player}, enter col (0-2): "))
            except ValueError:
                print("Invalid input. Use numbers between 0 and 2.")
                continue

            if row not in range(3) or col not in range(3): # check row and column index range is between 0 and 2
                print("Row and Column must be between 0 and 2.")
                continue
            if self.board[row][col] != " ": # is not empty cell
                print("That cell is already taken. Try again.")
                continue

            self.board[row][col] = self.current_player
            self.print_board()

            if self.check_winner(self.current_player): # check winner
                print(f"Player {self.current_player} wins!")
                break

            if self.is_full(): # check all cells are not empty
                print("It's a draw!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()

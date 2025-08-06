def print_board(board):
    print("\n")
    for row in board: # print row   
        print(" | ".join(row)) # print column
        print("-" * 10) # print horizontal line for each row
    print("\n")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row): # check all cells in row are same
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)): # check all cells in column are same
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)): # check all cells in diagonal are same
        return True
    if all(board[i][2 - i] == player for i in range(3)): # check all cells in reverse diagonal are same
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row) # check all cells are not empty

def tic_tac_toe():
    # create two dimension list using list comprehension for row and column
    # and append in board list
    board = [
        [" " for _ in range(3)] # create row
        for _ in range(3) # create column
    ] 
    current_player = "X"
    print("Tic Tac Toe - Two Player Game")
    print_board(board)
    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter col (0-2): "))
        except ValueError:
            print("Invalid input. Use numbers between 0 and 2.")
            continue

        if row not in range(3) or col not in range(3): # check row and column index range is between 0 and 2
            print("Row and Column must be between 0 and 2.")
            continue
        if board[row][col] != " ": # is not empty cell
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
    
if __name__ == "__main__":
    tic_tac_toe()
#!/usr/bin/python3



def print_board(board):
    """Prints the current Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there's a winner on the board."""
    
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

   
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    """Checks if the board is full and it's a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main game loop."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get row input
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 0, 1, or 2.")

        # Get column input
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 0, 1, or 2.")

        # Place mark if empty
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken! Try again.")
            continue  # ask input again

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
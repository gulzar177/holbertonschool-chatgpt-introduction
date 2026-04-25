#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)

def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in [0,1,2] or col not in [0,1,2]:
                print("Invalid position. Use 0, 1, or 2.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row, col = get_move(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

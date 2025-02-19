def display(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def win(board, display):
    for row_index in range(3):
        if all(board[row_index][col_index] == display for col_index in range(3)) or all(board[col_index][row_index] == display for col_index in range(3)):
            return True
    if all(board[row_index][row_index] == display for row_index in range(3)) or all(board[row_index][2 - row_index] == display for row_index in range(3)):
        return True
    return False


def full(board):
    return all(column != " " for row in board for column in row)


def turn():
    board = [[" " for _ in range(3)] for _ in range(3)]
    display = ["X", "O"]
    print("Tic-Tac-Toe Game")
    display(board)
    for turn in range(9):
        player = display[turn % 2]
        while 1:
            try:
                row, column = map(int, input(f"P {player}, row col (0-2): ").split())
                if board[row][column] == " ":
                    board[row][column] = player
                    break
                else:
                    print("Nope. Again.")
            except:
                print("Wrong. 0-2 pls.")
        display(board)
        if win(board, player):
            print(f"P {player} wins!")
            return
        if full(board):
            print("Draw!")
            return
    print("Draw!")


turn()

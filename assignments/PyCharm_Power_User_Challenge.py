def display_board(board):
    """

    :param board:
    :type board:
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def win(board, player):
    """

    :param board:
    :type board:
    :param player:
    :type player:
    :return:
    :rtype:
    """
    for row_index in range(3):
        if all(board[row_index][col_index] == player for col_index in range(3)) or all(
                board[col_index][row_index] == player for col_index in range(3)):
            return True
    if all(board[row_index][row_index] == player for row_index in range(3)) or all(
            board[row_index][2 - row_index] == player for row_index in range(3)):
        return True
    return False


def full(board):
    """

    :param board:
    :type board:
    :return:
    :rtype:
    """
    return all(column != " " for row in board for column in row)


def play_game():
    """

    :return:
    :rtype:
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    display_team = ["X", "O"]
    print("Tic-Tac-Toe Game")
    display_board(board)
    for turn_amount in range(9):
        current_player = display_team[turn_amount % 2]
        get_player_move(board, current_player)
        display_board(board)
        if win(board, current_player):
            print(f"P {current_player} wins!")
            return
        if full(board):
            print("Draw!")
            return
    print("Draw!")


def get_player_move(board, current_player):
    """

    :param board:
    :type board:
    :param current_player:
    :type current_player:
    """
    while 1:
        try:
            row, column = map(int, input(f"P {current_player}, row col (0-2): ").split())
            if board[row][column] == " ":
                board[row][column] = current_player
                break
            else:
                print("Nope. Again.")
        except ValueError:
            print("Wrong. 0-2 pls.")


play_game()

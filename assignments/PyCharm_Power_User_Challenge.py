def display_board(board):
    """
    Display the current state of the Tic-Tac-Toe board.

    :param board: A 3x3 list representing the game board
    :type board: list of lists
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def win(board, player):
    """
    Check if the current player has won the game.

    :param board: A 3x3 list representing the game board
    :type board: list of lists
    :param player: The current player's symbol ('X' or 'O')
    :type player: str
    :return: True if the player has won, False otherwise
    :rtype: bool
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
    Check if the game board is completely filled.

    :param board: A 3x3 list representing the game board
    :type board: list of lists
    :return: True if the board is full, False otherwise
    :rtype: bool
    """
    return all(column != " " for row in board for column in row)


def play_game():
    """
    Main function to play the Tic-Tac-Toe game.

    This function initializes the game, manages turns, and determines the game outcome.

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
    Get and validate the current player's move.

    :param board: A 3x3 list representing the game board
    :type board: list of lists
    :param current_player: The current player's symbol ('X' or 'O')
    :type current_player: str
    """
    while 1:
        try:
            row, column = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
            if board[row][column] == " ":
                board[row][column] = current_player
                break
            else:
                print("Nope. Again.")
        except ValueError:
            print("Wrong. 0-2 pls.")


play_game()

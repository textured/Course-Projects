import classes


def create_board(game: object, arrangement: str) -> list:
    """ creates a board by using a list """
    board = []
    for row in range(game.row):
        board.append([])
        for col in range(game.col):
            board[row].append('.')

    x = int((game.row / 2) - 1)
    y = int((game.col / 2) - 1)

    if arrangement == 'Black':
        board[x][y] = 'Black'
        board[x + 1][y + 1] = 'Black'
        board[x][y + 1] = 'White'
        board[x + 1][y] = 'White'

    elif arrangement == 'White':
        board[x][y] = 'White'
        board[x + 1][y + 1] = 'White'
        board[x][y + 1] = 'Black'
        board[x + 1][y] = 'Black'

    return board


def check_move(game: object, turn: object, board: list, move_row: int, move_col: int) -> bool:
    """ checks if a move is valid or not and returns a boolean based on validity """

    if turn.get_turn() == 'Black':
        player_1 = 'Black'
        player_2 = 'White'

    elif turn.get_turn() == 'White':
        player_1 = 'White'
        player_2 = 'Black'

    # Convert to array format
    move_row -= 1
    move_col -= 1

    if turn.get_turn() == player_1:
        if board[move_row][move_col] == player_1 or board[move_row][move_col] == player_2:
            raise classes.InvalidMoveError()

        elif board[move_row][move_col] == '.':

            if move_row == game.row - 1 and move_col != 0 and move_col != game.col - 1:  # Piece on bottom row
                if board[move_row - 1][move_col] == player_2:  # North
                    i = 0
                    while move_row - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col] == player_1:
                            return True
                        elif move_row - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row][move_col - 1] == player_2:  # West
                    i = 0
                    while move_col - 1 - i >= 0:
                        if board[move_row][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row][move_col - 1 - i] == player_1:
                            return True
                        elif move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row][move_col + 1] == player_2:  # East
                    i = 0
                    while move_col + 1 + i <= game.col - 1:
                        if board[move_row][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row][move_col + 1 + i] == player_1:
                            return True
                        elif move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row - 1][move_col - 1] == player_2:  # NW
                    i = 0
                    while move_row - 1 - i >= 0 and move_col - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col - 1 - i] == player_1:
                            return True
                        elif move_row - 1 - i < 0 and move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row - 1][move_col + 1] == player_2:  # NE
                    i = 0
                    while move_row - 1 - i >= 0 and move_col + 1 + i <= game.col - 1:
                        if board[move_row - 1 - i][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col + 1 + i] == player_1:
                            return True
                        elif move_row - 1 - i < 0 and move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()

            elif move_row == game.row - 1 and move_col == 0:  # Piece on bottom left corner
                if board[move_row - 1][move_col] == player_2:  # North
                    i = 0
                    while move_row - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col] == player_1:
                            return True
                        elif move_row - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row][move_col + 1] == player_2:  # East
                    i = 0
                    while move_col + 1 + i <= game.col - 1:
                        if board[move_row][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row][move_col + 1 + i] == player_1:
                            return True
                        elif move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row - 1][move_col + 1] == player_2:  # NE
                    i = 0
                    while move_row - 1 - i >= 0 and move_col + 1 + i <= game.col - 1:
                        if board[move_row - 1 - i][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col + 1 + i] == player_1:
                            return True
                        elif move_row - 1 - i < 0 and move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()

            elif move_row == game.row - 1 and move_col == game.col - 1:  # Piece on bottom right corner
                if board[move_row - 1][move_col] == player_2:  # North
                    i = 0
                    while move_row - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col] == player_1:
                            return True
                        elif move_row - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row][move_col - 1] == player_2:  # West
                    i = 0
                    while move_col - 1 - i >= 0:
                        if board[move_row][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row][move_col - 1 - i] == player_2:
                            return True
                        elif move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row - 1][move_col - 1] == player_2:  # NW
                    i = 0
                    while move_row - 1 - i >= 0 and move_col - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col - 1 - i] == player_1:
                            return True
                        elif move_row - 1 - i < 0 and move_col - 1 - i < 0:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()

            elif move_col == game.col - 1 and move_row != 0 and move_row != game.row - 1:  # Far right column
                if board[move_row - 1][move_col] == player_2:  # North
                    i = 0
                    while move_row - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col] == player_1:
                            return True
                        elif move_row - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row + 1][move_col] == player_2:  # South
                    i = 0
                    while move_row + 1 + i <= game.row - 1:
                        if board[move_row + 1 + i][move_col] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1:
                            break
                        else:
                            break
                if board[move_row][move_col - 1] == player_2:  # West
                    i = 0
                    while move_col - 1 - i >= 0:
                        if board[move_row][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row][move_col - 1 - i] == player_1:
                            return True
                        elif move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row - 1][move_col - 1] == player_2:  # NW
                    i = 0
                    while move_row - 1 - i >= 0 and move_col - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col - 1 - i] == player_1:
                            return True
                        elif move_row - 1 - i < 0 and move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row + 1][move_col - 1] == player_2:  # SW
                    i = 0
                    while move_row + 1 + i <= game.row - 1 and move_col - 1 - i >= 0:
                        if board[move_row + 1 + i][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col - 1 - i] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1 and move_col - 1 - i < 0:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()

            elif move_col == 0 and move_row != 0 and move_row != game.row - 1:  # Far left column
                if board[move_row - 1][move_col] == player_2:  # North
                    i = 0
                    while move_row - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col] == player_1:
                            return True
                        elif move_row - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row + 1][move_col] == player_2:  # South
                    i = 0
                    while move_row + 1 + i <= game.row - 1:
                        if board[move_row + 1 + i][move_col] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1:
                            break
                        else:
                            break
                if board[move_row][move_col + 1] == player_2:  # East
                    i = 0
                    while move_col + 1 + i <= game.col - 1:
                        if board[move_row][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row][move_col + 1 + i] == player_1:
                            return True
                        elif move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row - 1][move_col + 1] == player_2:  # NE
                    i = 0
                    while move_row - 1 - i >= 0 and move_col + 1 + i < game.col - 1:
                        if board[move_row - 1 - i][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col + 1 + i] == player_1:
                            return True
                        elif move_row - 1 - i < 0 and move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row + 1][move_col + 1] == player_2:  # SE
                    i = 0
                    while move_row + 1 + i <= game.row - 1 and move_col + 1 + i <= game.col - 1:
                        if board[move_row + 1 + i][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col + 1 + i] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1 and move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()

            elif move_row == 0 and move_col != 0 and move_col != game.col - 1:  # Top row
                if board[move_row + 1][move_col] == player_2:  # South
                    i = 0
                    while move_row + 1 + i <= game.row - 1:
                        if board[move_row + 1 + i][move_col] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1:
                            break
                        else:
                            break
                if board[move_row][move_col - 1] == player_2:  # West
                    i = 0
                    while move_col - 1 - i >= 0:
                        if board[move_row][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row][move_col - 1 - i] == player_1:
                            return True
                        elif move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row][move_col + 1] == player_2:  # East
                    i = 0
                    while move_col + 1 + i <= game.col - 1:
                        if board[move_row][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row][move_col + 1 + i] == player_1:
                            return True
                        elif move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row + 1][move_col + 1] == player_2:  # SE
                    i = 0
                    while move_row + 1 + i <= game.row - 1 and move_col + 1 + i <= game.col - 1:
                        if board[move_row + 1 + i][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col + 1 + i] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1 and move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row + 1][move_col - 1] == player_2:  # SW
                    i = 0
                    while move_row + 1 + i <= game.row - 1 and move_col - 1 - i >= 0:
                        if board[move_row + 1 + i][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col - 1 - i] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1 and move_col - 1 - i < 0:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()

            elif move_row == 0 and move_col == 0:  # Top left corner
                if board[move_row + 1][move_col] == player_2:  # South
                    i = 0
                    while move_row + 1 + i <= game.row - 1:
                        if board[move_row + 1 + i][move_col] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1:
                            break
                        else:
                            break
                if board[move_row][move_col + 1] == player_2:  # East
                    i = 0
                    while move_col + 1 + i <= game.col - 1:
                        if board[move_row][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row][move_col + 1 + i] == player_1:
                            return True
                        elif move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row + 1][move_col + 1] == player_2:  # SE
                    i = 0
                    while move_row + 1 + i <= game.row - 1 and move_col + 1 + i <= game.col - 1:
                        if board[move_row + 1 + i][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col + 1 + i] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1 and move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()

            elif move_row == 0 and move_col == game.col - 1:  # Top right corner
                if board[move_row + 1][move_col] == player_2:  # South
                    i = 0
                    while move_row + 1 + i <= game.row - 1:
                        if board[move_row + 1 + i][move_col] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1:
                            break
                        else:
                            break
                if board[move_row][move_col - 1] == player_2:  # West
                    i = 0
                    while move_col - 1 - i >= 0:
                        if board[move_row][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row][move_col - 1 - i] == player_1:
                            return True
                        elif move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row + 1][move_col - 1] == player_2:  # SW
                    i = 0
                    while move_row + 1 + i <= game.row - 1 and move_col - 1 - i >= 0:
                        if board[move_row + 1 + i][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col - 1 - i] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1 and move_col - 1 - i < 0:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()

            else:
                if board[move_row - 1][move_col] == player_2:  # North
                    i = 0
                    while move_row - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col] == player_1:
                            return True
                        elif move_row - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row + 1][move_col] == player_2:  # South
                    i = 0
                    while move_row + 1 + i <= game.row - 1:
                        if board[move_row + 1 + i][move_col] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1:
                            break
                        else:
                            break
                if board[move_row][move_col - 1] == player_2:  # West
                    i = 0
                    while move_col - 1 - i >= 0:
                        if board[move_row][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row][move_col - 1 - i] == player_1:
                            return True
                        elif move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row][move_col + 1] == player_2:  # East
                    i = 0
                    while move_col + 1 + i <= game.col - 1:
                        if board[move_row][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row][move_col + 1 + i] == player_1:
                            return True
                        elif move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row - 1][move_col - 1] == player_2:  # NW
                    i = 0
                    while move_row - 1 - i >= 0 and move_col - 1 - i >= 0:
                        if board[move_row - 1 - i][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col - 1 - i] == player_1:
                            return True
                        elif move_row - 1 - i < 0 and move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row - 1][move_col + 1] == player_2:  # NE
                    i = 0
                    while move_row - 1 - i >= 0 and move_col + 1 + i < game.col - 1:
                        if board[move_row - 1 - i][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row - 1 - i][move_col + 1 + i] == player_1:
                            return True
                        elif move_row - 1 - i < 0 and move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break
                if board[move_row + 1][move_col - 1] == player_2:  # SW
                    i = 0
                    while move_row + 1 + i <= game.row - 1 and move_col - 1 - i >= 0:
                        if board[move_row + 1 + i][move_col - 1 - i] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col - 1 - i] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1 and move_col - 1 - i < 0:
                            break
                        else:
                            break
                if board[move_row + 1][move_col + 1] == player_2:  # SE
                    i = 0
                    while move_row + 1 + i <= game.row - 1 and move_col + 1 + i <= game.col - 1:
                        if board[move_row + 1 + i][move_col + 1 + i] == player_2:
                            i += 1
                        elif board[move_row + 1 + i][move_col + 1 + i] == player_1:
                            return True
                        elif move_row + 1 + i > game.row - 1 and move_col + 1 + i > game.col - 1:
                            break
                        else:
                            break

                raise classes.InvalidMoveError()


def make_move(game: object, turn: object, board: list, move_row: int, move_col: int) -> None:
    """ Makes move on the board given row # and column # """
    object_list = []

    if turn.get_turn() == 'Black':
        player_1 = 'Black'
        player_2 = 'White'
    elif turn.get_turn() == 'White':
        player_1 = 'White'
        player_2 = 'Black'

    # Convert to array format
    move_row -= 1
    move_col -= 1

    if turn.get_turn() == player_1:
        if board[move_row][move_col] == '.':

            if move_row == 0 and move_col != 0 and move_col != game.col - 1:  # Top row
                if board[move_row + 1][move_col] == player_2:  # South
                    south = classes.South()
                    object_list.append(south)
                if board[move_row][move_col - 1] == player_2:  # West
                    west = classes.West()
                    object_list.append(west)
                if board[move_row][move_col + 1] == player_2:  # East
                    east = classes.East()
                    object_list.append(east)
                if board[move_row + 1][move_col + 1] == player_2:  # SE
                    south_east = classes.SouthEast()
                    object_list.append(south_east)
                if board[move_row + 1][move_col - 1] == player_2:  # SW
                    south_west = classes.SouthWest()
                    object_list.append(south_west)

            elif move_row == 0 and move_col == 0:  # Top left corner
                if board[move_row + 1][move_col] == player_2:  # South
                    south = classes.South()
                    object_list.append(south)
                if board[move_row][move_col + 1] == player_2:  # East
                    east = classes.East()
                    object_list.append(east)
                if board[move_row + 1][move_col + 1] == player_2:  # SE
                    south_east = classes.SouthEast()
                    object_list.append(south_east)

            elif move_row == 0 and move_col == game.col - 1:  # Top right corner
                if board[move_row + 1][move_col] == player_2:  # South
                    south = classes.South()
                    object_list.append(south)
                if board[move_row][move_col - 1] == player_2:  # West
                    west = classes.West()
                    object_list.append(west)
                if board[move_row + 1][move_col - 1] == player_2:  # SW
                    south_west = classes.SouthWest()
                    object_list.append(south_west)

            elif move_col == game.col - 1 and move_row != 0 and move_row != game.row - 1:  # Far right column
                if board[move_row - 1][move_col] == player_2:  # North
                    north = classes.North()
                    object_list.append(north)
                if board[move_row + 1][move_col] == player_2:  # South
                    south = classes.South()
                    object_list.append(south)
                if board[move_row][move_col - 1] == player_2:  # West
                    west = classes.West()
                    object_list.append(west)
                if board[move_row - 1][move_col - 1] == player_2:  # NW
                    north_west = classes.NorthWest()
                    object_list.append(north_west)
                if board[move_row + 1][move_col - 1] == player_2:  # SW
                    south_west = classes.SouthWest()
                    object_list.append(south_west)

            elif move_col == 0 and move_row != 0 and move_row != game.row - 1:  # Far left column
                if board[move_row - 1][move_col] == player_2:  # North
                    north = classes.North()
                    object_list.append(north)
                if board[move_row + 1][move_col] == player_2:  # South
                    south = classes.South()
                    object_list.append(south)
                if board[move_row][move_col + 1] == player_2:  # East
                    east = classes.East()
                    object_list.append(east)
                if board[move_row - 1][move_col + 1] == player_2:  # NE
                    north_east = classes.NorthEast()
                    object_list.append(north_east)
                if board[move_row + 1][move_col + 1] == player_2:  # SE
                    south_east = classes.SouthEast()
                    object_list.append(south_east)

            elif move_row == game.row - 1 and move_col != 0 and move_col != game.col - 1:  # Piece on bottom row
                if board[move_row - 1][move_col] == player_2:  # North
                    north = classes.North()
                    object_list.append(north)
                if board[move_row][move_col - 1] == player_2:  # West
                    west = classes.West()
                    object_list.append(west)
                if board[move_row][move_col + 1] == player_2:  # East
                    east = classes.East()
                    object_list.append(east)
                if board[move_row - 1][move_col - 1] == player_2:  # NW
                    north_west = classes.NorthWest()
                    object_list.append(north_west)
                if board[move_row - 1][move_col + 1] == player_2:  # NE
                    north_east = classes.NorthEast()
                    object_list.append(north_east)

            elif move_row == game.row - 1 and move_col == 0:  # Piece on bottom left corner
                if board[move_row - 1][move_col] == player_2:  # North
                    north = classes.North()
                    object_list.append(north)
                if board[move_row][move_col + 1] == player_2:  # East
                    east = classes.East()
                    object_list.append(east)
                if board[move_row - 1][move_col + 1] == player_2:  # NE
                    north_east = classes.NorthEast()
                    object_list.append(north_east)

            elif move_row == game.row - 1 and move_col == game.col - 1:  # Piece on bottom right corner
                if board[move_row - 1][move_col] == player_2:  # North
                    north = classes.North()
                    object_list.append(north)
                if board[move_row][move_col - 1] == player_2:  # West
                    west = classes.West()
                    object_list.append(west)
                if board[move_row - 1][move_col - 1] == player_2:  # NW
                    north_west = classes.NorthWest()
                    object_list.append(north_west)

            else:
                if board[move_row - 1][move_col] == player_2:  # North
                    north = classes.North()
                    object_list.append(north)
                if board[move_row + 1][move_col] == player_2:  # South
                    south = classes.South()
                    object_list.append(south)
                if board[move_row][move_col - 1] == player_2:  # West
                    west = classes.West()
                    object_list.append(west)
                if board[move_row][move_col + 1] == player_2:  # East
                    east = classes.East()
                    object_list.append(east)
                if board[move_row - 1][move_col - 1] == player_2:  # NW
                    north_west = classes.NorthWest()
                    object_list.append(north_west)
                if board[move_row - 1][move_col + 1] == player_2:  # NE
                    north_east = classes.NorthEast()
                    object_list.append(north_east)
                if board[move_row + 1][move_col - 1] == player_2:  # SW
                    south_west = classes.SouthWest()
                    object_list.append(south_west)
                if board[move_row + 1][move_col + 1] == player_2:  # SE
                    south_east = classes.SouthEast()
                    object_list.append(south_east)

    move_row += 1
    move_col += 1

    for item in object_list:
        item.check_move(game, turn, board, move_row, move_col)

    turn.make_move(game, board, move_row, move_col)


def check_for_valid_turns(game: object, turn: object, board: list) -> bool:
    """
    Before every move, makes sure there is minimum one valid move on the board
    """

    for row in range(game.row):
        for col in range(game.col):
            if board[row][col] == '.':
                try:
                    if check_move(game, turn, board, row + 1, col + 1):
                        return True
                except classes.InvalidMoveError:
                    pass

    return False

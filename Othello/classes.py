class InvalidMoveError(Exception):
    """ raise invalid move if called """
    pass


class Game:
    """ class that contains attributes of the game """
    def __init__(self):
        self.state = 'ACTIVE'

    def row(self, row: int) -> int:
        self.row = row

    def col(self, col: int) -> int:
        self.col = col

    def get_black_count(self, board: list) -> int:
        self.black_disc = 0
        for row in range(self.row):
            for col in range(self.col):
                if board[row][col] == 'Black':
                    self.black_disc += 1

        return self.black_disc

    def get_white_count(self, board: list) -> int:
        self.white_disc = 0
        for row in range(self.row):
            for col in range(self.col):
                if board[row][col] == 'White':
                    self.white_disc += 1

        return self.white_disc

    def game_rule(self, board, game_rule) -> str:
        """ determines how the game is won """

        if game_rule == '>':
            if self.get_black_count(board) > self.get_white_count(board):
                self.state = 'WIN'
                return 'WINNER: {}'.format('Black')
            elif self.get_white_count(board) > self.get_black_count(board):
                self.state = 'WIN'
                return 'WINNER: {}'.format('White')
            elif self.get_black_count(board) == self.get_white_count(board):
                self.state = 'NONE'
                return 'WINNER: {}'.format('NONE')
        if game_rule == '<':
            if self.get_black_count(board) < self.get_white_count(board):
                self.state = 'WIN'
                return 'WINNER: {}'.format('Black')
            elif self.get_white_count(board) < self.get_black_count(board):
                self.state = 'WIN'
                return 'WINNER: {}'.format('White')
            elif self.get_black_count(board) == self.get_white_count(board):
                self.state = 'NONE'
                return 'WINNER: {}'.format('NONE')


class Turn:
    """ class that controls the attributes of the turn """
    def __init__(self, turn_count: str):
        # odd is equal to what user specified
        self.player1 = turn_count
        self.count = 0
        self.black_no_move = False
        self.white_no_move = False

        if self.player1 == 'Black':
            self.player2 = 'White'
        elif self.player1 == 'White':
            self.player2 = 'Black'

    def get_turn(self):  # returns turn
        if self.count % 2 == 0:
            return self.player1

        elif self.count % 2 != 0:
            return self.player2

    def increment(self):  # changes player side
        self.count += 1

    def make_move(self, game, board: list, move_row: int, move_col: int):
        if self.get_turn() == 'Black':
            board[move_row - 1][move_col - 1] = 'Black'
        elif self.get_turn() == 'White':
            board[move_row - 1][move_col - 1] = 'White'

    def set_no_move(self, player):
        if player == 'Black':
            self.black_no_move = True
        elif player == 'White':
            self.white_no_move = True

    def set_move(self, player):
        if player == 'Black':
            self.black_no_move = False
        elif player == 'White':
            self.white_no_move = False


class North:
    """ Flips colors in North direction """
    def check_move(self, game, turn, board: list, move_row: int, move_col: int) -> bool:
        self.valid = False
        valid = False

        if turn.get_turn() == 'Black':
            player_1 = 'Black'
            player_2 = 'White'
        elif turn.get_turn() == 'White':
            player_1 = 'White'
            player_2 = 'Black'

        if turn.get_turn() == player_1:
            i = 0
            while move_row-2-i >= 0:
                if board[move_row-2-i][move_col-1] == player_2:
                    i += 1
                elif board[move_row-2-i][move_col-1] == player_1:
                    valid = True
                    break
                else:
                    return False
            if valid:
                j = 0
                while move_row-2-j >= 0:
                    if board[move_row-2-j][move_col-1] == player_2:
                        board[move_row - 2 - j][move_col-1] = player_1
                        j += 1
                    elif board[move_row-2-j][move_col-1] == player_1:
                        break

                self.valid = True

            return self.valid


class South:
    """ Flips colors in South direction """
    def check_move(self, game, turn, board: list, move_row: int, move_col: int) -> bool:
        self.valid = False
        valid = False

        if turn.get_turn() == 'Black':
            player_1 = 'Black'
            player_2 = 'White'
        elif turn.get_turn() == 'White':
            player_1 = 'White'
            player_2 = 'Black'

        if turn.get_turn() == player_1:
            i = 0
            while move_row + i <= game.row-1:
                if board[move_row+i][move_col-1] == player_2:
                    i += 1
                elif board[move_row+i][move_col-1] == player_1:
                    valid = True
                    break
                else:
                    return False

            if valid:
                j = 0
                while move_row+j <= game.row-1:
                    if board[move_row+j][move_col-1] == player_2:
                        board[move_row+j][move_col-1] = player_1
                        j += 1
                    elif board[move_row+j][move_col-1] == player_1:
                        break

                self.valid = True

            return self.valid


class West:
    """ Flips colors in West direction """
    def check_move(self, game, turn, board, move_row, move_col) -> bool:
        self.valid = False
        valid = False

        if turn.get_turn() == 'Black':
            player_1 = 'Black'
            player_2 = 'White'
        elif turn.get_turn() == 'White':
            player_1 = 'White'
            player_2 = 'Black'

        if turn.get_turn() == player_1:
            i = 0
            while move_col-2-i >= 0:
                if board[move_row-1][move_col-2-i] == player_2:
                    i += 1
                elif board[move_row-1][move_col-2-i] == player_1:
                    valid = True
                    break
                else:
                    return False

            if valid:
                j = 0
                while move_col-2-j >= 0:
                    if board[move_row-1][move_col-2-j] == player_2:
                        board[move_row-1][move_col-2-j] = player_1
                        j += 1
                    elif board[move_row-1][move_col-2-j] == player_1:
                        break

                self.valid = True

            return self.valid


class East:
    """ Flips colors in the East direction """
    def check_move(self, game, turn, board, move_row, move_col) -> bool:
        self.valid = False
        valid = False

        if turn.get_turn() == 'Black':
            player_1 = 'Black'
            player_2 = 'White'
        elif turn.get_turn() == 'White':
            player_1 = 'White'
            player_2 = 'Black'

        if turn.get_turn() == player_1:
            i = 0
            while move_col+i <= game.col-1:
                if board[move_row-1][move_col+i] == player_2:
                    i += 1
                elif board[move_row-1][move_col+i] == player_1:
                    valid = True
                    break
                else:
                    return False

            if valid:
                j = 0
                while move_col+i <= game.col-1:
                    if board[move_row-1][move_col+j] == player_2:
                        board[move_row-1][move_col+j] = player_1
                        j += 1
                    elif board[move_row-1][move_col+j] == player_1:
                        break

                self.valid = True

            return self.valid


class NorthWest:
    """ Flips colors in the North West Direction """
    def check_move(self, game, turn, board, move_row, move_col) -> bool:
        self.valid = False
        valid = False

        if turn.get_turn() == 'Black':
            player_1 = 'Black'
            player_2 = 'White'
        elif turn.get_turn() == 'White':
            player_1 = 'White'
            player_2 = 'Black'

        if turn.get_turn() == player_1:
            i = 0
            while move_row-2-i >= 0 and move_col-2-i >= 0:
                if board[move_row-2-i][move_col-2-i] == player_2:
                    i += 1
                elif board[move_row-2-i][move_col-2-i] == player_1:
                    valid = True
                    break
                else:
                    return False

            if valid:
                j = 0
                while move_row-2-j >= 0 and move_col-2-j >= 0:
                    if board[move_row-2-j][move_col-2-j] == player_2:
                        board[move_row - 2 - j][move_col - 2 - j] = player_1
                        j += 1
                    elif board[move_row-2-j][move_col-2-j] == player_1:
                        break

                    self.valid = True

            return self.valid


class NorthEast:
    """ Flips colors in the North East direction """
    def check_move(self, game, turn, board, move_row, move_col) -> bool:
        self.valid = False
        valid = False

        if turn.get_turn() == 'Black':
            player_1 = 'Black'
            player_2 = 'White'
        elif turn.get_turn() == 'White':
            player_1 = 'White'
            player_2 = 'Black'

        if turn.get_turn() == player_1:
            i = 0
            while move_row-2-i >= 0 and move_col+i <= game.col-1:
                if board[move_row-2-i][move_col+i] == player_2:
                    i += 1
                elif board[move_row-2-i][move_col+i] == player_1:
                    valid = True
                    break
                else:
                    return False

            if valid:
                j = 0
                while move_row - 2 - j >= 0 and move_col + j <= game.col - 1:
                    if board[move_row-2-j][move_col+j] == player_2:
                        board[move_row - 2 - j][move_col + j] = player_1
                        j += 1
                    elif board[move_row-2-j][move_col+j] == player_1:
                        break

                    self.valid = True

            return self.valid


class SouthWest:
    """ Flips colors in the South West Direction """
    def check_move(self, game, turn, board, move_row, move_col) -> bool:
        self.valid = False
        valid = False

        if turn.get_turn() == 'Black':
            player_1 = 'Black'
            player_2 = 'White'
        elif turn.get_turn() == 'White':
            player_1 = 'White'
            player_2 = 'Black'

        if turn.get_turn() == player_1:
            i = 0
            while move_row+i <= game.row-1 and move_col-2-i >= 0:
                if board[move_row+i][move_col-2-i] == player_2:
                    i += 1
                elif board[move_row+i][move_col-2-i] == player_1:
                    valid = True
                    break
                else:
                    return False

            if valid:
                j = 0
                while move_row + j <= game.row-1 and move_col - 2 - j >= 0:
                    if board[move_row+j][move_col-2-j] == player_2:
                        board[move_row+j][move_col-2-j] = player_1
                        j += 1
                    elif board[move_row+j][move_col-2-j] == player_1:
                        break

                    self.valid = True

            return self.valid


class SouthEast:
    """ Flips colors in the South East direction """
    def check_move(self, game, turn, board, move_row, move_col) -> bool:
        self.valid = False
        valid = False

        if turn.get_turn() == 'Black':
            player_1 = 'Black'
            player_2 = 'White'
        elif turn.get_turn() == 'White':
            player_1 = 'White'
            player_2 = 'Black'

        if turn.get_turn() == player_1:
            i = 0
            while move_row+i <= game.row-1 and move_col+i <= game.col-1:
                if board[move_row+i][move_col+i] == player_2:
                    i += 1
                elif board[move_row+i][move_col+i] == player_1:
                    valid = True
                    break
                else:
                    return False

            if valid:
                j = 0
                while move_row + j <= game.row - 1 and move_col + j <= game.col - 1:
                    if board[move_row+j][move_col+j] == player_2:
                        board[move_row+j][move_col+j] = player_1
                        j += 1
                    elif board[move_row+j][move_col+j] == player_1:
                        break

                    self.valid = True

            return self.valid

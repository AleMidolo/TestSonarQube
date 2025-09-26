class GomokuGame:
    EMPTY_SPACE = ' '
    WINNING_COUNT = 5
    PLAYER_X = 'X'
    PLAYER_O = 'O'

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self._initialize_board(board_size)
        self.current_player = self.PLAYER_X

    def _initialize_board(self, size):
        return [[self.EMPTY_SPACE for _ in range(size)] for _ in range(size)]

    def make_move(self, row, col):
        if self._is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self._switch_player()
            return True
        return False

    def _is_valid_move(self, row, col):
        return self.board[row][col] == self.EMPTY_SPACE

    def _switch_player(self):
        self.current_player = self.PLAYER_O if self.current_player == self.PLAYER_X else self.PLAYER_X

    def check_winner(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != self.EMPTY_SPACE:
                    winner = self._check_winner_from_position(row, col)
                    if winner:
                        return winner
        return None

    def _check_winner_from_position(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for direction in directions:
            if self._check_five_in_a_row(row, col, direction):
                return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        dx, dy = direction
        count = 1
        symbol = self.board[row][col]
        for i in range(1, self.WINNING_COUNT):
            new_row = row + dx * i
            new_col = col + dy * i
            if not self._is_within_bounds(new_row, new_col) or self.board[new_row][new_col] != symbol:
                return False
            count += 1
        return count == self.WINNING_COUNT

    def _is_within_bounds(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size
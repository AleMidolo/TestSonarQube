class GomokuGame:
    EMPTY_CELL = ' '
    WINNING_COUNT = 5
    PLAYER_X = 'X'
    PLAYER_O = 'O'

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self._initialize_board()
        self.current_player = self.PLAYER_X

    def _initialize_board(self):
        return [[self.EMPTY_CELL for _ in range(self.board_size)] for _ in range(self.board_size)]

    def make_move(self, row, col):
        if self._is_cell_empty(row, col):
            self._place_symbol(row, col)
            self._switch_player()
            return True
        return False

    def _is_cell_empty(self, row, col):
        return self.board[row][col] == self.EMPTY_CELL

    def _place_symbol(self, row, col):
        self.board[row][col] = self.current_player

    def _switch_player(self):
        self.current_player = self.PLAYER_O if self.current_player == self.PLAYER_X else self.PLAYER_X

    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self._is_cell_not_empty(row, col):
                    for direction in directions:
                        if self._check_five_in_a_row(row, col, direction):
                            return self.board[row][col]
        return None

    def _is_cell_not_empty(self, row, col):
        return self.board[row][col] != self.EMPTY_CELL

    def _check_five_in_a_row(self, row, col, direction):
        dx, dy = direction
        count = 1
        symbol = self.board[row][col]
        for i in range(1, self.WINNING_COUNT):
            new_row = row + dx * i
            new_col = col + dy * i
            if not self._is_within_bounds(new_row, new_col):
                return False
            if self.board[new_row][new_col] != symbol:
                return False
            count += 1
        return count == self.WINNING_COUNT

    def _is_within_bounds(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size
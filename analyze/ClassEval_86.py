class TicTacToe:
    EMPTY_CELL = ' '
    SIZE = 3

    def __init__(self, N=SIZE):
        self.board = self.create_board(N)
        self.current_player = 'X'

    def create_board(self, N):
        return [[self.EMPTY_CELL for _ in range(N)] for _ in range(N)]

    def make_move(self, row, col):
        if self.is_cell_empty(row, col):
            self.place_move(row, col)
            self.switch_player()
            return True
        return False

    def is_cell_empty(self, row, col):
        return self.board[row][col] == self.EMPTY_CELL

    def place_move(self, row, col):
        self.board[row][col] = self.current_player

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winner = self.check_rows() or self.check_columns() or self.check_diagonals()
        return winner

    def check_rows(self):
        for row in self.board:
            if self.is_winning_combination(row):
                return row[0]
        return None

    def check_columns(self):
        for col in range(self.SIZE):
            column = [self.board[row][col] for row in range(self.SIZE)]
            if self.is_winning_combination(column):
                return column[0]
        return None

    def check_diagonals(self):
        if self.is_winning_combination([self.board[i][i] for i in range(self.SIZE)]):
            return self.board[0][0]
        if self.is_winning_combination([self.board[i][self.SIZE - 1 - i] for i in range(self.SIZE)]):
            return self.board[0][self.SIZE - 1]
        return None

    def is_winning_combination(self, combination):
        return combination[0] == combination[1] == combination[2] != self.EMPTY_CELL

    def is_board_full(self):
        return all(cell != self.EMPTY_CELL for row in self.board for cell in row)
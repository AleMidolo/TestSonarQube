class TicTacToe:
    def __init__(self, N=3):
        self.N = N
        self.board = self.create_board()
        self.current_player = 'X'

    def create_board(self):
        return [[' ' for _ in range(self.N)] for _ in range(self.N)]

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.switch_player()
            return True
        return False

    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winner = self.check_rows() or self.check_columns() or self.check_diagonals()
        return winner

    def check_rows(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        return None

    def check_columns(self):
        for col in range(self.N):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        return None

    def check_diagonals(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_board_full(self):
        return all(' ' not in row for row in self.board)
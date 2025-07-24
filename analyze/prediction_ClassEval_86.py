class TicTacToe:
    def __init__(self, N=3):
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.is_cell_empty(row, col):
            self.place_marker(row, col)
            self.switch_player()
            return True
        return False

    def is_cell_empty(self, row, col):
        return self.board[row][col] == ' '

    def place_marker(self, row, col):
        self.board[row][col] = self.current_player

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winner = self.check_rows()
        if winner:
            return winner
        winner = self.check_columns()
        if winner:
            return winner
        winner = self.check_diagonals()
        return winner

    def check_rows(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        return None

    def check_columns(self):
        for col in range(len(self.board)):
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
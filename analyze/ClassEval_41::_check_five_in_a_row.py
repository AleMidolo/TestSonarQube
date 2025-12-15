class GomokuGame: 
    def __init__(self, board_size):
        """
        Initializes the game with a given board size.
        It initializes the board with empty spaces and sets the current player symble as 'X'.
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'


    def make_move(self, row, col):
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and changes the current player to the other player (if the current player is 'X', then it becomes 'O' and vice versa).
        :param row: int, the row index of this move
        :param col: int, the column index
        return: True if the move is valid, or False otherwise.
        >>> gomokuGame = GomokuGame(10)
        >>> gomokuGame.make_move(5, 5)
        True
        >>> gomokuGame.make_move(5, 5)
        False
        """
    
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False
    
    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame.check_winner()
        'X'
        """
    
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    for direction in directions:
                        if self._check_five_in_a_row(row, col, direction):
                            return self.board[row][col]
        return None
    

    def _check_five_in_a_row(self, row, col, direction):
        """
        controlla se ci sono cinque simboli consecutivi dello stesso giocatore in una riga a partire da una cella data in una direzione data (orizzontale, verticale, diagonale).
        Conta il numero di simboli consecutivi in quella direzione a partire dalla cella data,
        :param row: int, riga della cella data
        :param col: int, colonna della cella data
        :param direction: tuple, (int, int), denominato come (dx, dy). La riga e la colonna verranno aumentate di diversi dx e dy rispettivamente.
        :return: True se ci sono cinque simboli consecutivi dello stesso giocatore, e False altrimenti.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame._check_five_in_a_row(5, 1, (0, 1))
        True
        >>> gomokuGame._check_five_in_a_row(5, 1, (1, 1))
        False
        """
        count = 0
        dx, dy = direction
        player_symbol = self.board[row][col]

        for step in range(5):
            new_row = row + step * dx
            new_col = col + step * dy
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                if self.board[new_row][new_col] == player_symbol:
                    count += 1
                else:
                    break
            else:
                break

        return count == 5
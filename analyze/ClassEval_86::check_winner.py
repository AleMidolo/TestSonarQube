def check_winner(self):
    """
        Controlla se c'è un vincitore sulla tavola in righe, colonne e diagonali in tre direzioni
        :return: str o None, il segno del vincitore ('X' o 'O'), o None se non c'è ancora un vincitore
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
        ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
        """
    for row in self.board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
            return self.board[0][col]
    if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
        return self.board[0][0]
    if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
        return self.board[0][2]
    return None
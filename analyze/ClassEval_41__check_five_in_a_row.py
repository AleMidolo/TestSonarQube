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
    # Get the symbol at the starting position
    if not (0 <= row < len(self.board) and 0 <= col < len(self.board[0])):
        return False
    
    symbol = self.board[row][col]
    
    # If the cell is empty, there can't be five in a row
    if symbol is None or symbol == ' ' or symbol == '':
        return False
    
    dx, dy = direction
    count = 1  # Count the starting cell
    
    # Check in the positive direction
    r, c = row + dx, col + dy
    while (0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and 
           self.board[r][c] == symbol):
        count += 1
        r += dx
        c += dy
    
    # Check in the negative direction
    r, c = row - dx, col - dy
    while (0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and 
           self.board[r][c] == symbol):
        count += 1
        r -= dx
        c -= dy
    
    return count >= 5
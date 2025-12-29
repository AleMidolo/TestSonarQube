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
    dx, dy = direction
    count = 0
    player_symbol = self.board[row][col]
    for i in range(5):
        new_row = row + i * dx
        new_col = col + i * dy
        if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
            if self.board[new_row][new_col] == player_symbol:
                count += 1
            else:
                break
        else:
            break
    return count == 5
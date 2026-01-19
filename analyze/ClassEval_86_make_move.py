def make_move(self, row, col):
    """
        Posiziona il segno del giocatore corrente nella posizione specificata sulla tavola e cambia il segno.
        :param row: int, l'indice di riga della posizione
        :param col: int, l'indice di colonna della posizione
        :return: bool, che indica se la mossa è stata effettuata con successo o meno
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """
    if row < 0 or row >= 3 or col < 0 or (col >= 3):
        return False
    if self.board[row][col] != ' ':
        return False
    self.board[row][col] = self.current_player
    self.current_player = 'O' if self.current_player == 'X' else 'X'
    return True
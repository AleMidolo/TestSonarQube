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
    # Verifica se la posizione è valida e vuota
    if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
        if self.board[row][col] == ' ' or self.board[row][col] == '':
            # Posiziona il segno del giocatore corrente
            self.board[row][col] = self.current_player
            # Cambia il giocatore corrente
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
    return False
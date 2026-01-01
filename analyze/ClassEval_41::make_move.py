def make_move(self, row, col):
    """
        Effettua una mossa nella riga e colonna dati.
        Se la mossa è valida, posiziona il simbolo del giocatore corrente sulla scacchiera
        e cambia il giocatore corrente con l'altro giocatore (se il giocatore corrente è 'X', diventa 'O' e viceversa).
        :param row: int, l'indice della riga di questa mossa
        :param col: int, l'indice della colonna
        return: True se la mossa è valida, altrimenti False.
        >>> gomokuGame = GomokuGame(10)
        >>> gomokuGame.make_move(5, 5)
        True
        >>> gomokuGame.make_move(5, 5)
        False
        """
    if 0 <= row < self.board_size and 0 <= col < self.board_size and (self.board[row][col] == ' '):
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True
    return False
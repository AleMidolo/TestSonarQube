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
    # Verifica se la mossa è valida (dentro i limiti della scacchiera e cella vuota)
    if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
        return False
    
    if self.board[row][col] != ' ':
        return False
    
    # Posiziona il simbolo del giocatore corrente
    self.board[row][col] = self.current_player
    
    # Cambia il giocatore corrente
    if self.current_player == 'X':
        self.current_player = 'O'
    else:
        self.current_player = 'X'
    
    return True
def make_move(self, row, col):
    """
    Realiza un movimiento en la fila y columna dadas.
    Si el movimiento es válido, coloca el símbolo del jugador actual en el tablero
    y cambia el jugador actual al otro jugador (si el jugador actual es 'X', entonces se convierte en 'O' y viceversa).
    :param row: int, el índice de fila de este movimiento
    :param col: int, el índice de columna
    return: True si el movimiento es válido, o False en caso contrario.
    >>> gomokuGame = GomokuGame(10)
    >>> gomokuGame.make_move(5, 5)
    True
    >>> gomokuGame.make_move(5, 5)
    False
    """
    # Verificar si el movimiento está dentro de los límites del tablero
    if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
        return False
    
    # Verificar si la posición está vacía
    if self.board[row][col] != ' ':
        return False
    
    # Realizar el movimiento
    self.board[row][col] = self.current_player
    
    # Cambiar al otro jugador
    if self.current_player == 'X':
        self.current_player = 'O'
    else:
        self.current_player = 'X'
    
    return True
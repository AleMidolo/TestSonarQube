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
    if self.board[row][col] == ' ':
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True
    return False
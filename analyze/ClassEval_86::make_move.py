def make_move(self, row, col):
    """
        Coloca la marca del jugador actual en la posición especificada en el tablero y cambia la marca.
        :param row: int, el índice de fila de la posición
        :param col: int, el índice de columna de la posición
        :return: bool, indicando si el movimiento fue exitoso o no
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """
    if self.board[row][col] == ' ':
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True
    return False
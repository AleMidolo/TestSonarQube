def is_board_full(self):
    """
    Verifica si el tablero de juego está completamente lleno.
    :return: bool, indicando si el tablero de juego está lleno o no
    >>> ttt.is_board_full()
    False
    """
    for row in self.board:
        for cell in row:
            if cell == ' ' or cell == '':
                return False
    return True
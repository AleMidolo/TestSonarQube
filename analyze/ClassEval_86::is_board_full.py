def is_board_full(self):
    """
        Verifica si el tablero de juego está completamente lleno.
        :return: bool, indicando si el tablero de juego está lleno o no
        >>> ttt.is_board_full()
        False
        """
    for row in self.board:
        if ' ' in row:
            return False
    return True
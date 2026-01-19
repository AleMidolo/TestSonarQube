def is_board_full(self):
    """
        Verifica si el tablero de juego está completamente lleno.
        :return: bool, indicando si el tablero de juego está lleno o no
        >>> ttt.is_board_full()
        False
        """
    return all((cell != ' ' for row in self.board for cell in row))
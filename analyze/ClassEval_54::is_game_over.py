def is_game_over(self):
    """
        Verifica si el juego ha terminado (es decir, si no hay más íconos en el tablero de juego)
        :return: True o False, representando si el juego ha terminado
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True
        """
    for row in self.board:
        if any((icon != ' ' for icon in row)):
            return False
    return True
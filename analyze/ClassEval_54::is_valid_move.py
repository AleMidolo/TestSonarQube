def is_valid_move(self, pos1, pos2):
    """
        verifica si el movimiento de dos íconos es válido (es decir, las posiciones están dentro del rango del tablero de juego, las dos posiciones no son las mismas, las dos posiciones tienen el mismo ícono y hay un camino válido entre las dos posiciones)
        :param pos1: tupla de posición (x, y) del primer ícono
        :param pos2: tupla de posición (x, y) del segundo ícono
        :return: True o False, representando si el movimiento de los dos íconos es válido
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
    x1, y1 = pos1
    x2, y2 = pos2
    if not (0 <= x1 < self.BOARD_SIZE[0] and 0 <= y1 < self.BOARD_SIZE[1] and (0 <= x2 < self.BOARD_SIZE[0]) and (0 <= y2 < self.BOARD_SIZE[1])):
        return False
    if pos1 == pos2:
        return False
    if self.board[x1][y1] == ' ' or self.board[x2][y2] == ' ':
        return False
    if self.board[x1][y1] != self.board[x2][y2]:
        return False
    return self.has_path(pos1, pos2)
def _check_five_in_a_row(self, row, col, direction):
    """
        verifica si hay cinco símbolos consecutivos del mismo jugador en una fila comenzando desde una celda dada en una dirección dada (horizontal, vertical, diagonal).
        Cuenta el número de símbolos consecutivos en esa dirección comenzando desde la celda dada,
        :param row: int, fila de la celda dada
        :param col: int, columna de la celda dada
        :param direction: tuple, (int, int), nombrado como (dx, dy). La fila y la columna se incrementarán en varios dx y dy respectivamente.
        :return: True si hay cinco símbolos consecutivos del mismo jugador, y False en caso contrario.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame._check_five_in_a_row(5, 1, (0, 1))
        True
        >>> gomokuGame._check_five_in_a_row(5, 1, (1, 1))
        False
        """
    dx, dy = direction
    player = self.board[row][col]
    count = 1
    r, c = (row + dx, col + dy)
    while 0 <= r < self.board_size and 0 <= c < self.board_size and (self.board[r][c] == player):
        count += 1
        r += dx
        c += dy
    r, c = (row - dx, col - dy)
    while 0 <= r < self.board_size and 0 <= c < self.board_size and (self.board[r][c] == player):
        count += 1
        r -= dx
        c -= dy
    return count >= 5
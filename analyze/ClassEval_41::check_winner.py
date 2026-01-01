def check_winner(self):
    """
        Verifica si hay un ganador buscando cinco en fila en todas las direcciones (horizontal, vertical, diagonal).
        return: el símbolo del jugador ganador (ya sea 'X' o 'O') si hay un ganador, o None en caso contrario.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame.check_winner()
        'X'
        """
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for row in range(self.board_size):
        for col in range(self.board_size):
            if self.board[row][col] != ' ':
                for direction in directions:
                    if self._check_five_in_a_row(row, col, direction):
                        return self.board[row][col]
    return None
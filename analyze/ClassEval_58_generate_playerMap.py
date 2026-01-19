def generate_playerMap(self):
    """
    Genera un mapa de jugador con el tamaño dado del tablero, el parámetro n es el tamaño del tablero, el tamaño del tablero es n*n, el parámetro k es el número de minas, '-' representa la posición desconocida.
    :return: El mapa del jugador, lista.
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.generate_playerMap()
    [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    """
    return [['-' for _ in range(self.n)] for _ in range(self.n)]
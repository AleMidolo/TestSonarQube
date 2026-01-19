def generate_playerMap(self):
    """
    Genera una mappa del giocatore con la dimensione data del tabellone, il parametro n è la dimensione del tabellone, la dimensione del tabellone è n*n, il parametro k è il numero di mine, '-' rappresenta la posizione sconosciuta.
    :return: La mappa del giocatore, lista.
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.generate_playerMap()
    [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    """
    return [['-' for _ in range(self.n)] for _ in range(self.n)]
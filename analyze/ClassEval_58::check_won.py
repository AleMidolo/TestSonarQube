def check_won(self, map):
    """
        Controlla se il giocatore ha vinto il gioco; se ci sono solo mine nella mappa del giocatore, restituisce True, altrimenti restituisce False.
        :return: True se il giocatore ha vinto il gioco, False altrimenti.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.check_won(minesweeper_game.player_map)
        False
        """
    total_cells = self.n * self.n
    revealed_cells = sum((row.count('-') for row in map))
    return revealed_cells == self.k
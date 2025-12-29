def sweep(self, x, y):
    """
        Scopre la posizione data.
        :param x: La coordinata x della posizione, int.
        :param y: La coordinata y della posizione, int.
        :return: True se il giocatore ha vinto il gioco, False altrimenti; se il gioco continua, restituisce la mappa del giocatore, list.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.sweep(1, 1)
        [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]

        """
    if self.minesweeper_map[y][x] == 'X':
        return False
    else:
        self.player_map[y][x] = self.minesweeper_map[y][x]
        if self.check_won(self.player_map):
            return True
        return self.player_map
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
    for row in range(self.n):
        for col in range(self.n):
            if self.player_map[row][col] == '-' and self.minesweeper_map[row][col] != 'X':
                return False
    return True
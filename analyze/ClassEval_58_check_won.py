def check_won(self, map):
    """
        Verifica si el jugador ha ganado el juego. Si solo hay minas en el mapa del jugador, devuelve True, de lo contrario devuelve False.
        :return: True si el jugador ha ganado el juego, False en caso contrario.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.check_won(minesweeper_game.player_map)
        False
        """
    for i in range(self.n):
        for j in range(self.n):
            if map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                return False
    return True
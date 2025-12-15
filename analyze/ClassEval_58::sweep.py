def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.sweep(1, 1)
        [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]
        """
        if self.minesweeper_map[y][x] == 'X':
            return False  # Game over, hit a mine
        
        self.player_map[y][x] = self.minesweeper_map[y][x]
        
        if self.check_won(self.player_map):
            return True  # Player has won
        
        return self.player_map  # Game continues
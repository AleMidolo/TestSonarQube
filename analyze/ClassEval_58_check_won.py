def check_won(self, map):
    """
        Checks if the player has won the game, returns True if the player's map contains only mines, otherwise returns False.
        :return: True if the player has won the game, otherwise False.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.check_won(minesweeper_game.player_map)
        False

        """
    for row in range(self.n):
        for col in range(self.n):
            if self.player_map[row][col] != 'X' and self.minesweeper_map[row][col] != 'X':
                return False
    return True
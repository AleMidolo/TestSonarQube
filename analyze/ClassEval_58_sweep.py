def sweep(self, x, y):
    """
        दिए गए स्थान को स्वीप करता है।
        :param x: स्थान का x समन्वय, int.
        :param y: स्थान का y समन्वय, int.
        :return: यदि खिलाड़ी ने खेल जीत लिया है तो True, अन्यथा False, यदि खेल अभी भी जारी है, तो खिलाड़ी का मानचित्र लौटाएं, list.
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
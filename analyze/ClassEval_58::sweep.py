def sweep(self, x, y):
    """
        扫描给定的位置。
        :param x: 位置的 x 坐标，int。
        :param y: 位置的 y 坐标，int。
        :return: 如果玩家赢得了游戏则返回 True，其他情况返回 False，如果游戏仍在继续，返回玩家地图，list。
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
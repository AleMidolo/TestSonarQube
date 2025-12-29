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
    if x < 0 or x >= self.n or y < 0 or (y >= self.n):
        return self.player_map
    if self.player_map[y][x] != '-':
        return self.player_map
    if self.minesweeper_map[y][x] == 'X':
        for i in range(self.n):
            for j in range(self.n):
                if self.minesweeper_map[i][j] == 'X':
                    self.player_map[i][j] = 'X'
        return False
    self.player_map[y][x] = self.minesweeper_map[y][x]
    if self.minesweeper_map[y][x] == 0:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            new_x, new_y = (x + dx, y + dy)
            if 0 <= new_x < self.n and 0 <= new_y < self.n:
                if self.player_map[new_y][new_x] == '-':
                    self.sweep(new_x, new_y)
    if self.check_won(self.player_map):
        return True
    return self.player_map
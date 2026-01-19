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
    # Check if the position is already revealed
    if self.player_map[x][y] != '-':
        return self.player_map
    
    # Check if hit a mine
    if self.minesweeper_map[x][y] == 'X':
        return False
    
    # Reveal the cell
    self.player_map[x][y] = self.minesweeper_map[x][y]
    
    # If the cell is 0, recursively reveal adjacent cells
    if self.minesweeper_map[x][y] == 0:
        # Check all 8 adjacent cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                # Check bounds
                if 0 <= nx < len(self.minesweeper_map) and 0 <= ny < len(self.minesweeper_map[0]):
                    if self.player_map[nx][ny] == '-':
                        self.sweep(nx, ny)
    
    # Check if player won (all non-mine cells revealed)
    for i in range(len(self.minesweeper_map)):
        for j in range(len(self.minesweeper_map[0])):
            if self.minesweeper_map[i][j] != 'X' and self.player_map[i][j] == '-':
                return self.player_map
    
    return True
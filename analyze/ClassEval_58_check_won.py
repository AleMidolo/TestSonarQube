def check_won(self, map):
    """
        检查玩家是否赢得了游戏，如果玩家地图上只有地雷，则返回 True，否则返回 False。
        :return: 如果玩家赢得了游戏，则返回 True，否则返回 False。
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
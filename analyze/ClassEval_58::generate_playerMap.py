def generate_playerMap(self):
    """
        生成一个玩家地图，给定的参数 n 是棋盘的大小，棋盘的大小为 n*n，参数 k 是地雷的数量，'-' 表示未知位置。
        :return: 玩家地图，列表。
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_playerMap()
        [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        """
    return [['-' for _ in range(self.n)] for _ in range(self.n)]
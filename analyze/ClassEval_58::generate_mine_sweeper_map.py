def generate_mine_sweeper_map(self):
    """
        生成一个扫雷地图，给定棋盘的大小和地雷的数量，参数 n 是棋盘的大小，棋盘的大小为 n*n，参数 k 是地雷的数量，'X' 代表地雷，其他数字代表该位置周围的地雷数量。
        :return: 扫雷地图，列表。
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_mine_sweeper_map()
        [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

        """
    board = [[0 for _ in range(self.n)] for _ in range(self.n)]
    mines_placed = 0
    while mines_placed < self.k:
        x = random.randint(0, self.n - 1)
        y = random.randint(0, self.n - 1)
        if board[x][y] != 'X':
            board[x][y] = 'X'
            mines_placed += 1
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < self.n and 0 <= ny < self.n and (board[nx][ny] != 'X'):
                        board[nx][ny] += 1
    return board
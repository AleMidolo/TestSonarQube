def generate_mine_sweeper_map(self):
        """
        生成一个扫雷地图，给定棋盘的大小和地雷的数量，参数 n 是棋盘的大小，棋盘的大小为 n*n，参数 k 是地雷的数量，'X' 代表地雷，其他数字代表该位置周围的地雷数量。
        :return: 扫雷地图，列表。
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_mine_sweeper_map()
        [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

        """
        # Initialize the minesweeper map with zeros
        minesweeper_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        # Place mines randomly
        mines_placed = 0
        while mines_placed < self.k:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            if minesweeper_map[x][y] != 'X':  # Check if mine is already placed
                minesweeper_map[x][y] = 'X'
                mines_placed += 1
                
                # Update the surrounding numbers
                for i in range(max(0, x - 1), min(self.n, x + 2)):
                    for j in range(max(0, y - 1), min(self.n, y + 2)):
                        if minesweeper_map[i][j] != 'X':
                            minesweeper_map[i][j] += 1
        
        return minesweeper_map
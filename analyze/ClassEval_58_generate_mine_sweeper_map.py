import random

def generate_mine_sweeper_map(self):
    """
    生成一个扫雷地图，给定棋盘的大小和地雷的数量，参数 n 是棋盘的大小，棋盘的大小为 n*n，参数 k 是地雷的数量，'X' 代表地雷，其他数字代表该位置周围的地雷数量。
    :return: 扫雷地图，列表。
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.generate_mine_sweeper_map()
    [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

    """
    # 初始化 n*n 的棋盘，全部设为 0
    board = [[0 for _ in range(self.n)] for _ in range(self.n)]
    
    # 随机放置 k 个地雷
    positions = [(i, j) for i in range(self.n) for j in range(self.n)]
    mine_positions = random.sample(positions, self.k)
    
    # 在棋盘上标记地雷
    for row, col in mine_positions:
        board[row][col] = 'X'
    
    # 计算每个非地雷位置周围的地雷数量
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(self.n):
        for j in range(self.n):
            if board[i][j] != 'X':
                mine_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.n and 0 <= nj < self.n and board[ni][nj] == 'X':
                        mine_count += 1
                board[i][j] = mine_count
    
    return board
import random

def create_board(self):
    """
    创建具有给定大小和图标的游戏棋盘
    :return: 二维列表，游戏棋盘
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    >>> mc.create_board()
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    """
    rows, cols = self.size[0], self.size[1]
    total_cells = rows * cols
    
    # 确保总单元格数是偶数（麻将连连看需要成对）
    if total_cells % 2 != 0:
        raise ValueError("Board size must have an even number of cells")
    
    # 计算每个图标需要的数量
    pairs_needed = total_cells // 2
    icons_count = len(self.icons)
    
    # 创建图标列表，确保每个图标出现偶数次
    tiles = []
    for i in range(pairs_needed):
        icon = self.icons[i % icons_count]
        tiles.append(icon)
        tiles.append(icon)
    
    # 打乱图标顺序
    random.shuffle(tiles)
    
    # 创建二维棋盘
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[index])
            index += 1
        board.append(row)
    
    self.board = board
    return board
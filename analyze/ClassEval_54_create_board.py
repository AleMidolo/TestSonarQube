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
    
    # 创建图标列表，每个图标出现偶数次
    icons_list = []
    pairs_needed = total_cells // 2
    
    # 循环使用图标直到填满棋盘
    icon_index = 0
    for _ in range(pairs_needed):
        icons_list.append(self.icons[icon_index % len(self.icons)])
        icons_list.append(self.icons[icon_index % len(self.icons)])
        icon_index += 1
    
    # 打乱图标列表
    random.shuffle(icons_list)
    
    # 创建二维棋盘
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icons_list[i * cols + j])
        board.append(row)
    
    self.board = board
    return board
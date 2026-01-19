def create_board(self):
    """
    创建具有给定大小和图标的游戏棋盘
    :return: 二维列表,游戏棋盘
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    >>> mc.create_board()
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    """
    import random
    
    rows, cols = self.size[0], self.size[1]
    total_cells = rows * cols
    
    # 确保总格子数是偶数(麻将连连看需要成对)
    if total_cells % 2 != 0:
        raise ValueError("Board size must have even number of cells")
    
    # 创建图标列表,每个图标出现偶数次
    icons_needed = total_cells // 2
    board_icons = []
    
    # 循环使用图标列表填充棋盘
    icon_index = 0
    for _ in range(icons_needed):
        board_icons.append(self.icons[icon_index % len(self.icons)])
        board_icons.append(self.icons[icon_index % len(self.icons)])
        icon_index += 1
    
    # 打乱图标顺序
    random.shuffle(board_icons)
    
    # 将一维列表转换为二维棋盘
    self.board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(board_icons[i * cols + j])
        self.board.append(row)
    
    return self.board
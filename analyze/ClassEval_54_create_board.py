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
    rows, cols = self.size[0], self.size[1]
    total_cells = rows * cols
    
    # 确保总单元格数是偶数(麻将连连看需要成对)
    if total_cells % 2 != 0:
        raise ValueError("Board size must have even number of cells")
    
    # 计算每个图标需要的数量
    num_pairs = total_cells // 2
    icons_needed = num_pairs // len(self.icons)
    remainder = num_pairs % len(self.icons)
    
    # 创建图标列表(每个图标出现偶数次)
    tiles = []
    for i, icon in enumerate(self.icons):
        count = icons_needed * 2
        if i < remainder:
            count += 2
        tiles.extend([icon] * count)
    
    # 如果tiles不够填满棋盘,循环使用icons
    while len(tiles) < total_cells:
        for icon in self.icons:
            if len(tiles) >= total_cells:
                break
            tiles.extend([icon, icon])
    
    # 截取需要的数量
    tiles = tiles[:total_cells]
    
    # 打乱顺序
    import random
    random.shuffle(tiles)
    
    # 创建二维棋盘
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[i * cols + j])
        board.append(row)
    
    self.board = board
    return board
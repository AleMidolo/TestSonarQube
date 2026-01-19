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
    
    # 计算每个图标需要出现的次数（必须是偶数才能配对）
    num_icons = len(self.icons)
    pairs_needed = total_cells // 2
    
    # 创建图标列表，确保每个图标出现偶数次
    tiles = []
    for i in range(pairs_needed):
        icon = self.icons[i % num_icons]
        tiles.append(icon)
        tiles.append(icon)
    
    # 如果总格子数是奇数，添加一个额外的图标
    if total_cells % 2 == 1:
        tiles.append(self.icons[0])
    
    # 创建棋盘并填充
    board = []
    tile_index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[tile_index])
            tile_index += 1
        board.append(row)
    
    self.board = board
    return board
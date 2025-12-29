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
    rows, cols = self.BOARD_SIZE
    total_cells = rows * cols
    if total_cells % 2 != 0:
        raise ValueError('Board must have an even number of cells')
    icon_pairs = []
    for icon in self.ICONS:
        icon_pairs.extend([icon, icon])
    while len(icon_pairs) < total_cells:
        icon_pairs.extend(icon_pairs[:2])
    icon_pairs = icon_pairs[:total_cells]
    random.shuffle(icon_pairs)
    board = []
    for i in range(rows):
        row = icon_pairs[i * cols:(i + 1) * cols]
        board.append(row)
    return board
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
    icon_pairs = []
    for icon in self.ICONS:
        icon_pairs.extend([icon, icon])
    while len(icon_pairs) < total_cells:
        icon_pairs.append(random.choice(self.ICONS))
    random.shuffle(icon_pairs)
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icon_pairs[i * cols + j])
        board.append(row)
    return board
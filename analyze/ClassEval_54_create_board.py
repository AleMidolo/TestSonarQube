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
    if len(self.ICONS) == 0:
        raise ValueError('ICONS list cannot be empty')
    icon_count = len(self.ICONS)
    pairs_per_icon = total_cells // 2 // icon_count
    remaining_pairs = total_cells // 2 % icon_count
    icon_list = []
    for icon in self.ICONS:
        icon_list.extend([icon] * (pairs_per_icon * 2))
    if remaining_pairs > 0:
        remaining_icons = random.sample(self.ICONS, remaining_pairs)
        for icon in remaining_icons:
            icon_list.extend([icon] * 2)
    if len(icon_list) < total_cells:
        icon_list.append(random.choice(self.ICONS))
        icon_list.append(icon_list[-1])
    random.shuffle(icon_list)
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icon_list[i * cols + j])
        board.append(row)
    return board
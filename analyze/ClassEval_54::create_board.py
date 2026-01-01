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
    icon_counts = {}
    remaining_cells = total_cells
    while remaining_cells > 0:
        for icon in self.ICONS:
            if remaining_cells > 0:
                if icon not in icon_counts:
                    icon_counts[icon] = 0
                icon_counts[icon] += 2
                remaining_cells -= 2
    all_icons = []
    for icon, count in icon_counts.items():
        all_icons.extend([icon] * count)
    all_icons = all_icons[:total_cells]
    if len(all_icons) < total_cells:
        all_icons.append(random.choice(self.ICONS))
    random.shuffle(all_icons)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(all_icons[index])
            index += 1
        board.append(row)
    return board
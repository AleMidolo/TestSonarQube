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
    icon_count = len(self.ICONS)
    pairs_per_icon = total_cells // (icon_count * 2)
    remaining_pairs = total_cells % (icon_count * 2)
    icon_list = []
    for icon in self.ICONS:
        icon_list.extend([icon] * (pairs_per_icon * 2))
    remaining_icons = self.ICONS * 2
    random.shuffle(remaining_icons)
    icon_list.extend(remaining_icons[:remaining_pairs * 2])
    random.shuffle(icon_list)
    board = []
    for i in range(rows):
        row = icon_list[i * cols:(i + 1) * cols]
        board.append(row)
    return board
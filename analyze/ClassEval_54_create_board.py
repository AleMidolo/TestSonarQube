def create_board(self):
    """
        दिए गए बोर्ड आकार और आइकनों के साथ खेल का बोर्ड बनाएं
        :return: 2-आयामी सूची, खेल का बोर्ड
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
        raise ValueError('Board must have even number of cells')
    pairs_needed = total_cells // 2
    if len(self.ICONS) < pairs_needed:
        icon_pool = []
        while len(icon_pool) < total_cells:
            icon_pool.extend(self.ICONS)
        icon_pool = icon_pool[:total_cells]
    else:
        icon_pool = []
        for i in range(pairs_needed):
            icon = self.ICONS[i % len(self.ICONS)]
            icon_pool.extend([icon, icon])
    random.shuffle(icon_pool)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icon_pool[index])
            index += 1
        board.append(row)
    return board
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
    icons_needed = total_cells // len(self.ICONS) * len(self.ICONS)
    if icons_needed < total_cells:
        icons_needed += len(self.ICONS)
    icon_pool = []
    while len(icon_pool) < icons_needed:
        icon_pool.extend(self.ICONS)
    icon_pool = icon_pool[:icons_needed]
    if len(icon_pool) % 2 != 0:
        icon_pool.append(random.choice(self.ICONS))
    random.shuffle(icon_pool)
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if i * cols + j < len(icon_pool):
                row.append(icon_pool[i * cols + j])
            else:
                row.append(random.choice(self.ICONS))
        board.append(row)
    return board
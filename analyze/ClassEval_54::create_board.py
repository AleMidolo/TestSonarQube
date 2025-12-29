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
        raise ValueError('Board must have an even number of cells for matching pairs')
    icon_pairs = []
    for icon in self.ICONS:
        icon_pairs.extend([icon, icon])
    while len(icon_pairs) < total_cells:
        icon_pairs.extend(icon_pairs[:2])
    icon_pairs = icon_pairs[:total_cells]
    random.shuffle(icon_pairs)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icon_pairs[index])
            index += 1
        board.append(row)
    return board
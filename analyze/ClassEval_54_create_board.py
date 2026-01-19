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
        raise ValueError('Board must have an even number of cells')
    pairs_needed = total_cells // 2
    icon_pairs = []
    while len(icon_pairs) < pairs_needed:
        for icon in self.ICONS:
            if len(icon_pairs) < pairs_needed:
                icon_pairs.append(icon)
            else:
                break
    icon_list = []
    for icon in icon_pairs:
        icon_list.extend([icon, icon])
    random.shuffle(icon_list)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icon_list[index])
            index += 1
        board.append(row)
    return board
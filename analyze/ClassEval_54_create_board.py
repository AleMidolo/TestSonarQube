def create_board(self):
    """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
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
    if total_cells % 2 != 0:
        pairs_needed = total_cells // 2
        icon_pairs = []
        for i in range(pairs_needed):
            icon_pairs.append(self.ICONS[i % icon_count])
            icon_pairs.append(self.ICONS[i % icon_count])
        if total_cells % 2 == 1:
            icon_pairs.append(self.ICONS[0])
        icons = icon_pairs
    else:
        pairs_needed = total_cells // 2
        icons = []
        for i in range(pairs_needed):
            icon = self.ICONS[i % icon_count]
            icons.extend([icon, icon])
    random.shuffle(icons)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icons[index])
            index += 1
        board.append(row)
    return board
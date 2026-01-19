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
    if total_cells % 2 != 0:
        raise ValueError('Board must have an even number of cells')
    icon_pairs = []
    while len(icon_pairs) < total_cells:
        for icon in self.ICONS:
            if len(icon_pairs) < total_cells:
                icon_pairs.append(icon)
            if len(icon_pairs) < total_cells:
                icon_pairs.append(icon)
    random.shuffle(icon_pairs)
    board = []
    for i in range(rows):
        row = icon_pairs[i * cols:(i + 1) * cols]
        board.append(row)
    return board
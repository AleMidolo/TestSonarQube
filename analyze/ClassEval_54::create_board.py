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
    pairs_needed = total_cells // 2
    icon_pairs = []
    if pairs_needed <= len(self.ICONS):
        icon_pairs = self.ICONS[:pairs_needed]
    else:
        icon_pairs = list(self.ICONS)
        remaining = pairs_needed - len(self.ICONS)
        for _ in range(remaining):
            icon_pairs.append(random.choice(self.ICONS))
    all_icons = []
    for icon in icon_pairs:
        all_icons.extend([icon, icon])
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
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
    icons_list = []
    if total_cells % 2 != 0:
        total_cells += 1
    pairs_needed = total_cells // 2
    base_pairs_per_icon = pairs_needed // icon_count
    extra_pairs = pairs_needed % icon_count
    for i, icon in enumerate(self.ICONS):
        pairs_for_this_icon = base_pairs_per_icon
        if i < extra_pairs:
            pairs_for_this_icon += 1
        icons_list.extend([icon] * (pairs_for_this_icon * 2))
    if len(icons_list) > rows * cols:
        icons_list.pop()
    random.shuffle(icons_list)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icons_list[index])
            index += 1
        board.append(row)
    return board
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
    icon_counts = {}
    remaining_cells = total_cells
    for icon in self.ICONS:
        icon_counts[icon] = 2
        remaining_cells -= 2
    if remaining_cells > 0:
        if remaining_cells % 2 != 0:
            remaining_cells -= 1
        icons_list = list(self.ICONS)
        for _ in range(remaining_cells // 2):
            icon = random.choice(icons_list)
            icon_counts[icon] += 2
    flat_board = []
    for icon, count in icon_counts.items():
        flat_board.extend([icon] * count)
    random.shuffle(flat_board)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(flat_board[index])
            index += 1
        board.append(row)
    return board
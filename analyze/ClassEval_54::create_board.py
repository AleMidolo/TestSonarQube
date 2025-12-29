def create_board(self):
    """
        crea la tavola di gioco con la dimensione della tavola e le icone date
        :return: lista bidimensionale, la tavola di gioco
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.create_board()
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
    rows, cols = self.BOARD_SIZE
    total_cells = rows * cols
    icon_pairs = []
    for icon in self.ICONS:
        icon_pairs.extend([icon, icon])
    while len(icon_pairs) < total_cells:
        icon_pairs.extend(icon_pairs[:len(self.ICONS) * 2])
    icons = icon_pairs[:total_cells]
    random.shuffle(icons)
    board = []
    for i in range(rows):
        row = icons[i * cols:(i + 1) * cols]
        board.append(row)
    return board
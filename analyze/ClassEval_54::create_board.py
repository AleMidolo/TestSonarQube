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
    icons_count = len(self.ICONS)
    pairs_per_icon = total_cells // (icons_count * 2)
    remaining_cells = total_cells - pairs_per_icon * icons_count * 2
    icon_list = []
    for icon in self.ICONS:
        icon_list.extend([icon] * (pairs_per_icon * 2))
    for i in range(remaining_cells // 2):
        icon_list.extend([self.ICONS[i % icons_count]] * 2)
    random.shuffle(icon_list)
    board = []
    for i in range(rows):
        row = icon_list[i * cols:(i + 1) * cols]
        board.append(row)
    return board
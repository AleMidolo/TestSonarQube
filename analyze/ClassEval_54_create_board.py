def create_board(self):
    """
        crea el tablero de juego con el tamaño de tablero y los íconos dados
        :return: lista bidimensional, el tablero de juego
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
    remaining_pairs = total_cells % (icons_count * 2) // 2
    icon_pool = []
    for i, icon in enumerate(self.ICONS):
        pairs = pairs_per_icon + (1 if i < remaining_pairs else 0)
        icon_pool.extend([icon] * (pairs * 2))
    if len(icon_pool) < total_cells:
        icon_pool.extend([self.ICONS[0]] * (total_cells - len(icon_pool)))
    random.shuffle(icon_pool)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icon_pool[index])
            index += 1
        board.append(row)
    return board
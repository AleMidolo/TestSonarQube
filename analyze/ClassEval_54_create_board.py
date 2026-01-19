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
    icon_count = len(self.ICONS)
    if total_cells % 2 != 0:
        raise ValueError('Total number of cells must be even')
    pairs_needed = total_cells // 2
    base_pairs_per_icon = pairs_needed // icon_count
    extra_pairs = pairs_needed % icon_count
    icon_sequence = []
    for i, icon in enumerate(self.ICONS):
        pairs = base_pairs_per_icon
        if i < extra_pairs:
            pairs += 1
        icon_sequence.extend([icon] * (pairs * 2))
    random.shuffle(icon_sequence)
    board = []
    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(icon_sequence[index])
            index += 1
        board.append(row)
    return board
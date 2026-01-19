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
    icons_needed = []
    while len(icons_needed) < total_cells:
        icons_needed.extend(self.ICONS * 2)
    icons_needed = icons_needed[:total_cells]
    random.shuffle(icons_needed)
    board = []
    for i in range(rows):
        row = icons_needed[i * cols:(i + 1) * cols]
        board.append(row)
    return board
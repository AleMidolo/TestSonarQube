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
    icons_needed = total_cells // len(self.ICONS)
    icon_counts = [icons_needed] * len(self.ICONS)
    remainder = total_cells % len(self.ICONS)
    for i in range(remainder):
        icon_counts[i] += 1
    flat_board = []
    for icon, count in zip(self.ICONS, icon_counts):
        flat_board.extend([icon] * count)
    random.shuffle(flat_board)
    board = []
    for i in range(rows):
        row = flat_board[i * cols:(i + 1) * cols]
        board.append(row)
    return board
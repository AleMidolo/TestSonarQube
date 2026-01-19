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
    num_icons = len(self.ICONS)
    total_tiles = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
    icons_to_place = (self.ICONS * (total_tiles // num_icons))[:total_tiles]
    random.shuffle(icons_to_place)
    board = []
    for i in range(self.BOARD_SIZE[0]):
        row = icons_to_place[i * self.BOARD_SIZE[1]:(i + 1) * self.BOARD_SIZE[1]]
        board.append(row)
    return board
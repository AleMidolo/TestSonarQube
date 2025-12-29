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
    num_icons = len(self.ICONS)
    total_tiles = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
    icons_to_place = self.ICONS * (total_tiles // num_icons) + self.ICONS[:total_tiles % num_icons]
    random.shuffle(icons_to_place)
    board = []
    for i in range(self.BOARD_SIZE[0]):
        board.append(icons_to_place[i * self.BOARD_SIZE[1]:(i + 1) * self.BOARD_SIZE[1]])
    return board
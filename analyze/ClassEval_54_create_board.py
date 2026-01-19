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
    total_cells = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
    icons_list = (self.ICONS * (total_cells // num_icons + 1))[:total_cells]
    random.shuffle(icons_list)
    return [icons_list[i:i + self.BOARD_SIZE[1]] for i in range(0, total_cells, self.BOARD_SIZE[1])]
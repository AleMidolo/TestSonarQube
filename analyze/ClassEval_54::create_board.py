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
        num_icons = len(self.ICONS)
        total_tiles = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
        icons_to_use = (self.ICONS * (total_tiles // num_icons + 1))[:total_tiles]
        random.shuffle(icons_to_use)
        board = [icons_to_use[i:i + self.BOARD_SIZE[1]] for i in range(0, total_tiles, self.BOARD_SIZE[1])]
        return board
def create_board(self):
        """
        दिए गए बोर्ड आकार और आइकनों के साथ खेल का बोर्ड बनाएं
        :return: 2-आयामी सूची, खेल का बोर्ड
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.create_board()
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
        num_icons = len(self.ICONS)
        total_cells = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
        icons_to_place = (self.ICONS * (total_cells // num_icons)) + self.ICONS[:total_cells % num_icons]
        random.shuffle(icons_to_place)
        
        board = []
        for i in range(self.BOARD_SIZE[0]):
            row = icons_to_place[i * self.BOARD_SIZE[1]:(i + 1) * self.BOARD_SIZE[1]]
            board.append(row)
        
        return board
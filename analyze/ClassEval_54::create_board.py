def create_board(self):
    """
        创建具有给定大小和图标的游戏棋盘
        :return: 二维列表，游戏棋盘
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
    board = [icons_to_place[i:i + self.BOARD_SIZE[1]] for i in range(0, total_tiles, self.BOARD_SIZE[1])]
    return board
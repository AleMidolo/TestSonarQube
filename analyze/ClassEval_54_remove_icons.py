def remove_icons(self, pos1, pos2):
    """
    खेल के बोर्ड पर जुड़े हुए आइकनों को हटाएं
    :param pos1: पहले आइकन को हटाने की स्थिति ट्यूपल(x, y)
    :param pos2: दूसरे आइकन को हटाने की स्थिति ट्यूपल(x, y)
    :return: None
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    >>> mc.remove_icons((0, 0), (1, 0))
    mc.board = [[' ', 'b', 'c', 'a'],
                [' ', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    """
    x1, y1 = pos1
    x2, y2 = pos2
    self.board[y1][x1] = ' '
    self.board[y2][x2] = ' '
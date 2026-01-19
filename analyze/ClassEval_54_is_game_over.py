def is_game_over(self):
    """
    检查游戏是否结束（即，游戏板上是否没有更多图标）
    :return: True 或 False，表示游戏是否结束
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    >>> mc.board = [[' ', ' ', ' ', ' '],
    >>>         [' ', ' ', ' ', ' '],
    >>>         [' ', ' ', ' ', ' '],
    >>>         [' ', ' ', ' ', ' ']]
    >>> mc.is_game_over()
    True
    """
    for row in self.board:
        for cell in row:
            if cell != ' ':
                return False
    return True
def is_board_full(self):
    """
    检查游戏棋盘是否完全填满。
    :return: bool，表示游戏棋盘是否已满
    >>> ttt.is_board_full()
    False
    """
    for row in self.board:
        for cell in row:
            if cell == ' ' or cell == '':
                return False
    return True
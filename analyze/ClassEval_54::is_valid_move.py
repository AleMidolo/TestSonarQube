def is_valid_move(self, pos1, pos2):
    """
        检查两个图标的移动是否有效（即位置在游戏棋盘范围内，两个位置不相同，两个位置有相同的图标，并且两个位置之间有有效路径）
        :param pos1: 第一个图标的位置元组(x, y)
        :param pos2: 第二个图标的位置元组(x, y)
        :return: True 或 False，表示两个图标的移动是否有效
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
    if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1]):
        return False
    if not (0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
        return False
    if pos1 == pos2:
        return False
    if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
        return False
    if self.board[pos1[0]][pos1[1]] == ' ' or self.board[pos2[0]][pos2[1]] == ' ':
        return False
    return self.has_path(pos1, pos2)
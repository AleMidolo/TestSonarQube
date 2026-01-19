def has_path(self, pos1, pos2):
    """
    检查两个图标之间是否存在路径
    :param pos1: 第一个图标的位置元组(x, y)
    :param pos2: 第二个图标的位置元组(x, y)
    :return: True 或 False，表示两个图标之间是否存在路径
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    >>> mc.is_valid_move((0, 0), (1, 0))
    True
    """
    # 连连看游戏规则：两个相同图标可以通过最多3条直线（最多2次转弯）连接，且路径上不能有其他图标
    
    # 如果两个位置相同，返回False
    if pos1 == pos2:
        return False
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 检查位置是否有效
    if not (0 <= x1 < len(self.board) and 0 <= y1 < len(self.board[0])):
        return False
    if not (0 <= x2 < len(self.board) and 0 <= y2 < len(self.board[0])):
        return False
    
    # 检查两个位置的图标是否相同（且不为空）
    if self.board[x1][y1] != self.board[x2][y2] or self.board[x1][y1] is None or self.board[x1][y1] == '':
        return False
    
    # 检查直线连接（0次转弯）
    if self._check_straight_line(pos1, pos2):
        return True
    
    # 检查一次转弯
    if self._check_one_turn(pos1, pos2):
        return True
    
    # 检查两次转弯
    if self._check_two_turns(pos1, pos2):
        return True
    
    return False

def _check_straight_line(self, pos1, pos2):
    """检查两点之间是否可以直线连接"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 水平直线
    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            if self.board[x1][y] is not None and self.board[x1][y] != '':
                return False
        return True
    
    # 垂直直线
    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            if self.board[x][y1] is not None and self.board[x][y1] != '':
                return False
        return True
    
    return False

def _check_one_turn(self, pos1, pos2):
    """检查两点之间是否可以通过一次转弯连接"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 转折点1: (x1, y2)
    corner1 = (x1, y2)
    if (self.board[x1][y2] is None or self.board[x1][y2] == '') or corner1 == pos1 or corner1 == pos2:
        if self._check_straight_line(pos1, corner1) and self._check_straight_line(corner1, pos2):
            return True
    
    # 转折点2: (x2, y1)
    corner2 = (x2, y1)
    if (self.board[x2][y1] is None or self.board[x2][y1] == '') or corner2 == pos1 or corner2 == pos2:
        if self._check_straight_line(pos1, corner2) and self._check_straight_line(corner2, pos2):
            return True
    
    return False

def _check_two_turns(self, pos1, pos2):
    """检查两点之间是否可以通过两次转弯连接"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 尝试水平方向延伸
    for y in range(len(self.board[0])):
        if (self.board[x1][y] is None or self.board[x1][y] == '' or (x1, y) == pos1) and \
           (self.board[x2][y] is None or self.board[x2][y] == '' or (x2, y) == pos2):
            if self._check_straight_line(pos1, (x1, y)) and \
               self._check_straight_line((x1, y), (x2, y)) and \
               self._check_straight_line((x2, y), pos2):
                return True
    
    # 尝试垂直方向延伸
    for x in range(len(self.board)):
        if (self.board[x][y1] is None or self.board[x][y1] == '' or (x, y1) == pos1) and \
           (self.board[x][y2] is None or self.board[x][y2] == '' or (x, y2) == pos2):
            if self._check_straight_line(pos1, (x, y1)) and \
               self._check_straight_line((x, y1), (x, y2)) and \
               self._check_straight_line((x, y2), pos2):
                return True
    
    return False
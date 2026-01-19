def has_path(self, pos1, pos2):
    """
    检查两个图标之间是否存在路径
    :param pos1: 第一个图标的位置元组(x, y)
    :param pos2: 第二个图标的位置元组(x, y)
    :return: True 或 False，表示两个图标之间是否存在路径
    """
    # 如果两个位置相同，返回False
    if pos1 == pos2:
        return False
    
    # 获取棋盘尺寸
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 检查位置是否有效
    if not (0 <= x1 < cols and 0 <= y1 < rows and 0 <= x2 < cols and 0 <= y2 < rows):
        return False
    
    # 检查两个位置的图标是否相同（且不为空）
    if self.board[y1][x1] != self.board[y2][x2] or self.board[y1][x1] is None:
        return False
    
    # 连连看规则：最多转折2次（即最多3条线段）
    # 尝试直线连接（0次转折）
    if self._check_straight_line(pos1, pos2):
        return True
    
    # 尝试一次转折
    if self._check_one_turn(pos1, pos2):
        return True
    
    # 尝试两次转折
    if self._check_two_turns(pos1, pos2):
        return True
    
    return False

def _check_straight_line(self, pos1, pos2):
    """检查两点之间是否可以直线连接"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 水平直线
    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            if self.board[y1][x] is not None:
                return False
        return True
    
    # 垂直直线
    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            if self.board[y][x1] is not None:
                return False
        return True
    
    return False

def _check_one_turn(self, pos1, pos2):
    """检查两点之间是否可以通过一次转折连接"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 转折点1: (x1, y2)
    if (self.board[y2][x1] is None or (x1, y2) == pos1 or (x1, y2) == pos2):
        if self._check_straight_line(pos1, (x1, y2)) and self._check_straight_line((x1, y2), pos2):
            return True
    
    # 转折点2: (x2, y1)
    if (self.board[y1][x2] is None or (x2, y1) == pos1 or (x2, y1) == pos2):
        if self._check_straight_line(pos1, (x2, y1)) and self._check_straight_line((x2, y1), pos2):
            return True
    
    return False

def _check_two_turns(self, pos1, pos2):
    """检查两点之间是否可以通过两次转折连接"""
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 尝试水平扫描
    for y in range(rows):
        if (y == y1 or self.board[y][x1] is None or (x1, y) == pos1) and \
           (y == y2 or self.board[y][x2] is None or (x2, y) == pos2):
            if self._check_straight_line(pos1, (x1, y)) and \
               self._check_straight_line((x1, y), (x2, y)) and \
               self._check_straight_line((x2, y), pos2):
                return True
    
    # 尝试垂直扫描
    for x in range(cols):
        if (x == x1 or self.board[y1][x] is None or (x, y1) == pos1) and \
           (x == x2 or self.board[y2][x] is None or (x, y2) == pos2):
            if self._check_straight_line(pos1, (x, y1)) and \
               self._check_straight_line((x, y1), (x, y2)) and \
               self._check_straight_line((x, y2), pos2):
                return True
    
    return False
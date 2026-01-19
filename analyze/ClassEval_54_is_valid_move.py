def is_valid_move(self, pos1, pos2):
    """
    检查两个图标的移动是否有效（即位置在游戏棋盘范围内，两个位置不相同，两个位置有相同的图标，并且两个位置之间有有效路径）
    :param pos1: 第一个图标的位置元组(x, y)
    :param pos2: 第二个图标的位置元组(x, y)
    :return: True 或 False，表示两个图标的移动是否有效
    """
    # 检查位置是否在棋盘范围内
    if not self._is_in_bounds(pos1) or not self._is_in_bounds(pos2):
        return False
    
    # 检查两个位置是否相同
    if pos1 == pos2:
        return False
    
    # 检查两个位置是否都有图标（不为空）
    x1, y1 = pos1
    x2, y2 = pos2
    if self.board[y1][x1] is None or self.board[y2][x2] is None:
        return False
    
    # 检查两个位置的图标是否相同
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # 检查是否有有效路径（最多两个转角）
    return self._has_valid_path(pos1, pos2)

def _is_in_bounds(self, pos):
    """检查位置是否在棋盘范围内"""
    x, y = pos
    return 0 <= y < len(self.board) and 0 <= x < len(self.board[0])

def _has_valid_path(self, pos1, pos2):
    """检查两个位置之间是否有有效路径（0个、1个或2个转角）"""
    # 0个转角：直线连接
    if self._has_straight_path(pos1, pos2):
        return True
    
    # 1个转角：L形路径
    if self._has_one_turn_path(pos1, pos2):
        return True
    
    # 2个转角：Z形路径
    if self._has_two_turn_path(pos1, pos2):
        return True
    
    return False

def _has_straight_path(self, pos1, pos2):
    """检查是否有直线路径"""
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

def _has_one_turn_path(self, pos1, pos2):
    """检查是否有一个转角的路径"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 转角点1: (x1, y2)
    corner1 = (x1, y2)
    if self._is_empty_or_endpoint(corner1, pos1, pos2):
        if self._has_straight_path(pos1, corner1) and self._has_straight_path(corner1, pos2):
            return True
    
    # 转角点2: (x2, y1)
    corner2 = (x2, y1)
    if self._is_empty_or_endpoint(corner2, pos1, pos2):
        if self._has_straight_path(pos1, corner2) and self._has_straight_path(corner2, pos2):
            return True
    
    return False

def _has_two_turn_path(self, pos1, pos2):
    """检查是否有两个转角的路径"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 尝试水平方向的中间线
    for x in range(len(self.board[0])):
        mid1 = (x, y1)
        mid2 = (x, y2)
        if self._is_empty_or_endpoint(mid1, pos1, pos2) and self._is_empty_or_endpoint(mid2, pos1, pos2):
            if (self._has_straight_path(pos1, mid1) and 
                self._has_straight_path(mid1, mid2) and 
                self._has_straight_path(mid2, pos2)):
                return True
    
    # 尝试垂直方向的中间线
    for y in range(len(self.board)):
        mid1 = (x1, y)
        mid2 = (x2, y)
        if self._is_empty_or_endpoint(mid1, pos1, pos2) and self._is_empty_or_endpoint(mid2, pos1, pos2):
            if (self._has_straight_path(pos1, mid1) and 
                self._has_straight_path(mid1, mid2) and 
                self._has_straight_path(mid2, pos2)):
                return True
    
    return False

def _is_empty_or_endpoint(self, pos, pos1, pos2):
    """检查位置是否为空或是端点之一"""
    if pos == pos1 or pos == pos2:
        return True
    x, y = pos
    return self.board[y][x] is None
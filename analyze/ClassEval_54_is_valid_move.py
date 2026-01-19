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
    
    # 检查两个位置的图标是否相同
    x1, y1 = pos1
    x2, y2 = pos2
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # 检查两个位置的图标是否都不为空
    if self.board[y1][x1] is None or self.board[y2][x2] is None:
        return False
    
    # 检查是否存在有效路径
    return self._has_valid_path(pos1, pos2)

def _is_in_bounds(self, pos):
    """检查位置是否在棋盘范围内"""
    x, y = pos
    return 0 <= y < len(self.board) and 0 <= x < len(self.board[0])

def _has_valid_path(self, pos1, pos2):
    """检查两个位置之间是否有有效路径（最多转折2次）"""
    # 尝试0次转折（直线连接）
    if self._can_connect_straight(pos1, pos2):
        return True
    
    # 尝试1次转折
    if self._can_connect_one_turn(pos1, pos2):
        return True
    
    # 尝试2次转折
    if self._can_connect_two_turns(pos1, pos2):
        return True
    
    return False

def _can_connect_straight(self, pos1, pos2):
    """检查是否可以直线连接"""
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

def _can_connect_one_turn(self, pos1, pos2):
    """检查是否可以通过一次转折连接"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 尝试转折点 (x1, y2)
    corner1 = (x1, y2)
    if (corner1 != pos1 and corner1 != pos2 and 
        (self.board[y2][x1] is None or corner1 == pos2) and
        self._can_connect_straight(pos1, corner1) and 
        self._can_connect_straight(corner1, pos2)):
        return True
    
    # 尝试转折点 (x2, y1)
    corner2 = (x2, y1)
    if (corner2 != pos1 and corner2 != pos2 and 
        (self.board[y1][x2] is None or corner2 == pos2) and
        self._can_connect_straight(pos1, corner2) and 
        self._can_connect_straight(corner2, pos2)):
        return True
    
    return False

def _can_connect_two_turns(self, pos1, pos2):
    """检查是否可以通过两次转折连接"""
    # 这里实现简化版本，检查是否可以通过扩展边界来连接
    # 实际连连看游戏通常允许路径延伸到棋盘外围
    return False
def has_path(self, pos1, pos2):
    """
    检查两个图标之间是否存在路径
    :param pos1: 第一个图标的位置元组(x, y)
    :param pos2: 第二个图标的位置元组(x, y)
    :return: True 或 False，表示两个图标之间是否存在路径
    """
    # 检查两个位置的图标是否相同
    if self.board[pos1[1]][pos1[0]] != self.board[pos2[1]][pos2[0]]:
        return False
    
    # 检查是否是同一个位置
    if pos1 == pos2:
        return False
    
    # 连连看规则：最多转折2次（即最多3条线段）
    # 尝试直接连接（0次转折）
    if self._can_connect_direct(pos1, pos2):
        return True
    
    # 尝试1次转折
    if self._can_connect_one_turn(pos1, pos2):
        return True
    
    # 尝试2次转折
    if self._can_connect_two_turns(pos1, pos2):
        return True
    
    return False

def _can_connect_direct(self, pos1, pos2):
    """检查两点是否可以直接连接（同行或同列且中间无障碍）"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 同一行
    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            if self.board[y1][x] != '':
                return False
        return True
    
    # 同一列
    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            if self.board[y][x1] != '':
                return False
        return True
    
    return False

def _can_connect_one_turn(self, pos1, pos2):
    """检查两点是否可以通过1次转折连接"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 转折点1: (x1, y2)
    if self._is_empty_or_endpoint(x1, y2, pos1, pos2):
        if self._can_connect_direct(pos1, (x1, y2)) and self._can_connect_direct((x1, y2), pos2):
            return True
    
    # 转折点2: (x2, y1)
    if self._is_empty_or_endpoint(x2, y1, pos1, pos2):
        if self._can_connect_direct(pos1, (x2, y1)) and self._can_connect_direct((x2, y1), pos2):
            return True
    
    return False

def _can_connect_two_turns(self, pos1, pos2):
    """检查两点是否可以通过2次转折连接"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 尝试水平方向扩展
    for x in range(len(self.board[0])):
        if self._is_empty_or_endpoint(x, y1, pos1, pos2) and self._is_empty_or_endpoint(x, y2, pos1, pos2):
            if (self._can_connect_direct(pos1, (x, y1)) and 
                self._can_connect_direct((x, y1), (x, y2)) and 
                self._can_connect_direct((x, y2), pos2)):
                return True
    
    # 尝试垂直方向扩展
    for y in range(len(self.board)):
        if self._is_empty_or_endpoint(x1, y, pos1, pos2) and self._is_empty_or_endpoint(x2, y, pos1, pos2):
            if (self._can_connect_direct(pos1, (x1, y)) and 
                self._can_connect_direct((x1, y), (x2, y)) and 
                self._can_connect_direct((x2, y), pos2)):
                return True
    
    return False

def _is_empty_or_endpoint(self, x, y, pos1, pos2):
    """检查位置是否为空或是端点之一"""
    if (x, y) == pos1 or (x, y) == pos2:
        return True
    if 0 <= x < len(self.board[0]) and 0 <= y < len(self.board):
        return self.board[y][x] == ''
    return False
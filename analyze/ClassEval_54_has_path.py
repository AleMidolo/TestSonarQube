def has_path(self, pos1, pos2):
    """
    दो आइकनों के बीच एक पथ है या नहीं, यह जांचें
    :param pos1: पहले आइकन की स्थिति ट्यूपल(x, y)
    :param pos2: दूसरे आइकन की स्थिति ट्यूपल(x, y)
    :return: True या False, जो दर्शाता है कि दो आइकनों के बीच एक पथ है या नहीं
    """
    # Check if positions are the same
    if pos1 == pos2:
        return False
    
    # Check if the icons at both positions match
    if self.board[pos1[1]][pos1[0]] != self.board[pos2[1]][pos2[0]]:
        return False
    
    # Try to find a path with at most 2 turns (standard Mahjong Connect rules)
    # Check direct line (0 turns)
    if self._has_direct_path(pos1, pos2):
        return True
    
    # Check one-turn path
    if self._has_one_turn_path(pos1, pos2):
        return True
    
    # Check two-turn path
    if self._has_two_turn_path(pos1, pos2):
        return True
    
    return False

def _has_direct_path(self, pos1, pos2):
    """Check if there's a direct line between two positions"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Horizontal line
    if y1 == y2:
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        for x in range(start_x + 1, end_x):
            if self.board[y1][x] is not None and self.board[y1][x] != '':
                return False
        return True
    
    # Vertical line
    if x1 == x2:
        start_y = min(y1, y2)
        end_y = max(y1, y2)
        for y in range(start_y + 1, end_y):
            if self.board[y][x1] is not None and self.board[y][x1] != '':
                return False
        return True
    
    return False

def _has_one_turn_path(self, pos1, pos2):
    """Check if there's a path with one turn"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Try corner point (x1, y2)
    corner1 = (x1, y2)
    if self._is_empty_or_target(corner1, pos1, pos2):
        if self._has_direct_path(pos1, corner1) and self._has_direct_path(corner1, pos2):
            return True
    
    # Try corner point (x2, y1)
    corner2 = (x2, y1)
    if self._is_empty_or_target(corner2, pos1, pos2):
        if self._has_direct_path(pos1, corner2) and self._has_direct_path(corner2, pos2):
            return True
    
    return False

def _has_two_turn_path(self, pos1, pos2):
    """Check if there's a path with two turns"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Try horizontal then vertical then horizontal
    for x in range(len(self.board[0])):
        mid1 = (x, y1)
        mid2 = (x, y2)
        if self._is_empty_or_target(mid1, pos1, pos2) and self._is_empty_or_target(mid2, pos1, pos2):
            if (self._has_direct_path(pos1, mid1) and 
                self._has_direct_path(mid1, mid2) and 
                self._has_direct_path(mid2, pos2)):
                return True
    
    # Try vertical then horizontal then vertical
    for y in range(len(self.board)):
        mid1 = (x1, y)
        mid2 = (x2, y)
        if self._is_empty_or_target(mid1, pos1, pos2) and self._is_empty_or_target(mid2, pos1, pos2):
            if (self._has_direct_path(pos1, mid1) and 
                self._has_direct_path(mid1, mid2) and 
                self._has_direct_path(mid2, pos2)):
                return True
    
    return False

def _is_empty_or_target(self, pos, pos1, pos2):
    """Check if a position is empty or one of the target positions"""
    if pos == pos1 or pos == pos2:
        return True
    x, y = pos
    if 0 <= x < len(self.board[0]) and 0 <= y < len(self.board):
        return self.board[y][x] is None or self.board[y][x] == ''
    return False
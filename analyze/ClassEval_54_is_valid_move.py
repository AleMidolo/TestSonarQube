def is_valid_move(self, pos1, pos2):
    """
    दो आइकनों की चाल को मान्य है या नहीं, यह जांचें (यानी, स्थान खेल बोर्ड की सीमा के भीतर हैं, दोनों स्थान समान नहीं हैं, दोनों स्थानों में समान आइकन हैं, और दोनों स्थानों के बीच एक मान्य पथ है)
    :param pos1: पहले आइकन की स्थिति ट्यूपल(x, y)
    :param pos2: दूसरे आइकन की स्थिति ट्यूपल(x, y)
    :return: True या False, जो दर्शाता है कि दो आइकनों की चाल मान्य है या नहीं
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    >>> mc.is_valid_move((0, 0), (1, 0))
    True
    """
    # Check if positions are the same
    if pos1 == pos2:
        return False
    
    # Check if positions are within board boundaries
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    if not (0 <= x1 < cols and 0 <= y1 < rows):
        return False
    if not (0 <= x2 < cols and 0 <= y2 < rows):
        return False
    
    # Check if both positions have the same icon
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # Check if there's a valid path between the two positions
    # Mahjong Connect allows paths with at most 2 turns (3 line segments)
    return self._has_valid_path(pos1, pos2)

def _has_valid_path(self, pos1, pos2):
    """Helper method to check if there's a valid path with at most 2 turns"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Try direct line (0 turns)
    if self._is_clear_line(pos1, pos2):
        return True
    
    # Try 1 turn (L-shape)
    corner1 = (x1, y2)
    corner2 = (x2, y1)
    
    if self._is_empty_or_target(corner1, pos1, pos2):
        if self._is_clear_line(pos1, corner1) and self._is_clear_line(corner1, pos2):
            return True
    
    if self._is_empty_or_target(corner2, pos1, pos2):
        if self._is_clear_line(pos1, corner2) and self._is_clear_line(corner2, pos2):
            return True
    
    # Try 2 turns (Z-shape)
    # Horizontal then vertical then horizontal
    for x in range(-1, len(self.board[0]) + 1):
        mid1 = (x, y1)
        mid2 = (x, y2)
        if self._is_empty_or_target(mid1, pos1, pos2) and self._is_empty_or_target(mid2, pos1, pos2):
            if (self._is_clear_line(pos1, mid1) and 
                self._is_clear_line(mid1, mid2) and 
                self._is_clear_line(mid2, pos2)):
                return True
    
    # Vertical then horizontal then vertical
    for y in range(-1, len(self.board) + 1):
        mid1 = (x1, y)
        mid2 = (x2, y)
        if self._is_empty_or_target(mid1, pos1, pos2) and self._is_empty_or_target(mid2, pos1, pos2):
            if (self._is_clear_line(pos1, mid1) and 
                self._is_clear_line(mid1, mid2) and 
                self._is_clear_line(mid2, pos2)):
                return True
    
    return False

def _is_empty_or_target(self, pos, pos1, pos2):
    """Check if position is empty or one of the target positions"""
    if pos == pos1 or pos == pos2:
        return True
    x, y = pos
    if x < 0 or x >= len(self.board[0]) or y < 0 or y >= len(self.board):
        return True  # Outside board is considered passable
    return self.board[y][x] == '' or self.board[y][x] is None

def _is_clear_line(self, pos1, pos2):
    """Check if there's a clear straight line between two positions"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Must be horizontal or vertical line
    if x1 != x2 and y1 != y2:
        return False
    
    # Horizontal line
    if y1 == y2:
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        for x in range(start_x, end_x + 1):
            if not self._is_empty_or_target((x, y1), pos1, pos2):
                return False
        return True
    
    # Vertical line
    if x1 == x2:
        start_y = min(y1, y2)
        end_y = max(y1, y2)
        for y in range(start_y, end_y + 1):
            if not self._is_empty_or_target((x1, y), pos1, pos2):
                return False
        return True
    
    return False
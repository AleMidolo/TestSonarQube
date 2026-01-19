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
    # Check if positions are within board boundaries
    if not (0 <= pos1[0] < len(self.board[0]) and 0 <= pos1[1] < len(self.board)):
        return False
    if not (0 <= pos2[0] < len(self.board[0]) and 0 <= pos2[1] < len(self.board)):
        return False
    
    # Check if positions are different
    if pos1 == pos2:
        return False
    
    # Check if both positions have the same icon
    icon1 = self.board[pos1[1]][pos1[0]]
    icon2 = self.board[pos2[1]][pos2[0]]
    
    if icon1 != icon2 or icon1 is None or icon2 is None:
        return False
    
    # Check if there's a valid path between the two positions
    # Mahjong Connect allows paths with at most 2 turns (3 line segments)
    return self._has_valid_path(pos1, pos2)

def _has_valid_path(self, pos1, pos2):
    """Helper method to check if there's a valid path with at most 2 turns"""
    # Try direct line (0 turns)
    if self._is_clear_line(pos1, pos2):
        return True
    
    # Try 1 turn (L-shaped path)
    corner1 = (pos1[0], pos2[1])
    corner2 = (pos2[0], pos1[1])
    
    if self._is_empty_or_target(corner1, pos1, pos2):
        if self._is_clear_line(pos1, corner1) and self._is_clear_line(corner1, pos2):
            return True
    
    if self._is_empty_or_target(corner2, pos1, pos2):
        if self._is_clear_line(pos1, corner2) and self._is_clear_line(corner2, pos2):
            return True
    
    # Try 2 turns (Z-shaped path)
    for y in range(len(self.board)):
        for x in range(len(self.board[0])):
            mid = (x, y)
            if self._is_empty_or_target(mid, pos1, pos2):
                if (self._is_clear_line(pos1, mid) and self._is_clear_line(mid, pos2)):
                    return True
    
    return False

def _is_clear_line(self, pos1, pos2):
    """Check if there's a clear straight line between two positions"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Horizontal line
    if y1 == y2:
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        for x in range(start_x, end_x + 1):
            if (x, y1) != pos1 and (x, y1) != pos2:
                if self.board[y1][x] is not None:
                    return False
        return True
    
    # Vertical line
    if x1 == x2:
        start_y = min(y1, y2)
        end_y = max(y1, y2)
        for y in range(start_y, end_y + 1):
            if (x1, y) != pos1 and (x1, y) != pos2:
                if self.board[y][x1] is not None:
                    return False
        return True
    
    return False

def _is_empty_or_target(self, pos, pos1, pos2):
    """Check if position is empty or one of the target positions"""
    if pos == pos1 or pos == pos2:
        return True
    x, y = pos
    if 0 <= x < len(self.board[0]) and 0 <= y < len(self.board):
        return self.board[y][x] is None
    return False
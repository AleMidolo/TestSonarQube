def has_path(self, pos1, pos2):
    """
    verifica si hay un camino entre dos íconos
    :param pos1: tupla de posición (x, y) del primer ícono
    :param pos2: tupla de posición (x, y) del segundo ícono
    :return: True o False, representando si hay un camino entre dos íconos
    """
    # Check if positions are the same
    if pos1 == pos2:
        return False
    
    # Check if the icons at both positions match
    x1, y1 = pos1
    x2, y2 = pos2
    
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # Mahjong Connect allows paths with at most 2 turns (3 line segments)
    # Try direct line (0 turns)
    if self._has_direct_line(pos1, pos2):
        return True
    
    # Try 1 turn (2 line segments)
    if self._has_one_turn_path(pos1, pos2):
        return True
    
    # Try 2 turns (3 line segments)
    if self._has_two_turn_path(pos1, pos2):
        return True
    
    return False

def _has_direct_line(self, pos1, pos2):
    """Check if there's a direct line between two positions"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Same row
    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            if self.board[y1][x] is not None:
                return False
        return True
    
    # Same column
    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            if self.board[y][x1] is not None:
                return False
        return True
    
    return False

def _has_one_turn_path(self, pos1, pos2):
    """Check if there's a path with one turn"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Try corner point (x1, y2)
    corner1 = (x1, y2)
    if self.board[y2][x1] is None or corner1 == pos1 or corner1 == pos2:
        if self._has_direct_line(pos1, corner1) and self._has_direct_line(corner1, pos2):
            return True
    
    # Try corner point (x2, y1)
    corner2 = (x2, y1)
    if self.board[y1][x2] is None or corner2 == pos1 or corner2 == pos2:
        if self._has_direct_line(pos1, corner2) and self._has_direct_line(corner2, pos2):
            return True
    
    return False

def _has_two_turn_path(self, pos1, pos2):
    """Check if there's a path with two turns"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Try horizontal then vertical then horizontal
    for x in range(len(self.board[0])):
        if (self.board[y1][x] is None or (x, y1) == pos1) and \
           (self.board[y2][x] is None or (x, y2) == pos2):
            mid1 = (x, y1)
            mid2 = (x, y2)
            if self._has_direct_line(pos1, mid1) and \
               self._has_direct_line(mid1, mid2) and \
               self._has_direct_line(mid2, pos2):
                return True
    
    # Try vertical then horizontal then vertical
    for y in range(len(self.board)):
        if (self.board[y][x1] is None or (x1, y) == pos1) and \
           (self.board[y][x2] is None or (x2, y) == pos2):
            mid1 = (x1, y)
            mid2 = (x2, y)
            if self._has_direct_line(pos1, mid1) and \
               self._has_direct_line(mid1, mid2) and \
               self._has_direct_line(mid2, pos2):
                return True
    
    return False
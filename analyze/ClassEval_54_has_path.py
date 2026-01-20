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
    
    # Check for path with at most 2 turns (0, 1, or 2 turns)
    # Try direct line (0 turns)
    if self._has_direct_path(pos1, pos2):
        return True
    
    # Try path with 1 turn
    if self._has_one_turn_path(pos1, pos2):
        return True
    
    # Try path with 2 turns
    if self._has_two_turn_path(pos1, pos2):
        return True
    
    return False

def _has_direct_path(self, pos1, pos2):
    """Check if there's a direct line between two positions"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Check horizontal line
    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            if self.board[y1][x] != '':
                return False
        return True
    
    # Check vertical line
    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            if self.board[y][x1] != '':
                return False
        return True
    
    return False

def _has_one_turn_path(self, pos1, pos2):
    """Check if there's a path with one turn"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Try corner at (x1, y2)
    corner1 = (x1, y2)
    if (corner1 != pos1 and corner1 != pos2 and 
        self.board[y2][x1] == '' and
        self._has_direct_path(pos1, corner1) and 
        self._has_direct_path(corner1, pos2)):
        return True
    
    # Try corner at (x2, y1)
    corner2 = (x2, y1)
    if (corner2 != pos1 and corner2 != pos2 and
        self.board[y1][x2] == '' and
        self._has_direct_path(pos1, corner2) and 
        self._has_direct_path(corner2, pos2)):
        return True
    
    return False

def _has_two_turn_path(self, pos1, pos2):
    """Check if there's a path with two turns"""
    x1, y1 = pos1
    x2, y2 = pos2
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    # Try horizontal then vertical then horizontal
    for x in range(cols):
        if x == x1 or x == x2:
            continue
        mid1 = (x, y1)
        mid2 = (x, y2)
        if (self.board[y1][x] == '' and self.board[y2][x] == '' and
            self._has_direct_path(pos1, mid1) and
            self._has_direct_path(mid1, mid2) and
            self._has_direct_path(mid2, pos2)):
            return True
    
    # Try vertical then horizontal then vertical
    for y in range(rows):
        if y == y1 or y == y2:
            continue
        mid1 = (x1, y)
        mid2 = (x2, y)
        if (self.board[y][x1] == '' and self.board[y][x2] == '' and
            self._has_direct_path(pos1, mid1) and
            self._has_direct_path(mid1, mid2) and
            self._has_direct_path(mid2, pos2)):
            return True
    
    return False
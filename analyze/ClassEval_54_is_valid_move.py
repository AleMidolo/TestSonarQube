def is_valid_move(self, pos1, pos2):
    """
    check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
    :param pos1: position tuple(x, y) of the first icon
    :param pos2: position tuple(x, y) of the second icon
    :return:True or False ,representing whether the move of two icons is valid
    """
    # Check if positions are within board range
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    if not (0 <= x1 < cols and 0 <= y1 < rows):
        return False
    if not (0 <= x2 < cols and 0 <= y2 < rows):
        return False
    
    # Check if positions are not the same
    if pos1 == pos2:
        return False
    
    # Check if both positions have the same icon
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # Check if there is a valid path between the two positions
    # In Mahjong Connect, a valid path has at most 2 turns (3 line segments)
    return self.has_valid_path(pos1, pos2)


def has_valid_path(self, pos1, pos2):
    """
    Check if there is a valid path between two positions with at most 2 turns.
    """
    # Try direct line (0 turns)
    if self.is_direct_path(pos1, pos2):
        return True
    
    # Try 1 turn (2 line segments)
    if self.is_one_turn_path(pos1, pos2):
        return True
    
    # Try 2 turns (3 line segments)
    if self.is_two_turn_path(pos1, pos2):
        return True
    
    return False


def is_direct_path(self, pos1, pos2):
    """Check if there's a direct horizontal or vertical path."""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Same row (horizontal)
    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            if self.board[y1][x] != '':
                return False
        return True
    
    # Same column (vertical)
    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            if self.board[y][x1] != '':
                return False
        return True
    
    return False


def is_one_turn_path(self, pos1, pos2):
    """Check if there's a path with one turn."""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Try corner at (x1, y2)
    corner1 = (x1, y2)
    if (corner1 != pos1 and corner1 != pos2 and 
        self.board[y2][x1] == '' and
        self.is_direct_path(pos1, corner1) and 
        self.is_direct_path(corner1, pos2)):
        return True
    
    # Try corner at (x2, y1)
    corner2 = (x2, y1)
    if (corner2 != pos1 and corner2 != pos2 and 
        self.board[y1][x2] == '' and
        self.is_direct_path(pos1, corner2) and 
        self.is_direct_path(corner2, pos2)):
        return True
    
    return False


def is_two_turn_path(self, pos1, pos2):
    """Check if there's a path with two turns."""
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    # Try all possible intermediate points
    for y in range(rows):
        for x in range(cols):
            if (x, y) != pos1 and (x, y) != pos2:
                if self.board[y][x] == '':
                    if self.is_one_turn_path(pos1, (x, y)) and self.is_direct_path((x, y), pos2):
                        return True
                    if self.is_direct_path(pos1, (x, y)) and self.is_one_turn_path((x, y), pos2):
                        return True
    
    return False
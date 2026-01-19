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
    
    # Check if either position is empty (already removed)
    if self.board[y1][x1] is None or self.board[y2][x2] is None:
        return False
    
    # Check if there is a valid path between the two positions
    return self.has_valid_path(pos1, pos2)
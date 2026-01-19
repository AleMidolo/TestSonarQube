def remove_icons(self, pos1, pos2):
    """
    remove the connected icons on the game board
    :param pos1: position tuple(x, y) of the first icon to be removed
    :param pos2: position tuple(x, y) of the second icon to be removed
    :return: None
    """
    x1, y1 = pos1
    x2, y2 = pos2
    
    self.board[y1][x1] = ' '
    self.board[y2][x2] = ' '
def remove_icons(self, pos1, pos2):
    """
    移除游戏棋盘上相连的图标
    :param pos1: 第一个要移除的图标的位置元组(x, y)
    :param pos2: 第二个要移除的图标的位置元组(x, y)
    :return: None
    """
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Remove the icons by replacing them with empty spaces
    self.board[y1][x1] = ' '
    self.board[y2][x2] = ' '
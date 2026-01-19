def _check_five_in_a_row(self, row, col, direction):
    """
    检查从给定单元格开始，在给定方向（水平、垂直、对角线）上是否有五个连续的同一玩家的符号。
    计算从给定单元格开始在该方向上的连续符号数量。
    :param row: int, 给定单元格的行
    :param col: int, 给定单元格的列
    :param direction: tuple, (int, int)，命名为 (dx, dy)。行和列将分别加上若干 dx 和 dy。
    :return: 如果有五个连续的同一玩家的符号则返回 True，否则返回 False。
    """
    # 获取起始位置的玩家符号
    player = self.board[row][col]
    
    # 如果起始位置为空，则返回 False
    if player is None or player == '':
        return False
    
    dx, dy = direction
    count = 1  # 从当前位置开始计数为1
    
    # 向正方向检查
    current_row, current_col = row + dx, col + dy
    while (0 <= current_row < len(self.board) and 
           0 <= current_col < len(self.board[0]) and 
           self.board[current_row][current_col] == player):
        count += 1
        current_row += dx
        current_col += dy
    
    # 向反方向检查
    current_row, current_col = row - dx, col - dy
    while (0 <= current_row < len(self.board) and 
           0 <= current_col < len(self.board[0]) and 
           self.board[current_row][current_col] == player):
        count += 1
        current_row -= dx
        current_col -= dy
    
    # 如果连续数量大于等于5，返回 True
    return count >= 5
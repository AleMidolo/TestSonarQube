def check_winner(self):
    """
    检查棋盘上是否在行、列和对角线三个方向上有赢家
    :return: str 或 None，赢家的标记 ('X' 或 'O')，如果还没有赢家则返回 None
    >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
    >>> for move in moves:
    ...     ttt.make_move(move[0], move[1])
    >>> ttt.check_winner()
    'X'
    """
    # Check rows
    for row in self.board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    # Check columns
    for col in range(3):
        if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
            return self.board[0][col]
    
    # Check diagonal (top-left to bottom-right)
    if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
        return self.board[0][0]
    
    # Check diagonal (top-right to bottom-left)
    if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
        return self.board[0][2]
    
    return None
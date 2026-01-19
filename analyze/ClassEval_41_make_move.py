def make_move(self, row, col):
    """
    在给定的行和列上进行移动。
    如果移动有效，它将在棋盘上放置当前玩家的符号，并将当前玩家更改为另一个玩家（如果当前玩家是 'X'，则变为 'O'，反之亦然）。
    :param row: int，此移动的行索引
    :param col: int，列索引
    return: 如果移动有效则返回 True，否则返回 False。
    >>> gomokuGame = GomokuGame(10)
    >>> gomokuGame.make_move(5, 5)
    True
    >>> gomokuGame.make_move(5, 5)
    False
    """
    # 检查行和列索引是否在有效范围内
    if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
        return False
    
    # 检查该位置是否已经被占用
    if self.board[row][col] is not None and self.board[row][col] != '':
        return False
    
    # 放置当前玩家的符号
    self.board[row][col] = self.current_player
    
    # 切换到另一个玩家
    if self.current_player == 'X':
        self.current_player = 'O'
    else:
        self.current_player = 'X'
    
    return True
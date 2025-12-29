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
    for row in self.board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
            return self.board[0][col]
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
        return self.board[0][0]
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
        return self.board[0][2]
    return None
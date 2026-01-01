def make_move(self, row, col):
    """
        在棋盘上指定位置放置当前玩家的标记并切换标记。
        :param row: int, 位置的行索引
        :param col: int, 位置的列索引
        :return: bool, 表示移动是否成功
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """
    if self.board[row][col] == ' ':
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True
    return False
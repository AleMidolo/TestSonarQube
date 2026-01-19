def _check_five_in_a_row(self, row, col, direction):
    """
        检查从给定单元格开始，在给定方向（水平、垂直、对角线）上是否有五个连续的同一玩家的符号。
        计算从给定单元格开始在该方向上的连续符号数量。
        :param row: int, 给定单元格的行
        :param col: int, 给定单元格的列
        :param direction: tuple, (int, int)，命名为 (dx, dy)。行和列将分别加上若干 dx 和 dy。
        :return: 如果有五个连续的同一玩家的符号则返回 True，否则返回 False。
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame._check_five_in_a_row(5, 1, (0, 1))
        True
        >>> gomokuGame._check_five_in_a_row(5, 1, (1, 1))
        False
        """
    dx, dy = direction
    count = 0
    for i in range(5):
        new_row = row + i * dx
        new_col = col + i * dy
        if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
            if self.board[new_row][new_col] == self.board[row][col]:
                count += 1
            else:
                break
        else:
            break
    return count == 5
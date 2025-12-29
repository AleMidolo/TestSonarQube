def check_winner(self):
    """
        通过检查所有方向（水平、垂直、对角线）中是否有五个连在一起的棋子来判断是否有赢家。
        返回：如果有赢家，则返回获胜玩家的符号（'X' 或 'O'），否则返回 None。
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame.check_winner()
        'X'
        """
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for row in range(self.board_size):
        for col in range(self.board_size):
            if self.board[row][col] != ' ':
                for direction in directions:
                    if self._check_five_in_a_row(row, col, direction):
                        return self.board[row][col]
    return None
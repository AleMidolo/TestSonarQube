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
    # Check all positions on the board
    for row in range(self.size):
        for col in range(self.size):
            piece = self.board[row][col]
            if piece is None:
                continue
            
            # Check horizontal (right)
            if col + 4 < self.size:
                if all(self.board[row][col + i] == piece for i in range(5)):
                    return piece
            
            # Check vertical (down)
            if row + 4 < self.size:
                if all(self.board[row + i][col] == piece for i in range(5)):
                    return piece
            
            # Check diagonal (down-right)
            if row + 4 < self.size and col + 4 < self.size:
                if all(self.board[row + i][col + i] == piece for i in range(5)):
                    return piece
            
            # Check diagonal (down-left)
            if row + 4 < self.size and col - 4 >= 0:
                if all(self.board[row + i][col - i] == piece for i in range(5)):
                    return piece
    
    return None
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
    # 检查所有四个方向：水平、垂直、两个对角线
    directions = [
        (0, 1),   # 水平
        (1, 0),   # 垂直
        (1, 1),   # 主对角线
        (1, -1)   # 副对角线
    ]
    
    # 遍历棋盘上的每个位置
    for row in range(self.board_size):
        for col in range(self.board_size):
            # 如果当前位置为空，跳过
            if self.board[row][col] is None:
                continue
            
            current_player = self.board[row][col]
            
            # 检查每个方向
            for dr, dc in directions:
                count = 1  # 当前位置已经有一个棋子
                
                # 向正方向检查
                r, c = row + dr, col + dc
                while (0 <= r < self.board_size and 
                       0 <= c < self.board_size and 
                       self.board[r][c] == current_player):
                    count += 1
                    r += dr
                    c += dc
                
                # 向反方向检查
                r, c = row - dr, col - dc
                while (0 <= r < self.board_size and 
                       0 <= c < self.board_size and 
                       self.board[r][c] == current_player):
                    count += 1
                    r -= dr
                    c -= dc
                
                # 如果连续5个或以上，返回获胜者
                if count >= 5:
                    return current_player
    
    return None
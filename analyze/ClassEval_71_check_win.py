def check_win(self):
    """
    检查游戏是否获胜。当所有箱子都放置在目标位置时，游戏获胜。
    并更新 self.is_game_over 的值。
    :return self.is_game_over: 如果所有箱子都放置在目标位置，则返回 True，否则返回 False。
    >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
    >>> game.check_win()
    """
    # 检查是否所有箱子都在目标位置上
    # 遍历地图，查找是否还有未放置在目标位置的箱子
    for row in self.board:
        for cell in row:
            # 如果还存在箱子(X)未在目标位置，则游戏未获胜
            if cell == 'X':
                self.is_game_over = False
                return self.is_game_over
    
    # 如果没有找到任何箱子(X)，说明所有箱子都已放置在目标位置
    self.is_game_over = True
    return self.is_game_over
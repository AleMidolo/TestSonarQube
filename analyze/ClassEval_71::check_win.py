def check_win(self):
    """
        检查游戏是否获胜。当所有箱子都放置在目标位置时，游戏获胜。
        并更新 self.is_game_over 的值。
        :return self.is_game_over: 如果所有箱子都放置在目标位置，则返回 True，否则返回 False。
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
    for box in self.boxes:
        if box not in self.targets:
            self.is_game_over = False
            return False
    self.is_game_over = True
    return True
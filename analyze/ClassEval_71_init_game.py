def init_game(self):
    """
        通过根据地图设置玩家、目标和箱子的位置来初始化游戏。
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.targets
        [(3, 3)]
        >>> game.boxes
        [(2, 2)]
        >>> game.player_row
        1
        >>> game.player_col
        1
        """
    for row_idx, row in enumerate(self.map):
        for col_idx, char in enumerate(row):
            if char == 'O':
                self.player_row = row_idx
                self.player_col = col_idx
            elif char == 'G':
                self.targets.append((row_idx, col_idx))
                self.target_count += 1
            elif char == 'X':
                self.boxes.append((row_idx, col_idx))
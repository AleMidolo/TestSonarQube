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
    for i, row in enumerate(self.map):
        for j, char in enumerate(row):
            if char == 'O':
                self.player_row = i
                self.player_col = j
            elif char == 'G':
                self.targets.append((i, j))
                self.target_count += 1
            elif char == 'X':
                self.boxes.append((i, j))
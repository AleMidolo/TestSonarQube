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
    for r in range(len(self.map)):
        for c in range(len(self.map[r])):
            if self.map[r][c] == 'O':
                self.player_row, self.player_col = (r, c)
            elif self.map[r][c] == 'G':
                self.targets.append((r, c))
                self.target_count += 1
            elif self.map[r][c] == 'X':
                self.boxes.append((r, c))
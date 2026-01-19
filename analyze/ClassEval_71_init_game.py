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
    self.targets = []
    self.boxes = []
    self.player_row = None
    self.player_col = None
    
    for row in range(len(self.map)):
        for col in range(len(self.map[row])):
            cell = self.map[row][col]
            if cell == 'O':  # 玩家位置
                self.player_row = row
                self.player_col = col
            elif cell == 'X':  # 箱子位置
                self.boxes.append((row, col))
            elif cell == 'G':  # 目标位置
                self.targets.append((row, col))
def move(self, direction):
    """
    根据指定方向移动玩家并检查游戏是否获胜。
    :param direction: str，玩家移动的方向。
        它可以是 'w'、's'、'a' 或 'd'，分别表示上、下、左或右。

    :return: 如果游戏获胜则返回 True，否则返回 False。
    >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
    >>> game.print_map()
    # # # # # 
    # O     #
    #   X   #
    #     G #
    # # # # #
    >>> game.move('d')
    False
    >>> game.move('s')   
    False
    >>> game.move('a')   
    False
    >>> game.move('s') 
    False
    >>> game.move('d') 
    True
    """
    direction_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    if direction not in direction_map:
        return False
    delta_row, delta_col = direction_map[direction]
    new_player_row = self.player_row + delta_row
    new_player_col = self.player_col + delta_col
    if self.map[new_player_row][new_player_col] == '#':
        return False
    if self.map[new_player_row][new_player_col] == ' ' or self.map[new_player_row][new_player_col] == 'G':
        self.player_row = new_player_row
        self.player_col = new_player_col
    elif self.map[new_player_row][new_player_col] == 'X':
        box_new_row = new_player_row + delta_row
        box_new_col = new_player_col + delta_col
        if self.map[box_new_row][box_new_col] in [' ', 'G']:
            self.boxes.remove((new_player_row, new_player_col))
            if self.map[box_new_row][box_new_col] == 'G':
                self.boxes.append((box_new_row, box_new_col))
            else:
                self.boxes.append((box_new_row, box_new_col))
            self.player_row = new_player_row
            self.player_col = new_player_col
    return self.check_win()
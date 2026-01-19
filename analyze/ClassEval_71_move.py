def move(self, direction):
    """
    根据指定方向移动玩家并检查游戏是否获胜。
    :param direction: str，玩家移动的方向。
        它可以是 'w'、's'、'a' 或 'd'，分别表示上、下、左或右。

    :return: 如果游戏获胜则返回 True，否则返回 False。
    """
    # 定义方向映射
    directions = {
        'w': (-1, 0),  # 上
        's': (1, 0),   # 下
        'a': (0, -1),  # 左
        'd': (0, 1)    # 右
    }
    
    if direction not in directions:
        return False
    
    # 找到玩家当前位置
    player_row, player_col = None, None
    for i in range(len(self.map)):
        for j in range(len(self.map[i])):
            if self.map[i][j] == 'O':
                player_row, player_col = i, j
                break
        if player_row is not None:
            break
    
    # 计算新位置
    dr, dc = directions[direction]
    new_row = player_row + dr
    new_col = player_col + dc
    
    # 检查新位置是否有效
    if new_row < 0 or new_row >= len(self.map) or new_col < 0 or new_col >= len(self.map[0]):
        return False
    
    next_cell = self.map[new_row][new_col]
    
    # 如果是墙，不能移动
    if next_cell == '#':
        return False
    
    # 如果是空地或目标点，直接移动
    if next_cell == ' ' or next_cell == 'G':
        self.map[player_row] = self.map[player_row][:player_col] + ' ' + self.map[player_row][player_col + 1:]
        self.map[new_row] = self.map[new_row][:new_col] + 'O' + self.map[new_row][new_col + 1:]
        
        # 检查是否获胜（玩家到达目标点）
        if next_cell == 'G':
            return True
    
    # 如果是箱子，尝试推动箱子
    elif next_cell == 'X':
        box_new_row = new_row + dr
        box_new_col = new_col + dc
        
        # 检查箱子的新位置是否有效
        if box_new_row < 0 or box_new_row >= len(self.map) or box_new_col < 0 or box_new_col >= len(self.map[0]):
            return False
        
        box_next_cell = self.map[box_new_row][box_new_col]
        
        # 箱子只能推到空地或目标点
        if box_next_cell == ' ' or box_next_cell == 'G':
            # 移动箱子
            self.map[box_new_row] = self.map[box_new_row][:box_new_col] + 'X' + self.map[box_new_row][box_new_col + 1:]
            # 移动玩家到箱子原来的位置
            self.map[new_row] = self.map[new_row][:new_col] + 'O' + self.map[new_row][new_col + 1:]
            # 清空玩家原来的位置
            self.map[player_row] = self.map[player_row][:player_col] + ' ' + self.map[player_row][player_col + 1:]
            
            # 检查是否获胜（箱子到达目标点）
            if box_next_cell == 'G':
                return True
        else:
            return False
    
    return False
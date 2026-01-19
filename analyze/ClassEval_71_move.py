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
    
    # 获取方向偏移量
    dy, dx = directions[direction]
    
    # 找到玩家当前位置
    player_y, player_x = None, None
    for i in range(len(self.map)):
        for j in range(len(self.map[i])):
            if self.map[i][j] == 'O':
                player_y, player_x = i, j
                break
        if player_y is not None:
            break
    
    # 计算新位置
    new_y = player_y + dy
    new_x = player_x + dx
    
    # 检查新位置是否越界
    if new_y < 0 or new_y >= len(self.map) or new_x < 0 or new_x >= len(self.map[0]):
        return False
    
    # 检查新位置的内容
    target = self.map[new_y][new_x]
    
    # 如果是墙，不能移动
    if target == '#':
        return False
    
    # 如果是空地或目标点，直接移动
    if target == ' ' or target == 'G':
        self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x + 1:]
        self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x + 1:]
        return False
    
    # 如果是箱子，尝试推动箱子
    if target == 'X':
        # 计算箱子的新位置
        box_new_y = new_y + dy
        box_new_x = new_x + dx
        
        # 检查箱子新位置是否越界
        if box_new_y < 0 or box_new_y >= len(self.map) or box_new_x < 0 or box_new_x >= len(self.map[0]):
            return False
        
        box_target = self.map[box_new_y][box_new_x]
        
        # 箱子只能推到空地或目标点
        if box_target == ' ' or box_target == 'G':
            # 移动玩家
            self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x + 1:]
            self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x + 1:]
            
            # 移动箱子
            self.map[box_new_y] = self.map[box_new_y][:box_new_x] + 'X' + self.map[box_new_y][box_new_x + 1:]
            
            # 检查是否获胜（箱子是否在目标点上）
            if box_target == 'G':
                return True
        else:
            return False
    
    return False
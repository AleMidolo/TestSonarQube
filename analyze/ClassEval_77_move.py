def move(self, direction):
    """
    以指定方向移动蛇。如果蛇头的新位置等于食物的位置，则吃掉食物；如果蛇头的位置等于其身体的位置，则重新开始，否则长度加一。
    :param direction: 元组，表示移动的方向 (x, y)。
    :return: None
    >>> snake.move((1,1))
    self.length = 1
    self.positions = [(51, 51), (50, 50)]
    self.score = 10
    """
    # 计算新的蛇头位置
    current_head = self.positions[0]
    new_head = (current_head[0] + direction[0], current_head[1] + direction[1])
    
    # 检查新位置是否撞到自己的身体
    if new_head in self.positions[1:]:
        # 重新开始游戏
        self.reset()
        return
    
    # 将新头部添加到位置列表的开头
    self.positions.insert(0, new_head)
    
    # 检查是否吃到食物
    if hasattr(self, 'food') and new_head == self.food:
        # 吃到食物，增加长度和分数
        self.length += 1
        self.score += 10
        # 生成新的食物位置
        self.generate_food()
    else:
        # 没有吃到食物，移除尾部保持长度不变
        self.positions.pop()
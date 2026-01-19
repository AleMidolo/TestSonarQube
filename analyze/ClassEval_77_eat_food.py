def eat_food(self):
    """
    增加蛇的长度1，并将分数增加100。随机生成一个新的食物位置，但
    不要放在蛇身上。
    :return: None
    >>> snake = Snake(100, 100, 1, (51, 51))
    >>> snake.move((1,1))
    >>> snake.eat_food()
    self.length = 2
    self.score = 10
    """
    import random
    
    # 增加蛇的长度
    self.length += 1
    
    # 增加分数100
    self.score += 100
    
    # 随机生成新的食物位置，确保不在蛇身上
    while True:
        new_food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        if new_food not in self.body:
            self.food = new_food
            break
def random_food_position(self):
    """
    随机生成一个新的食物位置，但不要放在蛇身上。
    :return: None，改变食物位置
    """
    import random
    
    while True:
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        
        # 检查这个位置是否在蛇身上
        if (x, y) not in self.snake_body:
            self.food_position = (x, y)
            break
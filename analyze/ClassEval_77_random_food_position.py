def random_food_position(self):
    """
    随机生成一个新的食物位置，但不要放在蛇身上。
    :return: None，改变食物位置
    """
    import random
    
    while True:
        # 生成随机位置
        new_food_x = random.randint(0, self.width - 1)
        new_food_y = random.randint(0, self.height - 1)
        
        # 检查新位置是否在蛇身上
        if (new_food_x, new_food_y) not in self.snake_body:
            self.food_position = (new_food_x, new_food_y)
            break
def random_food_position(self):
    """
        随机生成一个新的食物位置，但不要放在蛇身上。
        :return: None，改变食物位置
        """
    while True:
        x = random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
        y = random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
        self.food_position = (x, y)
        if self.food_position not in self.positions:
            break
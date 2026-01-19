def reset(self):
    """
    重置蛇的状态为初始状态。将长度设置为1，蛇头位置设置为((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))，分数设置为0，并随机生成新的食物位置。
    :return: None
    >>> snake = Snake(100, 100, 1, (51, 51))
    >>> snake.reset()
    self.length = 1
    self.positions = [(50, 50)]
    self.score = 0
    self.random_food_position()
    """
    self.length = 1
    self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    self.score = 0
    self.random_food_position()
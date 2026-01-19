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
    self.length += 1
    self.score += 100
    self.random_food_position()
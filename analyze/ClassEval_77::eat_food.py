def eat_food(self):
    """
        Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but do not place it on the snake.
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
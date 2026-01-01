def reset(self):
    """
        Reset the snake's state to the initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate a new food position.
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.reset()
        self.length = 1
        self.positions = [(50, 50)]
        self.score = 0
        self.random_food_position()
        """
    self.length = 1
    self.positions = [(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2)]
    self.score = 0
    self.random_food_position()
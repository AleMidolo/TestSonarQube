def eat_food(self):
    """
    Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but
    don't place it on the snake.
    :return: None
    >>> snake = Snake(100, 100, 1, (51, 51))
    >>> snake.move((1,1))
    >>> snake.eat_food()
    self.length = 2
    self.score = 10
    """
    import random
    
    # Increase length and score
    self.length += 1
    self.score += 100
    
    # Generate new food position that's not on the snake
    while True:
        new_food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        if new_food not in self.body:
            self.food = new_food
            break
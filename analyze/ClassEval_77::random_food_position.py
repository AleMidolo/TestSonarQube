def random_food_position(self):
    """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
    while True:
        x = random.randrange(0, self.SCREEN_WIDTH, self.BLOCK_SIZE)
        y = random.randrange(0, self.SCREEN_HEIGHT, self.BLOCK_SIZE)
        new_food_position = (x, y)
        if new_food_position not in self.positions:
            self.food_position = new_food_position
            break
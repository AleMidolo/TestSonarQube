def random_food_position(self):
    """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
    while True:
        new_food = (random.randint(0, (self.SCREEN_WIDTH - self.BLOCK_SIZE) // self.BLOCK_SIZE) * self.BLOCK_SIZE, random.randint(0, (self.SCREEN_HEIGHT - self.BLOCK_SIZE) // self.BLOCK_SIZE) * self.BLOCK_SIZE)
        if new_food not in self.positions:
            self.food_position = new_food
            break
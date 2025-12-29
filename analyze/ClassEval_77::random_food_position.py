def random_food_position(self):
    """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
    while True:
        x = random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
        y = random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
        self.food_position = (x, y)
        if self.food_position not in self.positions:
            break
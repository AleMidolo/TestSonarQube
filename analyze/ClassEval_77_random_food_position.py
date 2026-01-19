def random_food_position(self):
    """
    Randomly generate a new food position, but don't place it on the snake.
    :return: None, Change the food position
    """
    import random
    
    while True:
        # Generate random x and y coordinates within the game boundaries
        new_x = random.randint(0, self.width - 1)
        new_y = random.randint(0, self.height - 1)
        new_position = (new_x, new_y)
        
        # Check if the new position is not on the snake
        if new_position not in self.snake:
            self.food = new_position
            break
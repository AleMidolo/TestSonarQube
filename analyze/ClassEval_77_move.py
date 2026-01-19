def move(self, direction):
    """
    Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
    :param direction: tuple, representing the direction of movement (x, y).
    :return: None
    >>> snake.move((1,1))
    self.length = 1
    self.positions = [(51, 51), (50, 50)]
    self.score = 10
    """
    # Calculate new head position
    current_head = self.positions[0]
    new_head = (current_head[0] + direction[0], current_head[1] + direction[1])
    
    # Check if new head position collides with body
    if new_head in self.positions[1:]:
        # Start over - reset the snake
        self.length = 1
        self.positions = [self.positions[0]]
        self.score = 0
        return
    
    # Add new head position
    self.positions.insert(0, new_head)
    
    # Check if snake ate food
    if hasattr(self, 'food') and new_head == self.food:
        # Eat the food - increase length and score
        self.length += 1
        self.score += 10
        # Generate new food position (assuming there's a method for this)
        if hasattr(self, 'generate_food'):
            self.generate_food()
    else:
        # No food eaten - remove tail to maintain length
        if len(self.positions) > self.length:
            self.positions.pop()
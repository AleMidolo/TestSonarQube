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
    # Check if new head position is at food location
    elif hasattr(self, 'food') and new_head == self.food:
        # Eat the food
        self.positions.insert(0, new_head)
        self.length += 1
        self.score += 10
        # Generate new food position (if there's a method for it)
        if hasattr(self, 'generate_food'):
            self.generate_food()
    else:
        # Normal move - add new head and remove tail
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
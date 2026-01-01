def move(self, direction):
    """
        Move the snake in the specified direction. If the new position of the snake's head equals the food position, eat the food; 
        if the new position of the snake's head equals any position of its body, reset; otherwise, add to its own length.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        >>> snake.move((1,1))
        self.length = 1
        self.positions = [(51, 51), (50, 50)]
        self.score = 10
        """
    new_head = (self.positions[0][0] + direction[0] * self.BLOCK_SIZE, self.positions[0][1] + direction[1] * self.BLOCK_SIZE)
    if new_head == self.food_position:
        self.eat_food()
    elif new_head in self.positions:
        self.reset()
    else:
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
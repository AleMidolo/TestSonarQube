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
    head_x, head_y = self.positions[0]
    dx, dy = direction
    new_head = (head_x + dx * self.BLOCK_SIZE, head_y + dy * self.BLOCK_SIZE)
    if new_head in self.positions:
        self.reset()
        return
    self.positions.insert(0, new_head)
    if new_head == self.food_position:
        self.eat_food()
    elif len(self.positions) > self.length:
        self.positions.pop()
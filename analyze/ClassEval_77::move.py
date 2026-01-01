def move(self, direction):
    """
        以指定方向移动蛇。如果蛇头的新位置等于食物的位置，则吃掉食物；如果蛇头的位置等于其身体的位置，则重新开始，否则长度加一。
        :param direction: 元组，表示移动的方向 (x, y)。
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
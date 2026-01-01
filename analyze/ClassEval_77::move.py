def move(self, direction):
    """
        以指定方向移动蛇。如果蛇头的新位置等于食物的位置，则吃掉食物；如果蛇头的位置等于其身体的位置，则重新开始，否则长度加一。
        :param direction: 元组，表示移动的方向 (x, y)。
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
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
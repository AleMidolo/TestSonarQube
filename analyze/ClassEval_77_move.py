def move(self, direction):
    """
        Muovi il serpente nella direzione specificata. Se la nuova posizione della testa del serpente è uguale alla posizione del cibo, allora mangia il cibo; se la posizione della testa del serpente è uguale alla posizione del suo corpo, allora ricomincia, altrimenti aumenta la sua lunghezza di uno.
        :param direction: tupla, che rappresenta la direzione di movimento (x, y).
        :return: None
        >>> snake.move((1,1))
        self.length = 1
        self.positions = [(51, 51), (50, 50)]
        self.score = 10
        """
    head_x, head_y = self.positions[0]
    new_head = (head_x + direction[0] * self.BLOCK_SIZE, head_y + direction[1] * self.BLOCK_SIZE)
    if new_head in self.positions:
        self.reset()
        return
    self.positions.insert(0, new_head)
    if new_head == self.food_position:
        self.eat_food()
    elif len(self.positions) > self.length:
        self.positions.pop()
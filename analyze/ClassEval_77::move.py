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
    new_head = (self.positions[0][0] + direction[0] * self.BLOCK_SIZE, self.positions[0][1] + direction[1] * self.BLOCK_SIZE)
    if new_head == self.food_position:
        self.eat_food()
    elif new_head in self.positions:
        self.reset()
    else:
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
def move(self, direction):
    """
        Mueve la serpiente en la dirección especificada. Si la nueva posición de la cabeza de la serpiente es igual a la posición de la comida, entonces come la comida; Si la posición de la cabeza de la serpiente es igual a la posición de su cuerpo, entonces comienza de nuevo, de lo contrario, su propia longitud más uno.
        :param direction: tupla, que representa la dirección del movimiento (x, y).
        :return: Ninguno
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
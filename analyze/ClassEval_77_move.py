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
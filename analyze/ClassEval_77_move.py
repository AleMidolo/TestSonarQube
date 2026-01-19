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
    # Calcular la nueva posición de la cabeza
    current_head = self.positions[0]
    new_head = (current_head[0] + direction[0], current_head[1] + direction[1])
    
    # Verificar si la nueva posición coincide con la comida
    if new_head == self.food_position:
        # Come la comida: aumenta longitud y puntuación
        self.positions.insert(0, new_head)
        self.length += 1
        self.score += 10
        # Generar nueva posición de comida
        self.generate_food()
    # Verificar si la nueva posición coincide con el cuerpo (colisión)
    elif new_head in self.positions:
        # Reiniciar el juego
        self.reset()
    else:
        # Movimiento normal: agregar nueva cabeza y quitar la cola
        self.positions.insert(0, new_head)
        self.positions.pop()
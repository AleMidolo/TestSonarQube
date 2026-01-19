def eat_food(self):
    """
    Aumenta la longitud de la serpiente en 1 y aumenta la puntuación en 100. Genera aleatoriamente una nueva posición de comida, pero
    no la coloca sobre la serpiente.
    :return: None
    >>> snake = Snake(100, 100, 1, (51, 51))
    >>> snake.move((1,1))
    >>> snake.eat_food()
    self.length = 2
    self.score = 10
    """
    import random
    
    # Aumenta la longitud de la serpiente en 1
    self.length += 1
    
    # Aumenta la puntuación en 100
    self.score += 100
    
    # Genera una nueva posición de comida que no esté sobre la serpiente
    while True:
        new_food_x = random.randint(0, self.width - 1)
        new_food_y = random.randint(0, self.height - 1)
        new_food_pos = (new_food_x, new_food_y)
        
        # Verifica que la nueva posición no esté en el cuerpo de la serpiente
        if new_food_pos not in self.body:
            self.food = new_food_pos
            break
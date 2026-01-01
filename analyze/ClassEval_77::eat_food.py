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
    self.length += 1
    self.score += 100
    self.random_food_position()
def reset(self):
    """
    Restablece la serpiente a su estado inicial. Establece la longitud en 1, la posición de la cabeza de la serpiente en ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), la puntuación en 0 y genera aleatoriamente una nueva posición de comida.
    :return: None
    >>> snake = Snake(100, 100, 1, (51, 51))
    >>> snake.reset()
    self.length = 1
    self.positions = [(50, 50)]
    self.score = 0
    self.random_food_position()
    """
    self.length = 1
    self.positions = [(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)]
    self.score = 0
    self.random_food_position()
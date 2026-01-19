def reset(self):
    """
    Ripristina il serpente al suo stato iniziale. Imposta la lunghezza a 1, la posizione della testa del serpente a ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), il punteggio a 0 e genera casualmente una nuova posizione per il cibo.
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
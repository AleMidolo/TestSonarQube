def eat_food(self):
    """
        Aumenta la lunghezza del serpente di 1 e aumenta il punteggio di 100. Genera casualmente una nuova posizione per il cibo, ma
        non posizionarla sul serpente.
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
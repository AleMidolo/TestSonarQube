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
    import random
    
    # Aumenta la lunghezza del serpente di 1
    self.length += 1
    
    # Aumenta il punteggio di 100
    self.score += 100
    
    # Genera una nuova posizione per il cibo che non sia sul serpente
    while True:
        new_food_x = random.randint(0, self.width - 1)
        new_food_y = random.randint(0, self.height - 1)
        new_food_pos = (new_food_x, new_food_y)
        
        # Verifica che la nuova posizione non sia sul corpo del serpente
        if new_food_pos not in self.body:
            self.food = new_food_pos
            break
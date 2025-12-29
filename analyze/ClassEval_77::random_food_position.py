def random_food_position(self):
    """
        Genera casualmente una nuova posizione per il cibo, ma non posizionarla sul serpente.
        :return: None, Cambia la posizione del cibo
        """
    while True:
        x = random.randrange(0, self.SCREEN_WIDTH, self.BLOCK_SIZE)
        y = random.randrange(0, self.SCREEN_HEIGHT, self.BLOCK_SIZE)
        new_position = (x, y)
        if new_position not in self.positions:
            self.food_position = new_position
            break
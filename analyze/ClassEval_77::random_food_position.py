def random_food_position(self):
    """
        Genera casualmente una nuova posizione per il cibo, ma non posizionarla sul serpente.
        :return: None, Cambia la posizione del cibo
        """
    while True:
        x = random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
        y = random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
        self.food_position = (x, y)
        if self.food_position not in self.positions:
            break
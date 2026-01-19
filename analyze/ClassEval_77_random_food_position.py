def random_food_position(self):
    """
        Genera aleatoriamente una nueva posición de comida, pero no la coloca sobre la serpiente.
        :return: None, Cambia la posición de la comida
        """
    while True:
        x = random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
        y = random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
        self.food_position = (x, y)
        if self.food_position not in self.positions:
            break
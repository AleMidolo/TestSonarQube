def random_food_position(self):
    """
        Genera aleatoriamente una nueva posición de comida, pero no la coloca sobre la serpiente.
        :return: None, Cambia la posición de la comida
        """
    while True:
        new_food_position = (random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE, random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE)
        if new_food_position not in self.positions:
            self.food_position = new_food_position
            break
def random_food_position(self):
    """
    Genera aleatoriamente una nueva posición de comida, pero no la coloca sobre la serpiente.
    :return: None, Cambia la posición de la comida
    """
    import random
    
    while True:
        # Generar una posición aleatoria para la comida
        new_food_x = random.randint(0, self.width - 1)
        new_food_y = random.randint(0, self.height - 1)
        new_food_position = (new_food_x, new_food_y)
        
        # Verificar que la nueva posición no esté sobre la serpiente
        if new_food_position not in self.snake:
            self.food = new_food_position
            break
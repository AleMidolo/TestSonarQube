def random_food_position(self):
    """
    Genera casualmente una nuova posizione per il cibo, ma non posizionarla sul serpente.
    :return: None, Cambia la posizione del cibo
    """
    import random
    
    while True:
        # Genera una posizione casuale per il cibo
        new_food_x = random.randint(0, self.width - 1)
        new_food_y = random.randint(0, self.height - 1)
        
        # Verifica che la nuova posizione non sia occupata dal serpente
        if (new_food_x, new_food_y) not in self.snake:
            self.food_x = new_food_x
            self.food_y = new_food_y
            break
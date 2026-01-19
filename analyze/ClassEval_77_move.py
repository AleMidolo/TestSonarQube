def move(self, direction):
    """
    Muovi il serpente nella direzione specificata. Se la nuova posizione della testa del serpente è uguale alla posizione del cibo, allora mangia il cibo; se la posizione della testa del serpente è uguale alla posizione del suo corpo, allora ricomincia, altrimenti aumenta la sua lunghezza di uno.
    :param direction: tupla, che rappresenta la direzione di movimento (x, y).
    :return: None
    >>> snake.move((1,1))
    self.length = 1
    self.positions = [(51, 51), (50, 50)]
    self.score = 10
    """
    # Calcola la nuova posizione della testa
    current_head = self.positions[0]
    new_head = (current_head[0] + direction[0], current_head[1] + direction[1])
    
    # Controlla se la nuova posizione coincide con il cibo
    if new_head == self.food:
        # Mangia il cibo: aumenta lunghezza e punteggio
        self.positions.insert(0, new_head)
        self.length += 1
        self.score += 10
        # Genera nuovo cibo (assumendo che esista un metodo per farlo)
        self.generate_food()
    # Controlla se la nuova posizione coincide con il corpo del serpente
    elif new_head in self.positions:
        # Ricomincia il gioco
        self.reset()
    else:
        # Movimento normale: aggiungi nuova testa e rimuovi la coda
        self.positions.insert(0, new_head)
        self.positions.pop()
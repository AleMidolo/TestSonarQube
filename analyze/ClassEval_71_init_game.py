def init_game(self):
    """
    Inicializa el juego estableciendo las posiciones del jugador, los objetivos y las cajas según el mapa.
    >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
    >>> game.targets
    [(3, 3)]
    >>> game.boxes
    [(2, 2)]
    >>> game.player_row
    1
    >>> game.player_col
    1
    """
    self.targets = []
    self.boxes = []
    self.player_row = None
    self.player_col = None
    
    for row in range(len(self.map)):
        for col in range(len(self.map[row])):
            cell = self.map[row][col]
            if cell == 'O':  # Jugador
                self.player_row = row
                self.player_col = col
            elif cell == 'X':  # Caja
                self.boxes.append((row, col))
            elif cell == 'G':  # Objetivo
                self.targets.append((row, col))
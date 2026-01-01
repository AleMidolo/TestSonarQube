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
    for i, row in enumerate(self.map):
        for j, char in enumerate(row):
            if char == 'O':
                self.player_row = i
                self.player_col = j
            elif char == 'G':
                self.targets.append((i, j))
                self.target_count += 1
            elif char == 'X':
                self.boxes.append((i, j))
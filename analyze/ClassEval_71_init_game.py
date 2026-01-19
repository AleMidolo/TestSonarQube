def init_game(self):
    """
    Inizializza il gioco impostando le posizioni del giocatore, degli obiettivi e delle scatole in base alla mappa.
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
    
    for row_idx, row in enumerate(self.map):
        for col_idx, cell in enumerate(row):
            if cell == 'O':  # Player position
                self.player_row = row_idx
                self.player_col = col_idx
            elif cell == 'X':  # Box position
                self.boxes.append((row_idx, col_idx))
            elif cell == 'G':  # Target/Goal position
                self.targets.append((row_idx, col_idx))
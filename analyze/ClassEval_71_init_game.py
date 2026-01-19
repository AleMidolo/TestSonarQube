def init_game(self):
    """
    Initialize the game by setting the positions of the player, targets, and boxes based on the map.
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
            if cell == 'O':  # Player
                self.player_row = row
                self.player_col = col
            elif cell == 'X':  # Box
                self.boxes.append((row, col))
            elif cell == 'G':  # Target
                self.targets.append((row, col))
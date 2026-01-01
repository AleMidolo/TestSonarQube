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
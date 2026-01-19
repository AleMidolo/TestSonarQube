def init_game(self):
    """
    खेल को प्रारंभ करें खिलाड़ी, लक्ष्यों और बक्सों की स्थिति को मानचित्र के आधार पर सेट करके।
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
            
            if cell == 'O':  # Player position
                self.player_row = row
                self.player_col = col
            elif cell == 'X':  # Box position
                self.boxes.append((row, col))
            elif cell == 'G':  # Goal/Target position
                self.targets.append((row, col))
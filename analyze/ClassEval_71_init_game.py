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
    for r in range(len(self.map)):
        for c in range(len(self.map[r])):
            if self.map[r][c] == 'O':
                self.player_row, self.player_col = (r, c)
            elif self.map[r][c] == 'G':
                self.targets.append((r, c))
                self.target_count += 1
            elif self.map[r][c] == 'X':
                self.boxes.append((r, c))
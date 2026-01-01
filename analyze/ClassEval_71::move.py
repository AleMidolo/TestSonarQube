def move(self, direction):
    """
        Muovi il giocatore in base alla direzione specificata e controlla se il gioco è vinto.
        :param direction: str, la direzione del movimento del giocatore. 
            Può essere 'w', 's', 'a' o 'd' che rappresentano rispettivamente su, giù, sinistra o destra.

        :return: True se il gioco è vinto, False altrimenti.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        >>> game.move('d')
        False
        >>> game.move('s')   
        False
        >>> game.move('a')   
        False
        >>> game.move('s') 
        False
        >>> game.move('d') 
        True
        """
    if self.is_game_over:
        return True
    dir_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    if direction not in dir_map:
        return False
    dr, dc = dir_map[direction]
    new_row = self.player_row + dr
    new_col = self.player_col + dc
    if new_row < 0 or new_row >= len(self.map) or new_col < 0 or (new_col >= len(self.map[0])) or (self.map[new_row][new_col] == '#'):
        return False
    box_index = -1
    for i, box in enumerate(self.boxes):
        if box == (new_row, new_col):
            box_index = i
            break
    if box_index != -1:
        box_new_row = new_row + dr
        box_new_col = new_col + dc
        if box_new_row < 0 or box_new_row >= len(self.map) or box_new_col < 0 or (box_new_col >= len(self.map[0])) or (self.map[box_new_row][box_new_col] == '#') or ((box_new_row, box_new_col) in self.boxes):
            return False
        self.boxes[box_index] = (box_new_row, box_new_col)
    self.player_row = new_row
    self.player_col = new_col
    return self.check_win()
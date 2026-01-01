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
    direction_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    if direction not in direction_map:
        return False
    delta_row, delta_col = direction_map[direction]
    new_player_row = self.player_row + delta_row
    new_player_col = self.player_col + delta_col
    if self.map[new_player_row][new_player_col] == '#':
        return False
    if (new_player_row, new_player_col) in self.boxes:
        new_box_row = new_player_row + delta_row
        new_box_col = new_player_col + delta_col
        if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
            return False
        self.boxes.remove((new_player_row, new_player_col))
        self.boxes.append((new_box_row, new_box_col))
    self.player_row = new_player_row
    self.player_col = new_player_col
    return self.check_win()
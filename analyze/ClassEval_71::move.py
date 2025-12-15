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
    direction_map = {
        'w': (-1, 0),  # up
        's': (1, 0),   # down
        'a': (0, -1),  # left
        'd': (0, 1)    # right
    }
    
    if direction not in direction_map:
        return False

    move_row, move_col = direction_map[direction]
    new_player_row = self.player_row + move_row
    new_player_col = self.player_col + move_col

    if self.map[new_player_row][new_player_col] == '#':
        return False  # Wall

    if (new_player_row, new_player_col) in self.boxes:
        new_box_row = new_player_row + move_row
        new_box_col = new_player_col + move_col
        if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
            return False  # Wall or another box

        # Move the box
        box_index = self.boxes.index((new_player_row, new_player_col))
        self.boxes[box_index] = (new_box_row, new_box_col)

    # Move the player
    self.player_row = new_player_row
    self.player_col = new_player_col

    # Check for win condition
    return self.check_win()
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
        return False  # Wall collision

    if self.map[new_player_row][new_player_col] == ' ':
        # Move player to empty space
        self.player_row = new_player_row
        self.player_col = new_player_col
    elif self.map[new_player_row][new_player_col] == 'X':
        # Check if the box can be moved
        box_new_row = new_player_row + move_row
        box_new_col = new_player_col + move_col
        
        if self.map[box_new_row][box_new_col] in [' ', 'G']:
            # Move the box
            self.boxes.remove((new_player_row, new_player_col))
            if self.map[box_new_row][box_new_col] == 'G':
                self.boxes.append((box_new_row, box_new_col))
            else:
                self.boxes.append((box_new_row, box_new_col))
            self.player_row = new_player_row
            self.player_col = new_player_col

    # Check for win condition
    return self.check_win()
def move(self, direction):
    """
    Move the player based on the specified direction and check if the game is won.
    :param direction: str, the direction of the player's movement. 
        It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.

    :return: True if the game is won, False otherwise.
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
    # Define direction mappings
    directions = {
        'w': (-1, 0),  # up
        's': (1, 0),   # down
        'a': (0, -1),  # left
        'd': (0, 1)    # right
    }
    
    if direction not in directions:
        return False
    
    dy, dx = directions[direction]
    
    # Calculate new player position
    new_player_y = self.player_pos[0] + dy
    new_player_x = self.player_pos[1] + dx
    
    # Check if new position is within bounds
    if (new_player_y < 0 or new_player_y >= len(self.map) or 
        new_player_x < 0 or new_player_x >= len(self.map[0])):
        return False
    
    # Check what's at the new position
    target_cell = self.map[new_player_y][new_player_x]
    
    # If it's a wall, can't move
    if target_cell == '#':
        return False
    
    # If it's empty space or goal, just move
    if target_cell == ' ' or target_cell == 'G':
        self.map[self.player_pos[0]][self.player_pos[1]] = ' '
        self.map[new_player_y][new_player_x] = 'O'
        self.player_pos = (new_player_y, new_player_x)
    
    # If it's a box, try to push it
    elif target_cell == 'X':
        # Calculate position behind the box
        box_new_y = new_player_y + dy
        box_new_x = new_player_x + dx
        
        # Check if box can be pushed
        if (box_new_y < 0 or box_new_y >= len(self.map) or 
            box_new_x < 0 or box_new_x >= len(self.map[0])):
            return False
        
        box_target_cell = self.map[box_new_y][box_new_x]
        
        # Box can only be pushed to empty space or goal
        if box_target_cell == ' ' or box_target_cell == 'G':
            # Move the box
            self.map[box_new_y][box_new_x] = 'X'
            # Move the player
            self.map[self.player_pos[0]][self.player_pos[1]] = ' '
            self.map[new_player_y][new_player_x] = 'O'
            self.player_pos = (new_player_y, new_player_x)
            
            # Check if box is on goal
            if box_target_cell == 'G':
                return True
        else:
            # Can't push box (blocked by wall or another box)
            return False
    
    return False
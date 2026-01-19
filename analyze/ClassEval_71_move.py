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
    
    # Find current player position
    player_y, player_x = self.player_pos
    
    # Calculate new position
    new_y = player_y + dy
    new_x = player_x + dx
    
    # Check if new position is valid (within bounds)
    if new_y < 0 or new_y >= len(self.map) or new_x < 0 or new_x >= len(self.map[0]):
        return False
    
    # Check what's at the new position
    target = self.map[new_y][new_x]
    
    # If it's a wall, can't move
    if target == '#':
        return False
    
    # If it's empty space or goal, just move
    if target == ' ' or target == 'G':
        self.map[player_y][player_x] = ' '
        self.map[new_y][new_x] = 'O'
        self.player_pos = (new_y, new_x)
        return self.check_win()
    
    # If it's a box, try to push it
    if target == 'X':
        # Calculate position behind the box
        box_new_y = new_y + dy
        box_new_x = new_x + dx
        
        # Check if box can be pushed
        if box_new_y < 0 or box_new_y >= len(self.map) or box_new_x < 0 or box_new_x >= len(self.map[0]):
            return False
        
        behind_box = self.map[box_new_y][box_new_x]
        
        # Box can only be pushed to empty space or goal
        if behind_box == ' ' or behind_box == 'G':
            # Move the box
            self.map[box_new_y][box_new_x] = 'X'
            # Move the player
            self.map[player_y][player_x] = ' '
            self.map[new_y][new_x] = 'O'
            self.player_pos = (new_y, new_x)
            return self.check_win()
        else:
            # Can't push box (wall or another box in the way)
            return False
    
    return False
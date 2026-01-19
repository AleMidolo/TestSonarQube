def move(self, direction):
    """
    निर्दिष्ट दिशा के आधार पर खिलाड़ी को स्थानांतरित करें और जांचें कि खेल जीता गया है या नहीं।
    :param direction: str, खिलाड़ी की गति की दिशा। 
        यह 'w', 's', 'a', या 'd' हो सकता है जो क्रमशः ऊपर, नीचे, बाएं, या दाएं का प्रतिनिधित्व करता है।

    :return: यदि खेल जीता गया है तो True, अन्यथा False।
    """
    # Direction mappings
    directions = {
        'w': (-1, 0),  # ऊपर (up)
        's': (1, 0),   # नीचे (down)
        'a': (0, -1),  # बाएं (left)
        'd': (0, 1)    # दाएं (right)
    }
    
    if direction not in directions:
        return False
    
    dy, dx = directions[direction]
    
    # Current player position
    player_y, player_x = self.player_pos
    
    # New position for player
    new_y = player_y + dy
    new_x = player_x + dx
    
    # Check if new position is within bounds
    if new_y < 0 or new_y >= len(self.map) or new_x < 0 or new_x >= len(self.map[0]):
        return False
    
    # Check what's at the new position
    target_cell = self.map[new_y][new_x]
    
    # If it's a wall, can't move
    if target_cell == '#':
        return False
    
    # If it's empty space or goal, just move
    if target_cell == ' ' or target_cell == 'G':
        self.map[player_y][player_x] = ' '
        self.map[new_y][new_x] = 'O'
        self.player_pos = (new_y, new_x)
    
    # If it's a box, try to push it
    elif target_cell == 'X':
        # Position where box would move to
        box_new_y = new_y + dy
        box_new_x = new_x + dx
        
        # Check if box's new position is valid
        if box_new_y < 0 or box_new_y >= len(self.map) or box_new_x < 0 or box_new_x >= len(self.map[0]):
            return False
        
        box_target_cell = self.map[box_new_y][box_new_x]
        
        # Box can only be pushed to empty space or goal
        if box_target_cell == ' ' or box_target_cell == 'G':
            # Move the box
            self.map[box_new_y][box_new_x] = 'X'
            # Move the player
            self.map[player_y][player_x] = ' '
            self.map[new_y][new_x] = 'O'
            self.player_pos = (new_y, new_x)
            
            # Check if box is on goal
            if box_target_cell == 'G':
                return True
        else:
            # Can't push box (blocked by wall or another box)
            return False
    
    return False
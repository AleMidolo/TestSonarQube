def move(self, direction):
    """
    निर्दिष्ट दिशा के आधार पर खिलाड़ी को स्थानांतरित करें और जांचें कि खेल जीता गया है या नहीं।
    :param direction: str, खिलाड़ी की गति की दिशा। 
        यह 'w', 's', 'a', या 'd' हो सकता है जो क्रमशः ऊपर, नीचे, बाएं, या दाएं का प्रतिनिधित्व करता है।

    :return: यदि खेल जीता गया है तो True, अन्यथा False।
    """
    # Direction mappings: w=up, s=down, a=left, d=right
    directions = {
        'w': (-1, 0),  # up
        's': (1, 0),   # down
        'a': (0, -1),  # left
        'd': (0, 1)    # right
    }
    
    if direction not in directions:
        return False
    
    dy, dx = directions[direction]
    
    # Find current player position (O)
    player_y, player_x = None, None
    for i in range(len(self.map)):
        for j in range(len(self.map[i])):
            if self.map[i][j] == 'O':
                player_y, player_x = i, j
                break
        if player_y is not None:
            break
    
    # Calculate new position
    new_y = player_y + dy
    new_x = player_x + dx
    
    # Check boundaries
    if new_y < 0 or new_y >= len(self.map) or new_x < 0 or new_x >= len(self.map[0]):
        return False
    
    next_cell = self.map[new_y][new_x]
    
    # If wall, can't move
    if next_cell == '#':
        return False
    
    # If empty space or goal, just move
    if next_cell == ' ' or next_cell == 'G':
        self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x+1:]
        self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x+1:]
        return False
    
    # If box, try to push it
    if next_cell == 'X':
        box_new_y = new_y + dy
        box_new_x = new_x + dx
        
        # Check if box can be pushed
        if box_new_y < 0 or box_new_y >= len(self.map) or box_new_x < 0 or box_new_x >= len(self.map[0]):
            return False
        
        box_next_cell = self.map[box_new_y][box_new_x]
        
        # Box can only be pushed to empty space or goal
        if box_next_cell == ' ' or box_next_cell == 'G':
            # Move player
            self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x+1:]
            self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x+1:]
            
            # Move box
            self.map[box_new_y] = self.map[box_new_y][:box_new_x] + 'X' + self.map[box_new_y][box_new_x+1:]
            
            # Check if box is on goal
            if box_next_cell == 'G':
                return True
            
            return False
        else:
            # Can't push box (wall or another box)
            return False
    
    return False
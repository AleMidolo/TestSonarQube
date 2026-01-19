def has_path(self, pos1, pos2):
    """
    check if there is a path between two icons
    :param pos1: position tuple(x, y) of the first icon
    :param pos2: position tuple(x, y) of the second icon
    :return: True or False ,representing whether there is a path between two icons
    """
    from collections import deque
    
    # If positions are the same, no path needed
    if pos1 == pos2:
        return False
    
    # Check if both positions have the same icon (required for Mahjong Connect)
    x1, y1 = pos1
    x2, y2 = pos2
    
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # If either position is empty, no valid path
    if self.board[y1][x1] is None or self.board[y2][x2] is None:
        return False
    
    # BFS to find path with at most 2 turns (3 line segments)
    rows = len(self.board)
    cols = len(self.board[0])
    
    # Queue stores: (x, y, direction, turns)
    # direction: 0=right, 1=down, 2=left, 3=up, -1=start
    queue = deque([(x1, y1, -1, 0)])
    visited = {}  # (x, y, direction): turns
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # right, down, left, up
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        # Check if we reached the destination
        if (x, y) == pos2:
            return True
        
        # Try all 4 directions
        for dir_idx, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            # Check bounds (can go one step outside the board)
            if -1 <= nx <= cols and -1 <= ny <= rows:
                # Calculate new turn count
                new_turns = turns
                if prev_dir != -1 and prev_dir != dir_idx:
                    new_turns += 1
                
                # Maximum 2 turns allowed (3 line segments)
                if new_turns > 2:
                    continue
                
                # Check if this cell is valid
                # Can pass through empty cells or the destination
                is_valid = False
                if (nx, ny) == pos2:
                    is_valid = True
                elif -1 <= nx < cols and -1 <= ny < rows:
                    if 0 <= nx < cols and 0 <= ny < rows:
                        if self.board[ny][nx] is None or (nx, ny) == pos1:
                            is_valid = True
                    else:
                        # Outside board is considered empty
                        is_valid = True
                
                if is_valid:
                    state = (nx, ny, dir_idx)
                    if state not in visited or visited[state] > new_turns:
                        visited[state] = new_turns
                        queue.append((nx, ny, dir_idx, new_turns))
    
    return False
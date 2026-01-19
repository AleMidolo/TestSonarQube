def has_path(self, pos1, pos2):
    """
    check if there is a path between two icons
    :param pos1: position tuple(x, y) of the first icon
    :param pos2: position tuple(x, y) of the second icon
    :return: True or False ,representing whether there is a path between two icons
    """
    from collections import deque
    
    # If positions are the same, no valid path
    if pos1 == pos2:
        return False
    
    # Check if both positions are valid and have matching icons
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Get board dimensions
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    # Check bounds
    if not (0 <= x1 < cols and 0 <= y1 < rows and 0 <= x2 < cols and 0 <= y2 < rows):
        return False
    
    # Check if icons match (assuming empty cells are None or '')
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # BFS to find path with at most 2 turns
    queue = deque([(x1, y1, -1, -1, 0)])  # (x, y, prev_dx, prev_dy, turns)
    visited = {}  # (x, y, dx, dy) -> turns
    
    while queue:
        x, y, prev_dx, prev_dy, turns = queue.popleft()
        
        # If we reached the destination
        if (x, y) == (x2, y2):
            return True
        
        # If too many turns, skip
        if turns > 2:
            continue
        
        # Try all 4 directions
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            # Check bounds (allow one step outside the board)
            if -1 <= nx <= cols and -1 <= ny <= rows:
                # Calculate new turn count
                new_turns = turns
                if prev_dx != -1 and (dx, dy) != (prev_dx, prev_dy):
                    new_turns += 1
                
                # Skip if too many turns
                if new_turns > 2:
                    continue
                
                # Check if cell is empty or is the destination
                is_empty = (nx < 0 or nx >= cols or ny < 0 or ny >= rows or 
                           self.board[ny][nx] is None or self.board[ny][nx] == '')
                is_dest = (nx, ny) == (x2, y2)
                
                if is_empty or is_dest:
                    state = (nx, ny, dx, dy)
                    if state not in visited or visited[state] > new_turns:
                        visited[state] = new_turns
                        queue.append((nx, ny, dx, dy, new_turns))
    
    return False
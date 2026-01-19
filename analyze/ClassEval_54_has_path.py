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
    
    # Check if both positions are valid and have the same icon
    rows, cols = len(self.board), len(self.board[0]) if self.board else 0
    x1, y1 = pos1
    x2, y2 = pos2
    
    if not (0 <= x1 < cols and 0 <= y1 < rows and 0 <= x2 < cols and 0 <= y2 < rows):
        return False
    
    if self.board[y1][x1] != self.board[y2][x2] or self.board[y1][x1] is None:
        return False
    
    # BFS to find path with at most 2 turns
    queue = deque([(x1, y1, -1, -1, 0)])  # (x, y, prev_dx, prev_dy, turns)
    visited = {}
    visited[(x1, y1, -1, -1)] = 0
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y, prev_dx, prev_dy, turns = queue.popleft()
        
        # If we reached the destination
        if (x, y) == (x2, y2):
            return True
        
        # Try all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Calculate new turn count
            new_turns = turns
            if prev_dx != -1 and (dx, dy) != (prev_dx, prev_dy):
                new_turns += 1
            
            # Can't have more than 2 turns
            if new_turns > 2:
                continue
            
            # Check bounds (can go one step outside the board)
            if not (-1 <= nx <= cols and -1 <= ny <= rows):
                continue
            
            # Check if cell is empty or is the destination
            if (0 <= nx < cols and 0 <= ny < rows):
                if (nx, ny) != (x2, y2) and self.board[ny][nx] is not None:
                    continue
            
            # Check if we've visited this state with fewer or equal turns
            state = (nx, ny, dx, dy)
            if state in visited and visited[state] <= new_turns:
                continue
            
            visited[state] = new_turns
            queue.append((nx, ny, dx, dy, new_turns))
    
    return False
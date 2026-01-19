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
    
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # If either position is empty, no path
    if self.board[y1][x1] is None or self.board[y2][x2] is None:
        return False
    
    # BFS to find path with at most 2 turns (3 line segments)
    # State: (x, y, direction, turns)
    # direction: 0=start, 1=horizontal, 2=vertical
    queue = deque([(x1, y1, 0, 0)])
    visited = set()
    visited.add((x1, y1, 0))
    
    while queue:
        x, y, direction, turns = queue.popleft()
        
        # Try all 4 directions
        for dx, dy, new_dir in [(0, 1, 2), (0, -1, 2), (1, 0, 1), (-1, 0, 1)]:
            nx, ny = x + dx, y + dy
            
            # Check bounds (allow one step outside the board)
            if nx < -1 or nx > cols or ny < -1 or ny > rows:
                continue
            
            # Calculate number of turns
            new_turns = turns
            if direction != 0 and direction != new_dir:
                new_turns += 1
            
            # Maximum 2 turns allowed
            if new_turns > 2:
                continue
            
            # Check if we reached the destination
            if nx == x2 and ny == y2:
                return True
            
            # Check if cell is empty or out of bounds (can pass through)
            can_pass = False
            if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
                can_pass = True
            elif self.board[ny][nx] is None:
                can_pass = True
            
            if can_pass:
                state = (nx, ny, new_dir)
                if state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, new_dir, new_turns))
    
    return False
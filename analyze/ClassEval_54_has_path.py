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
    y1, x1 = pos1
    y2, x2 = pos2
    
    # Boundary checks
    if not (0 <= y1 < len(self.board) and 0 <= x1 < len(self.board[0])):
        return False
    if not (0 <= y2 < len(self.board) and 0 <= x2 < len(self.board[0])):
        return False
    
    # Check if icons match (if they exist)
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # BFS to find path with at most 2 turns (3 line segments)
    # State: (y, x, direction, turns)
    # direction: 0=start, 1=horizontal, 2=vertical
    queue = deque([(y1, x1, 0, 0)])
    visited = set()
    visited.add((y1, x1, 0))
    
    while queue:
        y, x, direction, turns = queue.popleft()
        
        # Try all four directions
        for dy, dx, new_dir in [(0, 1, 1), (0, -1, 1), (1, 0, 2), (-1, 0, 2)]:
            ny, nx = y + dy, x + dx
            
            # Check boundaries (allow one step outside the board)
            if ny < -1 or ny > len(self.board) or nx < -1 or nx > len(self.board[0]):
                continue
            
            # Calculate new turn count
            new_turns = turns
            if direction != 0 and direction != new_dir:
                new_turns += 1
            
            # Maximum 2 turns allowed (3 line segments)
            if new_turns > 2:
                continue
            
            # Check if we reached the destination
            if (ny, nx) == (y2, x2):
                return True
            
            # Check if cell is empty or outside board
            if 0 <= ny < len(self.board) and 0 <= nx < len(self.board[0]):
                if self.board[ny][nx] is not None and (ny, nx) != (y2, x2):
                    continue
            
            # Add to queue if not visited with this state
            state = (ny, nx, new_dir)
            if state not in visited:
                visited.add(state)
                queue.append((ny, nx, new_dir, new_turns))
    
    return False
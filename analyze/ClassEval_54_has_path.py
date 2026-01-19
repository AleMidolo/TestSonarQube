def has_path(self, pos1, pos2):
    """
    controlla se c'è un percorso tra due icone
    :param pos1: tupla di posizione(x, y) della prima icona
    :param pos2: tupla di posizione(x, y) della seconda icona
    :return: True o False, che rappresenta se c'è un percorso tra due icone
    """
    from collections import deque
    
    # Check if positions are the same
    if pos1 == pos2:
        return False
    
    # Check if the tiles have the same value
    x1, y1 = pos1
    x2, y2 = pos2
    
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # BFS to find path with at most 2 turns
    rows = len(self.board)
    cols = len(self.board[0])
    
    # Queue stores: (x, y, direction, turns)
    # direction: 0=right, 1=down, 2=left, 3=up, -1=start
    queue = deque([(x1, y1, -1, 0)])
    visited = set()
    visited.add((x1, y1, -1))
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # right, down, left, up
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        # Try all 4 directions
        for dir_idx, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            # Calculate turns
            new_turns = turns
            if prev_dir != -1 and prev_dir != dir_idx:
                new_turns += 1
            
            # Max 2 turns allowed
            if new_turns > 2:
                continue
            
            # Check if we reached the destination
            if (nx, ny) == (x2, y2):
                return True
            
            # Check bounds (can go one step outside the board)
            if nx < -1 or nx > cols or ny < -1 or ny > rows:
                continue
            
            # Check if position is valid (empty or outside board)
            if 0 <= nx < cols and 0 <= ny < rows:
                if self.board[ny][nx] is not None and (nx, ny) != (x2, y2):
                    continue
            
            # Check if already visited with this direction
            state = (nx, ny, dir_idx)
            if state in visited:
                continue
            
            visited.add(state)
            queue.append((nx, ny, dir_idx, new_turns))
    
    return False
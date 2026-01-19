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
    # State: (x, y, direction, turns)
    # direction: 0=none, 1=horizontal, 2=vertical
    queue = deque([(x1, y1, 0, 0)])
    visited = set()
    visited.add((x1, y1, 0))
    
    rows = len(self.board)
    cols = len(self.board[0])
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        # Try all 4 directions
        for dx, dy, curr_dir in [(0, 1, 2), (0, -1, 2), (1, 0, 1), (-1, 0, 1)]:
            nx, ny = x + dx, y + dy
            
            # Check bounds (allow one step outside the board)
            if nx < -1 or nx > cols or ny < -1 or ny > rows:
                continue
            
            # Calculate new turn count
            new_turns = turns
            if prev_dir != 0 and prev_dir != curr_dir:
                new_turns += 1
            
            # Max 2 turns allowed
            if new_turns > 2:
                continue
            
            # Check if we reached the destination
            if (nx, ny) == (x2, y2):
                return True
            
            # Check if cell is empty or out of bounds (can pass through)
            if 0 <= nx < cols and 0 <= ny < rows:
                if self.board[ny][nx] is not None and (nx, ny) != (x2, y2):
                    continue
            
            # Mark as visited with direction
            state = (nx, ny, curr_dir)
            if state not in visited:
                visited.add(state)
                queue.append((nx, ny, curr_dir, new_turns))
    
    return False
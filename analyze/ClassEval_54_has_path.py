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
    
    # Check if the tiles match
    x1, y1 = pos1
    x2, y2 = pos2
    
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # BFS to find path with at most 2 turns
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    # Queue stores: (x, y, direction, turns)
    # direction: 0=horizontal, 1=vertical, -1=start
    queue = deque([(x1, y1, -1, 0)])
    visited = {}
    visited[(x1, y1, -1)] = 0
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # down, up, right, left
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        # Try all 4 directions
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            # Determine current direction (0=horizontal for left/right, 1=vertical for up/down)
            curr_dir = 0 if i >= 2 else 1
            
            # Calculate new turn count
            new_turns = turns
            if prev_dir != -1 and prev_dir != curr_dir:
                new_turns += 1
            
            # Can't have more than 2 turns
            if new_turns > 2:
                continue
            
            # Check if we reached the destination
            if nx == x2 and ny == y2:
                return True
            
            # Check bounds (allow one step outside the board)
            if nx < -1 or nx > cols or ny < -1 or ny > rows:
                continue
            
            # Check if cell is empty or outside board
            if 0 <= nx < cols and 0 <= ny < rows:
                if self.board[ny][nx] is not None and (nx, ny) != (x2, y2):
                    continue
            
            # Check if we've visited this state with fewer or equal turns
            state = (nx, ny, curr_dir)
            if state in visited and visited[state] <= new_turns:
                continue
            
            visited[state] = new_turns
            queue.append((nx, ny, curr_dir, new_turns))
    
    return False
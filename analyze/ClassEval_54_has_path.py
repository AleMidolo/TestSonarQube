def has_path(self, pos1, pos2):
    """
    verifica si hay un camino entre dos íconos
    :param pos1: tupla de posición (x, y) del primer ícono
    :param pos2: tupla de posición (x, y) del segundo ícono
    :return: True o False, representando si hay un camino entre dos íconos
    """
    from collections import deque
    
    # Si las posiciones son iguales, no hay camino válido
    if pos1 == pos2:
        return False
    
    # Verificar que ambas posiciones tengan el mismo ícono (no vacío)
    x1, y1 = pos1
    x2, y2 = pos2
    
    if not (0 <= x1 < len(self.board) and 0 <= y1 < len(self.board[0])):
        return False
    if not (0 <= x2 < len(self.board) and 0 <= y2 < len(self.board[0])):
        return False
    
    if self.board[x1][y1] != self.board[x2][y2] or self.board[x1][y1] is None or self.board[x1][y1] == '':
        return False
    
    # BFS para encontrar camino con máximo 2 giros
    queue = deque([(x1, y1, -1, -1, 0)])  # (x, y, dir_x, dir_y, turns)
    visited = {}
    
    while queue:
        x, y, prev_dx, prev_dy, turns = queue.popleft()
        
        # Si llegamos al destino con máximo 2 giros
        if (x, y) == pos2:
            return True
        
        # Evitar revisitar con peor o igual número de giros
        state = (x, y, prev_dx, prev_dy)
        if state in visited and visited[state] <= turns:
            continue
        visited[state] = turns
        
        # Si ya usamos 2 giros, solo podemos seguir en la misma dirección
        if turns >= 2 and prev_dx != -1:
            dx, dy = prev_dx, prev_dy
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.board) and 0 <= ny < len(self.board[0]):
                if (nx, ny) == pos2 or self.board[nx][ny] is None or self.board[nx][ny] == '':
                    queue.append((nx, ny, dx, dy, turns))
            continue
        
        # Explorar las 4 direcciones
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            # Verificar límites
            if not (0 <= nx < len(self.board) and 0 <= ny < len(self.board[0])):
                continue
            
            # Solo podemos pasar por celdas vacías o el destino
            if (nx, ny) != pos2 and self.board[nx][ny] is not None and self.board[nx][ny] != '':
                continue
            
            # Calcular número de giros
            new_turns = turns
            if prev_dx != -1 and (dx, dy) != (prev_dx, prev_dy):
                new_turns += 1
            
            # Solo permitir hasta 2 giros
            if new_turns <= 2:
                queue.append((nx, ny, dx, dy, new_turns))
    
    return False
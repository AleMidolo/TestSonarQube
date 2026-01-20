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
    
    # Verificar que ambas posiciones tengan el mismo ícono
    x1, y1 = pos1
    x2, y2 = pos2
    
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # BFS para encontrar un camino con máximo 2 giros
    # Estado: (x, y, dirección, número_de_giros)
    # dirección: 0=ninguna, 1=horizontal, 2=vertical
    
    queue = deque([(x1, y1, 0, 0)])  # (x, y, dirección_previa, giros)
    visited = set()
    visited.add((x1, y1, 0))
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # abajo, arriba, derecha, izquierda
    dir_types = [2, 2, 1, 1]  # vertical, vertical, horizontal, horizontal
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        # Explorar en todas las direcciones
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            curr_dir = dir_types[i]
            
            # Calcular nuevos giros
            new_turns = turns
            if prev_dir != 0 and prev_dir != curr_dir:
                new_turns += 1
            
            # Máximo 2 giros permitidos
            if new_turns > 2:
                continue
            
            # Verificar si llegamos al destino
            if (nx, ny) == (x2, y2):
                return True
            
            # Verificar límites del tablero (permitir ir fuera del tablero en 1 posición)
            if nx < -1 or nx > len(self.board[0]) or ny < -1 or ny > len(self.board):
                continue
            
            # Verificar si la celda está vacía o fuera del tablero
            is_empty = False
            if nx < 0 or nx >= len(self.board[0]) or ny < 0 or ny >= len(self.board):
                is_empty = True
            elif self.board[ny][nx] == '' or self.board[ny][nx] is None:
                is_empty = True
            
            if not is_empty and (nx, ny) != (x2, y2):
                continue
            
            # Evitar visitar el mismo estado
            state = (nx, ny, curr_dir)
            if state not in visited:
                visited.add(state)
                queue.append((nx, ny, curr_dir, new_turns))
    
    return False
def has_path(self, pos1, pos2):
    """
    controlla se c'è un percorso tra due icone
    :param pos1: tupla di posizione(x, y) della prima icona
    :param pos2: tupla di posizione(x, y) della seconda icona
    :return: True o False, che rappresenta se c'è un percorso tra due icone
    """
    from collections import deque
    
    # Se le posizioni sono uguali, non c'è un percorso valido
    if pos1 == pos2:
        return False
    
    # Le icone devono essere dello stesso tipo
    if self.board[pos1[1]][pos1[0]] != self.board[pos2[1]][pos2[0]]:
        return False
    
    # BFS per trovare un percorso con al massimo 2 svolte
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    # Coda: (x, y, direzione, numero_di_svolte)
    # direzione: 0=nessuna, 1=su, 2=giù, 3=sinistra, 4=destra
    queue = deque([(pos1[0], pos1[1], 0, 0)])
    visited = set()
    visited.add((pos1[0], pos1[1], 0))
    
    directions = [(0, -1, 1), (0, 1, 2), (-1, 0, 3), (1, 0, 4)]  # su, giù, sinistra, destra
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        # Se abbiamo raggiunto la destinazione
        if (x, y) == pos2:
            return True
        
        # Se abbiamo già fatto 2 svolte, non possiamo continuare
        if turns > 2:
            continue
        
        # Esplora tutte le direzioni
        for dx, dy, new_dir in directions:
            nx, ny = x + dx, y + dy
            
            # Calcola il numero di svolte
            new_turns = turns
            if prev_dir != 0 and prev_dir != new_dir:
                new_turns += 1
            
            # Se abbiamo superato 2 svolte, salta
            if new_turns > 2:
                continue
            
            # Controlla i limiti del board (con estensione virtuale)
            if -1 <= nx <= cols and -1 <= ny <= rows:
                # Se siamo fuori dal board o la cella è vuota o è la destinazione
                if (nx, ny) == pos2:
                    if new_turns <= 2:
                        return True
                elif (nx == -1 or nx == cols or ny == -1 or ny == rows or 
                      self.board[ny][nx] == '' or self.board[ny][nx] is None):
                    state = (nx, ny, new_dir)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nx, ny, new_dir, new_turns))
    
    return False
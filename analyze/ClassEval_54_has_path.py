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
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Verifica che le icone nelle due posizioni siano uguali
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # Verifica che nessuna delle due posizioni sia vuota
    if self.board[y1][x1] is None or self.board[y2][x2] is None:
        return False
    
    # BFS per trovare un percorso con al massimo 2 svolte
    rows = len(self.board)
    cols = len(self.board[0])
    
    # Coda: (x, y, direzione, numero_di_svolte)
    # direzione: 0=nessuna, 1=orizzontale, 2=verticale
    queue = deque([(x1, y1, 0, 0)])
    visited = set()
    visited.add((x1, y1, 0))
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # destra, sinistra, giù, su
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            # Determina la direzione corrente (1=orizzontale, 2=verticale)
            curr_dir = 1 if dx != 0 else 2
            
            # Calcola il numero di svolte
            new_turns = turns
            if prev_dir != 0 and prev_dir != curr_dir:
                new_turns += 1
            
            # Se abbiamo più di 2 svolte, salta
            if new_turns > 2:
                continue
            
            # Verifica i limiti (può andare fuori dal bordo di 1 cella)
            if nx < -1 or nx > cols or ny < -1 or ny > rows:
                continue
            
            # Se abbiamo raggiunto la destinazione
            if (nx, ny) == (x2, y2):
                return True
            
            # Verifica se la cella è valida (vuota o fuori dal bordo)
            if -1 <= nx < cols and -1 <= ny < rows:
                if 0 <= nx < cols and 0 <= ny < rows:
                    if self.board[ny][nx] is not None and (nx, ny) != (x2, y2):
                        continue
                
                state = (nx, ny, curr_dir)
                if state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, curr_dir, new_turns))
    
    return False
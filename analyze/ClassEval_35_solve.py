def solve(self):
    """
    Utilizza l'algoritmo BFS per trovare un percorso che porti dallo stato iniziale allo stato obiettivo.Mantiene una lista come coda (open_list), inizialmente contenente lo stato iniziale. A ogni iterazione visita ed estrae l'elemento in posizione 0, richiama il metodo get_possible_moves per ottenere tutte le direzioni possibili e, per ciascuna di esse, invoca move per generare i nuovi stati, che vengono poi aggiunti alla coda. Il processo continua finché open_list non è vuota oppure finché non si raggiunge lo stato obiettivo.
    :return path: lista di str, la soluzione allo stato obiettivo.
    >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    >>> eightPuzzle.solve()
    ['destra']
    """
    from collections import deque
    
    # Coda per BFS: ogni elemento è una tupla (stato, percorso)
    open_list = deque([(self.state, [])])
    
    # Set per tenere traccia degli stati visitati
    visited = set()
    visited.add(tuple(map(tuple, self.state)))
    
    while open_list:
        # Estrae l'elemento in posizione 0
        current_state, path = open_list.popleft()
        
        # Salva lo stato corrente
        original_state = self.state
        self.state = current_state
        
        # Verifica se abbiamo raggiunto lo stato obiettivo
        if self.is_goal():
            self.state = original_state
            return path
        
        # Ottiene tutte le mosse possibili
        possible_moves = self.get_possible_moves()
        
        # Per ogni mossa possibile
        for move_direction in possible_moves:
            # Genera il nuovo stato
            new_state = self.move(move_direction)
            
            # Converte lo stato in tupla per poterlo aggiungere al set
            state_tuple = tuple(map(tuple, new_state))
            
            # Se non è stato visitato, aggiungilo alla coda
            if state_tuple not in visited:
                visited.add(state_tuple)
                new_path = path + [move_direction]
                open_list.append((new_state, new_path))
        
        # Ripristina lo stato originale
        self.state = original_state
    
    # Se non trova soluzione
    return []
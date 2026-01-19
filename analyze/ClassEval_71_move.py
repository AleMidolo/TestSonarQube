def move(self, direction):
    """
    Muovi il giocatore in base alla direzione specificata e controlla se il gioco è vinto.
    :param direction: str, la direzione del movimento del giocatore. 
        Può essere 'w', 's', 'a' o 'd' che rappresentano rispettivamente su, giù, sinistra o destra.

    :return: True se il gioco è vinto, False altrimenti.
    """
    # Definisci i movimenti per ogni direzione
    directions = {
        'w': (-1, 0),  # su
        's': (1, 0),   # giù
        'a': (0, -1),  # sinistra
        'd': (0, 1)    # destra
    }
    
    if direction not in directions:
        return False
    
    dy, dx = directions[direction]
    
    # Trova la posizione corrente del giocatore
    player_y, player_x = None, None
    for i in range(len(self.map)):
        for j in range(len(self.map[i])):
            if self.map[i][j] == 'O':
                player_y, player_x = i, j
                break
        if player_y is not None:
            break
    
    # Calcola la nuova posizione
    new_y = player_y + dy
    new_x = player_x + dx
    
    # Controlla se la nuova posizione è valida
    if new_y < 0 or new_y >= len(self.map) or new_x < 0 or new_x >= len(self.map[0]):
        return False
    
    target_cell = self.map[new_y][new_x]
    
    # Se c'è un muro, non muovere
    if target_cell == '#':
        return False
    
    # Se c'è una cassa
    if target_cell == 'X':
        # Calcola la posizione dietro la cassa
        box_new_y = new_y + dy
        box_new_x = new_x + dx
        
        # Controlla se la cassa può essere spinta
        if box_new_y < 0 or box_new_y >= len(self.map) or box_new_x < 0 or box_new_x >= len(self.map[0]):
            return False
        
        box_target = self.map[box_new_y][box_new_x]
        
        # La cassa può essere spinta solo in uno spazio vuoto o sul goal
        if box_target != ' ' and box_target != 'G':
            return False
        
        # Sposta la cassa
        self.map[box_new_y] = self.map[box_new_y][:box_new_x] + 'X' + self.map[box_new_y][box_new_x + 1:]
    
    # Muovi il giocatore
    self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x + 1:]
    self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x + 1:]
    
    # Controlla se il gioco è vinto (la cassa è sul goal)
    for i in range(len(self.map)):
        if 'G' in self.map[i]:
            # Se c'è ancora un goal visibile, il gioco non è vinto
            return False
    
    return True
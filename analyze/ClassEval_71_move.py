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
    
    # Trova la posizione corrente del giocatore (O)
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
    
    next_cell = self.map[new_y][new_x]
    
    # Se c'è un muro, non muovere
    if next_cell == '#':
        return False
    
    # Se c'è una scatola (X)
    if next_cell == 'X':
        # Calcola la posizione dietro la scatola
        box_new_y = new_y + dy
        box_new_x = new_x + dx
        
        # Controlla se la scatola può essere spinta
        if box_new_y < 0 or box_new_y >= len(self.map) or box_new_x < 0 or box_new_x >= len(self.map[0]):
            return False
        
        box_next_cell = self.map[box_new_y][box_new_x]
        
        # La scatola può essere spinta solo su spazio vuoto o goal
        if box_next_cell == ' ' or box_next_cell == 'G':
            # Muovi la scatola
            self.map[box_new_y] = self.map[box_new_y][:box_new_x] + 'X' + self.map[box_new_y][box_new_x + 1:]
            # Muovi il giocatore
            self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x + 1:]
            self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x + 1:]
            
            # Controlla se il gioco è vinto (scatola sul goal)
            if box_next_cell == 'G':
                return True
        else:
            return False
    
    # Se c'è spazio vuoto o goal
    elif next_cell == ' ' or next_cell == 'G':
        # Muovi il giocatore
        self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x + 1:]
        self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x + 1:]
    
    return False
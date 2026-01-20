def move(self, direction):
    """
    Mueve al jugador según la dirección especificada y verifica si el juego ha sido ganado.
    :param direction: str, la dirección del movimiento del jugador. 
        Puede ser 'w', 's', 'a' o 'd' que representan arriba, abajo, izquierda o derecha respectivamente.

    :return: True si el juego ha sido ganado, False en caso contrario.
    """
    # Definir los desplazamientos para cada dirección
    directions = {
        'w': (-1, 0),  # arriba
        's': (1, 0),   # abajo
        'a': (0, -1),  # izquierda
        'd': (0, 1)    # derecha
    }
    
    if direction not in directions:
        return False
    
    dy, dx = directions[direction]
    
    # Encontrar la posición actual del jugador (O)
    player_y, player_x = None, None
    for i in range(len(self.map)):
        for j in range(len(self.map[i])):
            if self.map[i][j] == 'O':
                player_y, player_x = i, j
                break
        if player_y is not None:
            break
    
    # Calcular la nueva posición del jugador
    new_y = player_y + dy
    new_x = player_x + dx
    
    # Verificar límites
    if new_y < 0 or new_y >= len(self.map) or new_x < 0 or new_x >= len(self.map[0]):
        return False
    
    # Verificar qué hay en la nueva posición
    target = self.map[new_y][new_x]
    
    # Si es una pared, no se puede mover
    if target == '#':
        return False
    
    # Si es un espacio vacío, mover al jugador
    if target == ' ':
        self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x + 1:]
        self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x + 1:]
        return False
    
    # Si es la caja (X), intentar empujarla
    if target == 'X':
        # Calcular la posición detrás de la caja
        box_new_y = new_y + dy
        box_new_x = new_x + dx
        
        # Verificar límites para la caja
        if box_new_y < 0 or box_new_y >= len(self.map) or box_new_x < 0 or box_new_x >= len(self.map[0]):
            return False
        
        box_target = self.map[box_new_y][box_new_x]
        
        # La caja solo se puede empujar a un espacio vacío o al objetivo (G)
        if box_target == ' ' or box_target == 'G':
            # Mover la caja
            self.map[box_new_y] = self.map[box_new_y][:box_new_x] + 'X' + self.map[box_new_y][box_new_x + 1:]
            # Mover al jugador a donde estaba la caja
            self.map[new_y] = self.map[new_y][:new_x] + 'O' + self.map[new_y][new_x + 1:]
            # Limpiar la posición anterior del jugador
            self.map[player_y] = self.map[player_y][:player_x] + ' ' + self.map[player_y][player_x + 1:]
            
            # Verificar si la caja llegó al objetivo
            if box_target == 'G':
                return True
            return False
        else:
            # No se puede empujar la caja (hay una pared u otro obstáculo)
            return False
    
    return False
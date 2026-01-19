def is_valid_move(self, pos1, pos2):
    """
    verifica si el movimiento de dos íconos es válido (es decir, las posiciones están dentro del rango del tablero de juego, las dos posiciones no son las mismas, las dos posiciones tienen el mismo ícono y hay un camino válido entre las dos posiciones)
    :param pos1: tupla de posición (x, y) del primer ícono
    :param pos2: tupla de posición (x, y) del segundo ícono
    :return: True o False, representando si el movimiento de los dos íconos es válido
    """
    # Verificar que las posiciones estén dentro del rango del tablero
    if not (0 <= pos1[0] < len(self.board[0]) and 0 <= pos1[1] < len(self.board)):
        return False
    if not (0 <= pos2[0] < len(self.board[0]) and 0 <= pos2[1] < len(self.board)):
        return False
    
    # Verificar que las dos posiciones no sean las mismas
    if pos1 == pos2:
        return False
    
    # Verificar que las dos posiciones tengan el mismo ícono
    icon1 = self.board[pos1[1]][pos1[0]]
    icon2 = self.board[pos2[1]][pos2[0]]
    if icon1 != icon2:
        return False
    
    # Verificar que hay un camino válido entre las dos posiciones
    # En Mahjong Connect, un camino válido tiene como máximo 2 giros (3 segmentos de línea)
    return self.has_valid_path(pos1, pos2)

def has_valid_path(self, pos1, pos2):
    """
    Verifica si existe un camino válido entre dos posiciones con máximo 2 giros
    """
    # Intentar camino directo (0 giros)
    if self.is_direct_path(pos1, pos2):
        return True
    
    # Intentar camino con 1 giro
    # Punto de giro en (pos1[0], pos2[1])
    corner1 = (pos1[0], pos2[1])
    if self.is_direct_path(pos1, corner1) and self.is_direct_path(corner1, pos2):
        return True
    
    # Punto de giro en (pos2[0], pos1[1])
    corner2 = (pos2[0], pos1[1])
    if self.is_direct_path(pos1, corner2) and self.is_direct_path(corner2, pos2):
        return True
    
    # Intentar camino con 2 giros (buscar puntos intermedios)
    for y in range(len(self.board)):
        for x in range(len(self.board[0])):
            mid = (x, y)
            if self.is_direct_path(pos1, mid) and self.has_one_turn_path(mid, pos2):
                return True
    
    return False

def is_direct_path(self, pos1, pos2):
    """
    Verifica si hay un camino directo (horizontal o vertical) sin obstáculos
    """
    if pos1[0] == pos2[0]:  # Vertical
        y_start = min(pos1[1], pos2[1])
        y_end = max(pos1[1], pos2[1])
        for y in range(y_start, y_end + 1):
            if (pos1[0], y) != pos1 and (pos1[0], y) != pos2:
                if self.board[y][pos1[0]] != '':
                    return False
        return True
    elif pos1[1] == pos2[1]:  # Horizontal
        x_start = min(pos1[0], pos2[0])
        x_end = max(pos1[0], pos2[0])
        for x in range(x_start, x_end + 1):
            if (x, pos1[1]) != pos1 and (x, pos1[1]) != pos2:
                if self.board[pos1[1]][x] != '':
                    return False
        return True
    return False

def has_one_turn_path(self, pos1, pos2):
    """
    Verifica si hay un camino con exactamente 1 giro
    """
    corner1 = (pos1[0], pos2[1])
    if self.is_direct_path(pos1, corner1) and self.is_direct_path(corner1, pos2):
        return True
    
    corner2 = (pos2[0], pos1[1])
    if self.is_direct_path(pos1, corner2) and self.is_direct_path(corner2, pos2):
        return True
    
    return False
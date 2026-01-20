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
    # Punto intermedio en (pos1.x, pos2.y)
    mid1 = (pos1[0], pos2[1])
    if self.is_empty_or_target(mid1, pos1, pos2):
        if self.is_direct_path(pos1, mid1) and self.is_direct_path(mid1, pos2):
            return True
    
    # Punto intermedio en (pos2.x, pos1.y)
    mid2 = (pos2[0], pos1[1])
    if self.is_empty_or_target(mid2, pos1, pos2):
        if self.is_direct_path(pos1, mid2) and self.is_direct_path(mid2, pos2):
            return True
    
    # Intentar camino con 2 giros (buscar puntos intermedios en todas las direcciones)
    for y in range(len(self.board)):
        mid = (pos1[0], y)
        if self.is_empty_or_target(mid, pos1, pos2) and self.is_direct_path(pos1, mid):
            mid2 = (pos2[0], y)
            if self.is_empty_or_target(mid2, pos1, pos2):
                if self.is_direct_path(mid, mid2) and self.is_direct_path(mid2, pos2):
                    return True
    
    for x in range(len(self.board[0])):
        mid = (x, pos1[1])
        if self.is_empty_or_target(mid, pos1, pos2) and self.is_direct_path(pos1, mid):
            mid2 = (x, pos2[1])
            if self.is_empty_or_target(mid2, pos1, pos2):
                if self.is_direct_path(mid, mid2) and self.is_direct_path(mid2, pos2):
                    return True
    
    return False

def is_empty_or_target(self, pos, pos1, pos2):
    """Verifica si una posición está vacía o es una de las posiciones objetivo"""
    if pos == pos1 or pos == pos2:
        return True
    if 0 <= pos[0] < len(self.board[0]) and 0 <= pos[1] < len(self.board):
        return self.board[pos[1]][pos[0]] is None or self.board[pos[1]][pos[0]] == ''
    return False

def is_direct_path(self, pos1, pos2):
    """Verifica si hay un camino directo (horizontal o vertical) sin obstáculos"""
    if pos1[0] == pos2[0]:  # Vertical
        y_start, y_end = min(pos1[1], pos2[1]), max(pos1[1], pos2[1])
        for y in range(y_start, y_end + 1):
            if (pos1[0], y) != pos1 and (pos1[0], y) != pos2:
                if not (self.board[y][pos1[0]] is None or self.board[y][pos1[0]] == ''):
                    return False
        return True
    elif pos1[1] == pos2[1]:  # Horizontal
        x_start, x_end = min(pos1[0], pos2[0]), max(pos1[0], pos2[0])
        for x in range(x_start, x_end + 1):
            if (x, pos1[1]) != pos1 and (x, pos1[1]) != pos2:
                if not (self.board[pos1[1]][x] is None or self.board[pos1[1]][x] == ''):
                    return False
        return True
    return False
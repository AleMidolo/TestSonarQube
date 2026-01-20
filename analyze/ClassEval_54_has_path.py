def has_path(self, pos1, pos2):
    """
    verifica si hay un camino entre dos íconos
    :param pos1: tupla de posición (x, y) del primer ícono
    :param pos2: tupla de posición (x, y) del segundo ícono
    :return: True o False, representando si hay un camino entre dos íconos
    """
    # En Mahjong Connect, dos íconos pueden conectarse si hay un camino
    # con máximo 2 giros (3 segmentos de línea) que los conecte
    # y el camino solo pasa por celdas vacías (None o '')
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Verificar si las posiciones son las mismas
    if pos1 == pos2:
        return False
    
    # Verificar si los íconos son iguales
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # Verificar camino directo (0 giros)
    if self._has_direct_path(pos1, pos2):
        return True
    
    # Verificar camino con 1 giro
    if self._has_one_turn_path(pos1, pos2):
        return True
    
    # Verificar camino con 2 giros
    if self._has_two_turn_path(pos1, pos2):
        return True
    
    return False

def _is_empty(self, x, y):
    """Verifica si una celda está vacía o fuera del tablero"""
    if x < 0 or y < 0 or y >= len(self.board) or x >= len(self.board[0]):
        return True  # Fuera del tablero se considera vacío
    return self.board[y][x] is None or self.board[y][x] == ''

def _has_direct_path(self, pos1, pos2):
    """Verifica si hay un camino directo (horizontal o vertical)"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Camino horizontal
    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            if not self._is_empty(x, y1):
                return False
        return True
    
    # Camino vertical
    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            if not self._is_empty(x1, y):
                return False
        return True
    
    return False

def _has_one_turn_path(self, pos1, pos2):
    """Verifica si hay un camino con un giro"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Punto de giro 1: (x1, y2)
    corner1 = (x1, y2)
    if (corner1 != pos1 and corner1 != pos2 and 
        self._is_empty(x1, y2) and
        self._has_direct_path(pos1, corner1) and 
        self._has_direct_path(corner1, pos2)):
        return True
    
    # Punto de giro 2: (x2, y1)
    corner2 = (x2, y1)
    if (corner2 != pos1 and corner2 != pos2 and
        self._is_empty(x2, y1) and
        self._has_direct_path(pos1, corner2) and 
        self._has_direct_path(corner2, pos2)):
        return True
    
    return False

def _has_two_turn_path(self, pos1, pos2):
    """Verifica si hay un camino con dos giros"""
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Explorar líneas horizontales desde pos1
    for x in range(-1, len(self.board[0]) + 1):
        if x != x1:
            mid1 = (x, y1)
            if self._is_empty(x, y1) and self._has_direct_path(pos1, mid1):
                mid2 = (x, y2)
                if (self._is_empty(x, y2) and 
                    self._has_direct_path(mid1, mid2) and 
                    self._has_direct_path(mid2, pos2)):
                    return True
    
    # Explorar líneas verticales desde pos1
    for y in range(-1, len(self.board) + 1):
        if y != y1:
            mid1 = (x1, y)
            if self._is_empty(x1, y) and self._has_direct_path(pos1, mid1):
                mid2 = (x2, y)
                if (self._is_empty(x2, y) and 
                    self._has_direct_path(mid1, mid2) and 
                    self._has_direct_path(mid2, pos2)):
                    return True
    
    return False
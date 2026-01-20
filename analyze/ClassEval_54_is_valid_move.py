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
    if self.board[pos1[1]][pos1[0]] != self.board[pos2[1]][pos2[0]]:
        return False
    
    # Verificar que hay un camino válido entre las dos posiciones
    return self.has_valid_path(pos1, pos2)
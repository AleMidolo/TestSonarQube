def is_valid_move(self, pos1, pos2):
    """
    verifica se il movimento di due icone è valido (cioè le posizioni sono all'interno dell'intervallo della tavola da gioco, le due posizioni non sono le stesse, le due posizioni hanno la stessa icona e c'è un percorso valido tra le due posizioni)
    :param pos1: tupla di posizione (x, y) della prima icona
    :param pos2: tupla di posizione (x, y) della seconda icona
    :return: True o False, che rappresenta se il movimento di due icone è valido
    """
    # Verifica che le posizioni siano all'interno della tavola
    if not (0 <= pos1[0] < len(self.board[0]) and 0 <= pos1[1] < len(self.board)):
        return False
    if not (0 <= pos2[0] < len(self.board[0]) and 0 <= pos2[1] < len(self.board)):
        return False
    
    # Verifica che le due posizioni non siano le stesse
    if pos1 == pos2:
        return False
    
    # Verifica che le due posizioni abbiano la stessa icona
    if self.board[pos1[1]][pos1[0]] != self.board[pos2[1]][pos2[0]]:
        return False
    
    # Verifica che ci sia un percorso valido tra le due posizioni
    # Nel Mahjong Connect, un percorso valido può avere al massimo 2 svolte (3 segmenti di linea)
    return self._has_valid_path(pos1, pos2)

def _has_valid_path(self, pos1, pos2):
    """
    Verifica se esiste un percorso valido tra due posizioni con al massimo 2 svolte
    """
    # Prova percorso diretto (0 svolte)
    if self._is_direct_path(pos1, pos2):
        return True
    
    # Prova percorso con 1 svolta
    if self._is_one_turn_path(pos1, pos2):
        return True
    
    # Prova percorso con 2 svolte
    if self._is_two_turn_path(pos1, pos2):
        return True
    
    return False

def _is_direct_path(self, pos1, pos2):
    """Verifica se c'è un percorso diretto (orizzontale o verticale) tra due posizioni"""
    if pos1[0] == pos2[0]:  # Stessa colonna (verticale)
        y_min, y_max = min(pos1[1], pos2[1]), max(pos1[1], pos2[1])
        for y in range(y_min + 1, y_max):
            if self.board[y][pos1[0]] != '':
                return False
        return True
    elif pos1[1] == pos2[1]:  # Stessa riga (orizzontale)
        x_min, x_max = min(pos1[0], pos2[0]), max(pos1[0], pos2[0])
        for x in range(x_min + 1, x_max):
            if self.board[pos1[1]][x] != '':
                return False
        return True
    return False

def _is_one_turn_path(self, pos1, pos2):
    """Verifica se c'è un percorso con una svolta tra due posizioni"""
    # Prova punto di svolta (pos1[0], pos2[1])
    corner1 = (pos1[0], pos2[1])
    if (corner1 != pos1 and corner1 != pos2 and 
        (self.board[corner1[1]][corner1[0]] == '' or corner1 == pos1 or corner1 == pos2)):
        if self._is_direct_path(pos1, corner1) and self._is_direct_path(corner1, pos2):
            return True
    
    # Prova punto di svolta (pos2[0], pos1[1])
    corner2 = (pos2[0], pos1[1])
    if (corner2 != pos1 and corner2 != pos2 and 
        (self.board[corner2[1]][corner2[0]] == '' or corner2 == pos1 or corner2 == pos2)):
        if self._is_direct_path(pos1, corner2) and self._is_direct_path(corner2, pos2):
            return True
    
    return False

def _is_two_turn_path(self, pos1, pos2):
    """Verifica se c'è un percorso con due svolte tra due posizioni"""
    # Prova tutti i possibili punti intermedi
    for y in range(len(self.board)):
        for x in range(len(self.board[0])):
            mid = (x, y)
            if self.board[y][x] == '' or mid == pos1 or mid == pos2:
                if self._is_one_turn_path(pos1, mid) and self._is_one_turn_path(mid, pos2):
                    return True
    return False
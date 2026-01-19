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
    return self.has_valid_path(pos1, pos2)


def has_valid_path(self, pos1, pos2):
    """
    Verifica se esiste un percorso valido tra due posizioni con al massimo 2 svolte
    """
    # Percorso diretto (0 svolte)
    if self.is_direct_path(pos1, pos2):
        return True
    
    # Percorso con 1 svolta
    # Prova il punto intermedio (pos1[0], pos2[1])
    mid1 = (pos1[0], pos2[1])
    if self.is_empty_or_target(mid1, pos1, pos2):
        if self.is_direct_path(pos1, mid1) and self.is_direct_path(mid1, pos2):
            return True
    
    # Prova il punto intermedio (pos2[0], pos1[1])
    mid2 = (pos2[0], pos1[1])
    if self.is_empty_or_target(mid2, pos1, pos2):
        if self.is_direct_path(pos1, mid2) and self.is_direct_path(mid2, pos2):
            return True
    
    # Percorso con 2 svolte - esplora tutte le possibili posizioni intermedie
    for y in range(-1, len(self.board) + 1):
        for x in range(-1, len(self.board[0]) + 1):
            mid = (x, y)
            if self.is_empty_or_target(mid, pos1, pos2):
                # Controlla percorso pos1 -> mid -> pos2 con 1 svolta in ciascun segmento
                if self.has_one_turn_path(pos1, mid) and self.has_one_turn_path(mid, pos2):
                    return True
    
    return False


def is_direct_path(self, pos1, pos2):
    """Verifica se c'è un percorso diretto (orizzontale o verticale) senza ostacoli"""
    if pos1[0] == pos2[0]:  # Stesso x, percorso verticale
        y_min, y_max = min(pos1[1], pos2[1]), max(pos1[1], pos2[1])
        for y in range(y_min + 1, y_max):
            if not self.is_empty_or_target((pos1[0], y), pos1, pos2):
                return False
        return True
    elif pos1[1] == pos2[1]:  # Stesso y, percorso orizzontale
        x_min, x_max = min(pos1[0], pos2[0]), max(pos1[0], pos2[0])
        for x in range(x_min + 1, x_max):
            if not self.is_empty_or_target((x, pos1[1]), pos1, pos2):
                return False
        return True
    return False


def has_one_turn_path(self, pos1, pos2):
    """Verifica se c'è un percorso con esattamente 1 svolta"""
    mid1 = (pos1[0], pos2[1])
    if self.is_empty_or_target(mid1, pos1, pos2):
        if self.is_direct_path(pos1, mid1) and self.is_direct_path(mid1, pos2):
            return True
    
    mid2 = (pos2[0], pos1[1])
    if self.is_empty_or_target(mid2, pos1, pos2):
        if self.is_direct_path(pos1, mid2) and self.is_direct_path(mid2, pos2):
            return True
    
    return False


def is_empty_or_target(self, pos, pos1, pos2):
    """Verifica se una posizione è vuota o è una delle posizioni target"""
    if pos == pos1 or pos == pos2:
        return True
    # Posizioni fuori dalla tavola sono considerate vuote
    if pos[0] < 0 or pos[0] >= len(self.board[0]) or pos[1] < 0 or pos[1] >= len(self.board):
        return True
    return self.board[pos[1]][pos[0]] is None or self.board[pos[1]][pos[0]] == ''
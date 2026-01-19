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
    
    # Verifica che entrambe le posizioni non siano vuote
    if self.board[pos1[1]][pos1[0]] is None or self.board[pos2[1]][pos2[0]] is None:
        return False
    
    # Verifica che esista un percorso valido tra le due posizioni
    return self.has_valid_path(pos1, pos2)
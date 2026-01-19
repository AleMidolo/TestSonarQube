def get_possible_moves(self, state):
    """
    Secondo lo stato attuale, trova tutte le direzioni di movimento possibili. Ha solo 4 direzioni: 'su', 'giù', 'sinistra', 'destra'.
    :param state: una lista di interi di dimensione 3*3, memorizza lo stato attuale.
    :return moves: una lista di str, memorizza tutte le direzioni di movimento possibili secondo lo stato attuale.
    >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
    ['su', 'sinistra', 'destra']
    """
    moves = []
    
    # Trova la posizione dello 0 (spazio vuoto)
    zero_row, zero_col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break
        if zero_row is not None:
            break
    
    # Controlla se possiamo muovere su (lo 0 si muove su, quindi deve esserci una riga sopra)
    if zero_row > 0:
        moves.append('su')
    
    # Controlla se possiamo muovere giù (lo 0 si muove giù, quindi deve esserci una riga sotto)
    if zero_row < 2:
        moves.append('giù')
    
    # Controlla se possiamo muovere sinistra (lo 0 si muove a sinistra, quindi deve esserci una colonna a sinistra)
    if zero_col > 0:
        moves.append('sinistra')
    
    # Controlla se possiamo muovere destra (lo 0 si muove a destra, quindi deve esserci una colonna a destra)
    if zero_col < 2:
        moves.append('destra')
    
    return moves
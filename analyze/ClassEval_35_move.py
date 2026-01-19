def move(self, state, direction):
    """
    Trova il blocco vuoto, quindi sposta il tabellone nella direzione data.
    :param state: una lista di interi di dimensione 3*3, memorizza lo stato prima del movimento.
    :param direction: str, ha solo 4 direzioni 'su', 'giù', 'sinistra', 'destra'
    :return new_state: una lista di interi di dimensione 3*3, memorizza lo stato dopo il movimento.
    >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'sinistra')
    [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
    """
    # Crea una copia dello stato per non modificare l'originale
    new_state = [row[:] for row in state]
    
    # Trova la posizione del blocco vuoto (0)
    empty_row, empty_col = None, None
    for i in range(3):
        for j in range(3):
            if new_state[i][j] == 0:
                empty_row, empty_col = i, j
                break
        if empty_row is not None:
            break
    
    # Determina la nuova posizione in base alla direzione
    if direction == 'su':
        new_row, new_col = empty_row - 1, empty_col
    elif direction == 'giù':
        new_row, new_col = empty_row + 1, empty_col
    elif direction == 'sinistra':
        new_row, new_col = empty_row, empty_col - 1
    elif direction == 'destra':
        new_row, new_col = empty_row, empty_col + 1
    else:
        return new_state
    
    # Verifica che la nuova posizione sia valida
    if 0 <= new_row < 3 and 0 <= new_col < 3:
        # Scambia il blocco vuoto con il blocco nella nuova posizione
        new_state[empty_row][empty_col] = new_state[new_row][new_col]
        new_state[new_row][new_col] = 0
    
    return new_state
def move(self, state, direction):
    """
    Encuentra el bloque en blanco, luego mueve el tablero en la dirección dada.
    :param state: una lista de enteros de tamaño 3*3, almacena el estado antes de mover.
    :param direction: str, solo tiene 4 direcciones 'up', 'down', 'left', 'right'
    :return new_state: una lista de enteros de tamaño 3*3, almacena el estado después de mover.
    >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
    [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
    """
    # Crear una copia profunda del estado para no modificar el original
    new_state = [row[:] for row in state]
    
    # Encontrar la posición del bloque en blanco (0)
    blank_row, blank_col = None, None
    for i in range(3):
        for j in range(3):
            if new_state[i][j] == 0:
                blank_row, blank_col = i, j
                break
        if blank_row is not None:
            break
    
    # Determinar la nueva posición según la dirección
    if direction == 'up':
        new_row, new_col = blank_row - 1, blank_col
    elif direction == 'down':
        new_row, new_col = blank_row + 1, blank_col
    elif direction == 'left':
        new_row, new_col = blank_row, blank_col - 1
    elif direction == 'right':
        new_row, new_col = blank_row, blank_col + 1
    else:
        return new_state
    
    # Verificar que la nueva posición esté dentro de los límites
    if 0 <= new_row < 3 and 0 <= new_col < 3:
        # Intercambiar el blanco con el bloque en la nueva posición
        new_state[blank_row][blank_col] = new_state[new_row][new_col]
        new_state[new_row][new_col] = 0
    
    return new_state
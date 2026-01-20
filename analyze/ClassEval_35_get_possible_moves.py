def get_possible_moves(self, state):
    """
    De acuerdo con el estado actual, encuentra todas las direcciones de movimiento posibles. Solo tiene 4 direcciones: 'arriba', 'abajo', 'izquierda', 'derecha'.
    :param state: una lista de enteros de tamaño 3*3, que almacena el estado actual.
    :return moves: una lista de str, que almacena todas las direcciones de movimiento posibles de acuerdo con el estado actual.
    >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
    ['arriba', 'izquierda', 'derecha']
    """
    moves = []
    
    # Encontrar la posición del espacio vacío (0)
    row, col = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row, col = i, j
                break
    
    # Verificar si se puede mover hacia arriba (el 0 puede intercambiarse con la celda de arriba)
    # Esto significa que hay una celda arriba, es decir, row > 0
    if row > 0:
        moves.append('arriba')
    
    # Verificar si se puede mover hacia abajo (el 0 puede intercambiarse con la celda de abajo)
    # Esto significa que hay una celda abajo, es decir, row < 2
    if row < 2:
        moves.append('abajo')
    
    # Verificar si se puede mover hacia izquierda (el 0 puede intercambiarse con la celda de la izquierda)
    # Esto significa que hay una celda a la izquierda, es decir, col > 0
    if col > 0:
        moves.append('izquierda')
    
    # Verificar si se puede mover hacia derecha (el 0 puede intercambiarse con la celda de la derecha)
    # Esto significa que hay una celda a la derecha, es decir, col < 2
    if col < 2:
        moves.append('derecha')
    
    return moves
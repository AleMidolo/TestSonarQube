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
    
    # Verificar si se puede mover arriba (el espacio vacío puede moverse arriba si no está en la fila 0)
    if row > 0:
        moves.append('arriba')
    
    # Verificar si se puede mover abajo (el espacio vacío puede moverse abajo si no está en la fila 2)
    if row < 2:
        moves.append('abajo')
    
    # Verificar si se puede mover izquierda (el espacio vacío puede moverse a la izquierda si no está en la columna 0)
    if col > 0:
        moves.append('izquierda')
    
    # Verificar si se puede mover derecha (el espacio vacío puede moverse a la derecha si no está en la columna 2)
    if col < 2:
        moves.append('derecha')
    
    return moves
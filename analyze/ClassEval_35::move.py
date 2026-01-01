def move(self, state, direction):
    """
        Encuentra el bloque en blanco, luego mueve el tablero en la dirección dada.
        :param state: una lista de enteros de tamaño 3*3, almacena el estado antes de mover.
        :param direction: str, solo tiene 4 direcciones 'up', 'down', 'left', 'right'
        :return new_state: una lista de enteros de tamaño 3*3, almacena el estado después de mover.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
    new_state = [row[:] for row in state]
    i, j = self.find_blank(state)
    if direction == 'up':
        new_state[i][j], new_state[i - 1][j] = (new_state[i - 1][j], new_state[i][j])
    elif direction == 'down':
        new_state[i][j], new_state[i + 1][j] = (new_state[i + 1][j], new_state[i][j])
    elif direction == 'left':
        new_state[i][j], new_state[i][j - 1] = (new_state[i][j - 1], new_state[i][j])
    elif direction == 'right':
        new_state[i][j], new_state[i][j + 1] = (new_state[i][j + 1], new_state[i][j])
    return new_state
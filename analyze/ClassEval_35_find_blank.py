def find_blank(self, state):
    """
    Encuentra la posición en blanco del estado actual, que es el elemento 0.
    :param state: una lista de enteros de tamaño 3*3, que almacena el estado actual.
    :return i, j: dos enteros, que representan las coordenadas del bloque en blanco.
    >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
    >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
    (2, 1)
    """
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return (i, j)
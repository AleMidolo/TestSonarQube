def get_possible_moves(self, state):
    """
        De acuerdo con el estado actual, encuentra todas las direcciones de movimiento posibles. Solo tiene 4 direcciones: 'arriba', 'abajo', 'izquierda', 'derecha'.
        :param state: una lista de enteros de tamaño 3*3, que almacena el estado actual.
        :return moves: una lista de str, que almacena todas las direcciones de movimiento posibles de acuerdo con el estado actual.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['arriba', 'izquierda', 'derecha']
        """
    i, j = self.find_blank(state)
    moves = []
    if i > 0:
        moves.append('up')
    if i < 2:
        moves.append('down')
    if j > 0:
        moves.append('left')
    if j < 2:
        moves.append('right')
    return moves
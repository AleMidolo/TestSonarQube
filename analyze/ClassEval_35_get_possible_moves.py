def get_possible_moves(self, state):
    """
        Secondo lo stato attuale, trova tutte le direzioni di movimento possibili. Ha solo 4 direzioni: 'su', 'giù', 'sinistra', 'destra'.
        :param state: una lista di interi di dimensione 3*3, memorizza lo stato attuale.
        :return moves: una lista di str, memorizza tutte le direzioni di movimento possibili secondo lo stato attuale.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['su', 'sinistra', 'destra']
        """
    moves = []
    i, j = self.find_blank(state)
    if i > 0:
        moves.append('up')
    if i < 2:
        moves.append('down')
    if j > 0:
        moves.append('left')
    if j < 2:
        moves.append('right')
    return moves
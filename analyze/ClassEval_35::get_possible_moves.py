def get_possible_moves(self, state):
    """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['up', 'left', 'right']
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
def move(self, state, direction):
    """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
    import copy
    new_state = copy.deepcopy(state)
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
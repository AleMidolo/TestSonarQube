def move(self, state, direction):
    """
    Find the blank block, then makes the board moves forward the given direction.
    :param state: a 3*3 size list of Integer, stores the state before moving.
    :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
    :return new_state: a 3*3 size list of Integer, stores the state after moving.
    >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
    [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
    """
    # Create a deep copy of the state to avoid modifying the original
    new_state = [row[:] for row in state]
    
    # Find the position of the blank (0)
    blank_row, blank_col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                blank_row, blank_col = i, j
                break
        if blank_row is not None:
            break
    
    # Determine the new position based on direction
    # Note: moving the blank "left" means swapping with the tile to its left
    if direction == 'left':
        if blank_col > 0:
            new_state[blank_row][blank_col] = new_state[blank_row][blank_col - 1]
            new_state[blank_row][blank_col - 1] = 0
    elif direction == 'right':
        if blank_col < 2:
            new_state[blank_row][blank_col] = new_state[blank_row][blank_col + 1]
            new_state[blank_row][blank_col + 1] = 0
    elif direction == 'up':
        if blank_row > 0:
            new_state[blank_row][blank_col] = new_state[blank_row - 1][blank_col]
            new_state[blank_row - 1][blank_col] = 0
    elif direction == 'down':
        if blank_row < 2:
            new_state[blank_row][blank_col] = new_state[blank_row + 1][blank_col]
            new_state[blank_row + 1][blank_col] = 0
    
    return new_state
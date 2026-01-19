def get_possible_moves(self, state):
    """
    According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
    :param state: a 3*3 size list of Integer, stores the current state.
    :return moves: a list of str, store all the possible moving directions according to the current state.
    >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
    ['up', 'left', 'right']
    """
    moves = []
    
    # Find the position of the empty tile (0)
    empty_row, empty_col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_row, empty_col = i, j
                break
        if empty_row is not None:
            break
    
    # Check each possible direction
    # 'up' means moving a tile up into the empty space (empty tile moves down)
    if empty_row < 2:  # Can move down (tile from below moves up)
        moves.append('up')
    
    # 'down' means moving a tile down into the empty space (empty tile moves up)
    if empty_row > 0:  # Can move up (tile from above moves down)
        moves.append('down')
    
    # 'left' means moving a tile left into the empty space (empty tile moves right)
    if empty_col < 2:  # Can move right (tile from right moves left)
        moves.append('left')
    
    # 'right' means moving a tile right into the empty space (empty tile moves left)
    if empty_col > 0:  # Can move left (tile from left moves right)
        moves.append('right')
    
    return moves
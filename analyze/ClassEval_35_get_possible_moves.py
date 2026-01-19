def get_possible_moves(self, state):
    """
    According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
    :param state: a 3*3 size list of Integer, stores the current state.
    :return moves: a list of str, store all the possible moving directions according to the current state.
    >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
    ['up', 'left', 'right']
    """
    moves = []
    
    # Find the position of 0 (empty tile)
    zero_row, zero_col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break
        if zero_row is not None:
            break
    
    # Check each direction
    # 'up' means moving a tile up into the empty space (empty space moves down)
    if zero_row < 2:  # Can move down (tile from below moves up)
        moves.append('up')
    
    # 'down' means moving a tile down into the empty space (empty space moves up)
    if zero_row > 0:  # Can move up (tile from above moves down)
        moves.append('down')
    
    # 'left' means moving a tile left into the empty space (empty space moves right)
    if zero_col < 2:  # Can move right (tile from right moves left)
        moves.append('left')
    
    # 'right' means moving a tile right into the empty space (empty space moves left)
    if zero_col > 0:  # Can move left (tile from left moves right)
        moves.append('right')
    
    return moves
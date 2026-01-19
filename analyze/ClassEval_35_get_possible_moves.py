def get_possible_moves(self, state):
    """
    अभी की स्थिति के आधार पर सभी संभावित चलने की दिशाएँ पाएँ।
    केवल चार दिशाएँ हैं: 'ऊपर', 'नीचे', 'बाएँ', 'दाएँ'।

    :param state: इंटीजर की एक 3×3 लिस्ट, जो अभी की स्थिति को स्टोर करती है
    :return moves: str की एक लिस्ट, जो अभी की स्थिति के आधार पर सभी संभावित चलने की दिशाएँ स्टोर करती है

    >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
    ['ऊपर', 'बाएँ', 'दाएँ']
    """
    # Find the position of 0 (empty space)
    zero_row, zero_col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break
        if zero_row is not None:
            break
    
    moves = []
    
    # Check if we can move up (0 can move up if there's a tile above it)
    # Moving up means the tile above moves down to 0's position
    if zero_row > 0:
        moves.append('ऊपर')
    
    # Check if we can move down (0 can move down if there's a tile below it)
    if zero_row < 2:
        moves.append('नीचे')
    
    # Check if we can move left (0 can move left if there's a tile to its left)
    if zero_col > 0:
        moves.append('बाएँ')
    
    # Check if we can move right (0 can move right if there's a tile to its right)
    if zero_col < 2:
        moves.append('दाएँ')
    
    return moves
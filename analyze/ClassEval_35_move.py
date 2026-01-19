def move(self, state, direction):
    """
    खाली ब्लॉक को खोजें, फिर दिए गए दिशा में बोर्ड को आगे बढ़ाएं।
    :param state: एक 3*3 आकार की Integer की सूची, जो चलने से पहले की स्थिति को संग्रहीत करती है।
    :param direction: str, केवल 4 दिशाएँ 'up', 'down', 'left', 'right' हैं
    :return new_state: एक 3*3 आकार की Integer की सूची, जो चलने के बाद की स्थिति को संग्रहीत करती है।
    >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
    [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
    """
    # Create a deep copy of the state to avoid modifying the original
    new_state = [row[:] for row in state]
    
    # Find the position of the empty block (0)
    empty_row, empty_col = None, None
    for i in range(3):
        for j in range(3):
            if new_state[i][j] == 0:
                empty_row, empty_col = i, j
                break
        if empty_row is not None:
            break
    
    # Determine the new position based on direction
    # Note: moving the empty block 'left' means swapping with the tile on its left
    if direction == 'left':
        if empty_col > 0:
            # Swap empty block with the tile on its left
            new_state[empty_row][empty_col], new_state[empty_row][empty_col - 1] = \
                new_state[empty_row][empty_col - 1], new_state[empty_row][empty_col]
    elif direction == 'right':
        if empty_col < 2:
            # Swap empty block with the tile on its right
            new_state[empty_row][empty_col], new_state[empty_row][empty_col + 1] = \
                new_state[empty_row][empty_col + 1], new_state[empty_row][empty_col]
    elif direction == 'up':
        if empty_row > 0:
            # Swap empty block with the tile above it
            new_state[empty_row][empty_col], new_state[empty_row - 1][empty_col] = \
                new_state[empty_row - 1][empty_col], new_state[empty_row][empty_col]
    elif direction == 'down':
        if empty_row < 2:
            # Swap empty block with the tile below it
            new_state[empty_row][empty_col], new_state[empty_row + 1][empty_col] = \
                new_state[empty_row + 1][empty_col], new_state[empty_row][empty_col]
    
    return new_state
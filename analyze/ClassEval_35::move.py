def move(self, state, direction):
    """
    खाली ब्लॉक को खोजें, फिर दिए गए दिशा में बोर्ड को आगे बढ़ाएं।
    :param state: एक 3*3 आकार की Integer की सूची, जो चलने से पहले की स्थिति को संग्रहीत करती है।
    :param direction: str, केवल 4 दिशाएँ 'up', 'down', 'left', 'right' हैं
    :return new_state: एक 3*3 आकार की Integer की सूची, जो चलने के बाद की स्थिति को संग्रहीत करती है।
    >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
    [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
    """
    new_state = [row[:] for row in state]  # Create a copy of the current state
    i, j = self.find_blank(state)  # Find the position of the blank space (0)

    if direction == 'up':
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif direction == 'down':
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif direction == 'left':
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif direction == 'right':
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

    return new_state
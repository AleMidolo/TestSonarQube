def move(self, state, direction):
    """
        Trova il blocco vuoto, quindi sposta il tabellone nella direzione data.
        :param state: una lista di interi di dimensione 3*3, memorizza lo stato prima del movimento.
        :param direction: str, ha solo 4 direzioni 'su', 'giù', 'sinistra', 'destra'
        :return new_state: una lista di interi di dimensione 3*3, memorizza lo stato dopo il movimento.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'sinistra')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
    i, j = self.find_blank(state)
    new_state = [row[:] for row in state]
    if direction == 'up':
        new_state[i][j], new_state[i - 1][j] = (new_state[i - 1][j], new_state[i][j])
    elif direction == 'down':
        new_state[i][j], new_state[i + 1][j] = (new_state[i + 1][j], new_state[i][j])
    elif direction == 'left':
        new_state[i][j], new_state[i][j - 1] = (new_state[i][j - 1], new_state[i][j])
    elif direction == 'right':
        new_state[i][j], new_state[i][j + 1] = (new_state[i][j + 1], new_state[i][j])
    return new_state
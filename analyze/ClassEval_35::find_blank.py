def find_blank(self, state):
    """
        Trova la posizione vuota dello stato attuale, che è l'elemento 0.
        :param state: una lista di interi di dimensione 3*3, che memorizza lo stato attuale.
        :return i, j: due interi, che rappresentano le coordinate del blocco vuoto.
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None
def select_all(self):
    """
    Genera una lista de todos los arreglos seleccionando al menos 1 elemento y como máximo el número de datos internos.
    :return: Lista, una lista de todos los arreglos.
    >>> ac = ArrangementCalculator([1, 2, 3])
    >>> ac.select_all()
    [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """
    from itertools import permutations
    
    result = []
    n = len(self.data)
    
    # Generate all permutations for each length from 1 to n
    for r in range(1, n + 1):
        for perm in permutations(self.data, r):
            result.append(list(perm))
    
    return result
def select_all(self):
    """
    Genera un elenco di tutti gli arrangiamenti selezionando almeno 1 elemento e al massimo il numero di dati interni.
    :return: Lista, un elenco di tutti gli arrangiamenti.
    >>> ac = ArrangementCalculator([1, 2, 3])
    >>> ac.select_all()
    [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """
    from itertools import permutations
    
    result = []
    n = len(self.data)
    
    # Generate arrangements for each length from 1 to n
    for r in range(1, n + 1):
        # Get all permutations of length r
        for perm in permutations(self.data, r):
            result.append(list(perm))
    
    return result
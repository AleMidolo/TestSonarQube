def select(self, m=None):
    """
    Genera un elenco di disposizioni selezionando m elementi dai dati interni.
    Se m non è fornito, seleziona tutti gli elementi.
    :param m: int, il numero di elementi da scegliere (default=None).
    :return: List, un elenco di disposizioni.
    >>> ac = ArrangementCalculator([1, 2, 3, 4])
    >>> ac.select(2)
    [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]

    """
    from itertools import permutations
    
    if m is None:
        m = len(self.data)
    
    result = []
    for perm in permutations(self.data, m):
        result.append(list(perm))
    
    return result
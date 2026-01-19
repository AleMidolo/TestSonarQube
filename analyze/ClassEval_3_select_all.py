def select_all(self):
    """
    Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
    :return: List, a list of all arrangements.
    >>> ac = ArrangementCalculator([1, 2, 3])
    >>> ac.select_all()
    [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """
    from itertools import permutations
    
    result = []
    n = len(self.datas)
    
    # Generate permutations for each length from 1 to n
    for r in range(1, n + 1):
        for perm in permutations(self.datas, r):
            result.append(list(perm))
    
    return result
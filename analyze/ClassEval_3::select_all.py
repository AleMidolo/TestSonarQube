def select_all(self):
    """
    Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
    :return: List, a list of all arrangements.
    >>> ac = ArrangementCalculator([1, 2, 3])
    >>> ac.select_all()
    [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """
    
    total_arrangements = []
    for i in range(1, len(self.datas) + 1):
        arrangements = self.select(i)
        total_arrangements.extend(arrangements)
    return total_arrangements
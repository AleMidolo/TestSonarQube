def select_all(self) -> List[List[str]]:
    """
    Genera tutte le possibili combinazioni di selezione di elementi dalla lista di dati fornita e utilizza il metodo select.
    :return: Una lista di combinazioni, List[List[str]].
    >>> calc = CombinationCalculator(["A", "B", "C", "D"])
    >>> calc.select_all()
    [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
    """
    result = []
    n = len(self.data)
    
    for i in range(1, n + 1):
        result.extend(self.select(i))
    
    return result
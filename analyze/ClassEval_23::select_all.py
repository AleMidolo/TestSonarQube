def select_all(self) -> List[List[str]]:
    """
        Genera tutte le possibili combinazioni di selezione di elementi dalla lista di dati fornita e utilizza il metodo select.
        :return: Una lista di combinazioni, List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        """
    all_combinations = []
    for m in range(1, len(self.datas) + 1):
        all_combinations.extend(self.select(m))
    return all_combinations
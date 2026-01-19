def select_all(self) -> List[List[str]]:
    """
        Genera todas las combinaciones posibles de selección de elementos de la lista de datos dada, y utiliza el método select.
        :return: Una lista de combinaciones, List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        """
    all_combinations = []
    for m in range(1, len(self.datas) + 1):
        all_combinations.extend(self.select(m))
    return all_combinations
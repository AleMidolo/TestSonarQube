def select_all(self) -> List[List[str]]:
    """
        Generate all possible combinations of  selecting elements from the given data list,and it uses the select method.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        """
    result = []
    n = len(self.datas)
    for m in range(1, n + 1):
        result.extend(self.select(m))
    return result
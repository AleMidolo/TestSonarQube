def select(self, m: int) -> List[List[str]]:
    """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination,int.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
    if m <= 0 or m > len(self.datas):
        return []
    result = []
    self._select(0, [None] * m, 0, result)
    return result
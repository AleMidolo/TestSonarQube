def select(self, m: int) -> List[List[str]]:
    """
        Genera combinazioni con un numero specificato di elementi.
        :param m: Il numero di elementi in ogni combinazione, int.
        :return: Una lista di combinazioni, List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
    if m <= 0 or m > len(self.datas):
        return []
    result = []
    resultList = [None] * m
    self._select(0, resultList, 0, result)
    return result
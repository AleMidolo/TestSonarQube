def select(self, m: int) -> List[List[str]]:
    """
        Generar combinaciones con un número especificado de elementos.
        :param m: El número de elementos en cada combinación, int.
        :return: Una lista de combinaciones, List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
    if m <= 0 or m > len(self.datas):
        return []
    result = []
    self._select(0, [None] * m, 0, result)
    return result
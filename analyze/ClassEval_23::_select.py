def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
    """
        Genera combinaciones con un número especificado de elementos mediante recursión.
        :param dataIndex: El índice de los datos a seleccionar, int.
        :param resultList: La lista de elementos en la combinación, List[str].
        :param resultIndex: El índice del elemento en la combinación, int.
        :param result: La lista de combinaciones, List[List[str]].
        :return: Ninguno.
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> result = []
        >>> calc._select(0, [None] * 2, 0, result)
        >>> result
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
    if resultIndex == len(resultList):
        result.append(resultList.copy())
        return
    for i in range(dataIndex, len(self.datas)):
        resultList[resultIndex] = self.datas[i]
        self._select(i + 1, resultList, resultIndex + 1, result)
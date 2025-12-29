def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
    """
        Generate combinations with a specified number of elements via recursion.
        :param dataIndex: The index of data to select, int.
        :param resultList: The list of elements in the combination, List[str].
        :param resultIndex: The index of element in the combination, int.
        :param result: The list of combinations, List[List[str]].
        :return: None.
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> result = []
        >>> calc._select(0, [None] * 2, 0, result)
        >>> result
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
    if resultIndex == len(resultList):
        result.append(resultList.copy())
        return
    if dataIndex >= len(self.datas):
        return
    resultList[resultIndex] = self.datas[dataIndex]
    self._select(dataIndex + 1, resultList, resultIndex + 1, result)
    self._select(dataIndex + 1, resultList, resultIndex, result)
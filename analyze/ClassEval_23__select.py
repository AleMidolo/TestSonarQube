def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
    """
    Generate combinations with a specified number of elements by recursion.
    :param dataIndex: The index of the data to be selected,int.
    :param resultList: The list of elements in the combination,List[str].
    :param resultIndex: The index of the element in the combination,int.
    :param result: The list of combinations,List[List[str]].
    :return: None.
    >>> calc = CombinationCalculator(["A", "B", "C", "D"])
    >>> result = []
    >>> calc._select(0, [None] * 2, 0, result)
    >>> result
    [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

    """
    # Base case: if we've filled all positions in resultList, add a copy to result
    if resultIndex == len(resultList):
        result.append(resultList[:])
        return
    
    # Recursive case: try each element from dataIndex onwards
    # We need to ensure we have enough elements left to fill the remaining positions
    # Elements needed = len(resultList) - resultIndex
    # Elements available = len(self.data) - dataIndex
    for i in range(dataIndex, len(self.data) - (len(resultList) - resultIndex) + 1):
        resultList[resultIndex] = self.data[i]
        self._select(i + 1, resultList, resultIndex + 1, result)
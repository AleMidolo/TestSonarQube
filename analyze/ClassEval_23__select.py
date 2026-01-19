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
    
    # If we've run out of data elements to select from, return
    if dataIndex >= len(self.data):
        return
    
    # Calculate how many more elements we need to select
    remaining_positions = len(resultList) - resultIndex
    # Calculate how many elements are still available
    remaining_elements = len(self.data) - dataIndex
    
    # If we don't have enough elements left to fill remaining positions, return
    if remaining_elements < remaining_positions:
        return
    
    # Option 1: Include the current element at dataIndex
    resultList[resultIndex] = self.data[dataIndex]
    self._select(dataIndex + 1, resultList, resultIndex + 1, result)
    
    # Option 2: Skip the current element and try the next one
    self._select(dataIndex + 1, resultList, resultIndex, result)
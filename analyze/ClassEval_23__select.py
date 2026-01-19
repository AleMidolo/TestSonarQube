def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
    """
    Genera combinazioni con un numero specificato di elementi tramite ricorsione.
    :param dataIndex: L'indice dei dati da selezionare, int.
    :param resultList: La lista degli elementi nella combinazione, List[str].
    :param resultIndex: L'indice dell'elemento nella combinazione, int.
    :param result: La lista delle combinazioni, List[List[str]].
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
    for i in range(dataIndex, len(self.data)):
        resultList[resultIndex] = self.data[i]
        # Recursively fill the next position, starting from i+1 to avoid duplicates
        self._select(i + 1, resultList, resultIndex + 1, result)
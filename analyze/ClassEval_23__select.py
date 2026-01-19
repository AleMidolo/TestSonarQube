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
    # Caso base: si hemos llenado todos los elementos de la combinación
    if resultIndex == len(resultList):
        result.append(resultList[:])
        return
    
    # Caso base: si no hay suficientes elementos restantes para completar la combinación
    if dataIndex >= len(self.data):
        return
    
    # Incluir el elemento actual en la combinación
    resultList[resultIndex] = self.data[dataIndex]
    self._select(dataIndex + 1, resultList, resultIndex + 1, result)
    
    # No incluir el elemento actual y continuar con el siguiente
    self._select(dataIndex + 1, resultList, resultIndex, result)
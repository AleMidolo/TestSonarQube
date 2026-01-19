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
    # Caso base: se abbiamo riempito tutti gli elementi della combinazione
    if resultIndex == len(resultList):
        result.append(resultList[:])
        return
    
    # Caso base: se non ci sono abbastanza elementi rimanenti per completare la combinazione
    if dataIndex >= len(self.data):
        return
    
    # Calcola quanti elementi mancano da selezionare
    remaining_needed = len(resultList) - resultIndex
    # Calcola quanti elementi sono ancora disponibili
    remaining_available = len(self.data) - dataIndex
    
    # Se non ci sono abbastanza elementi disponibili, termina
    if remaining_available < remaining_needed:
        return
    
    # Scelta 1: Includere l'elemento corrente nella combinazione
    resultList[resultIndex] = self.data[dataIndex]
    self._select(dataIndex + 1, resultList, resultIndex + 1, result)
    
    # Scelta 2: Non includere l'elemento corrente e passare al prossimo
    self._select(dataIndex + 1, resultList, resultIndex, result)
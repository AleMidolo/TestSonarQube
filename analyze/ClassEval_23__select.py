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
    # Caso base: se abbiamo riempito tutti gli slot nella combinazione
    if resultIndex == len(resultList):
        result.append(resultList[:])
        return
    
    # Caso base: se non ci sono più elementi da considerare
    if dataIndex >= len(self.data):
        return
    
    # Calcola quanti elementi mancano da selezionare
    remaining_slots = len(resultList) - resultIndex
    # Calcola quanti elementi sono ancora disponibili
    remaining_elements = len(self.data) - dataIndex
    
    # Se non ci sono abbastanza elementi rimanenti, termina
    if remaining_elements < remaining_slots:
        return
    
    # Scelta 1: Includere l'elemento corrente nella combinazione
    resultList[resultIndex] = self.data[dataIndex]
    self._select(dataIndex + 1, resultList, resultIndex + 1, result)
    
    # Scelta 2: Non includere l'elemento corrente e passare al successivo
    self._select(dataIndex + 1, resultList, resultIndex, result)
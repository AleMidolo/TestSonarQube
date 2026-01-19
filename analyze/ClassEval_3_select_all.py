def select_all(self):
    """
        Genera un elenco di tutti gli arrangiamenti selezionando almeno 1 elemento e al massimo il numero di dati interni.
        :return: Lista, un elenco di tutti gli arrangiamenti.
        >>> ac = ArrangementCalculator([1, 2, 3])
        >>> ac.select_all()
        [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        """
    result = []
    n = len(self.datas)
    for i in range(1, n + 1):
        result.extend(self.select(i))
    return result
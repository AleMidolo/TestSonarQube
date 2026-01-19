def select(self, m=None):
    """
        Genera una lista de arreglos seleccionando m elementos de los datos internos.
        Si no se proporciona m, selecciona todos los elementos.
        :param m: int, el número de elementos a elegir (por defecto=None).
        :return: List, una lista de arreglos.
        >>> ac = ArrangementCalculator([1, 2, 3, 4])
        >>> ac.select(2)
        [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
        """
    if m is None:
        m = len(self.datas)
    return list(itertools.permutations(self.datas, m))
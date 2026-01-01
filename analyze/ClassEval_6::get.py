def get(self, index):
    """
        calcula el tamaño de cada bloque y el resto de la división, y calcula las posiciones de inicio y fin correspondientes basadas en el índice de la partición.
        :param index: el índice de la partición, int.
        :return: el bloque correspondiente, lista.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]
        """
    size, remainder = self.setNum()
    start = index * size + min(index, remainder)
    end = start + size + (1 if index < remainder else 0)
    return self.lst[start:end]
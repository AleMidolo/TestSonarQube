def get(self, index):
    """
        calcula el tamaño de cada bloque y el resto de la división, y calcula las posiciones de inicio y fin correspondientes basadas en el índice de la partición.
        :param index: el índice de la partición, int.
        :return: el bloque correspondiente, lista.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """
    if index < 0 or index >= self.limit:
        raise IndexError('Partition index out of range')
    size, remainder = self.setNum()
    if index < remainder:
        start = index * (size + 1)
        end = start + (size + 1)
    else:
        start = remainder * (size + 1) + (index - remainder) * size
        end = start + size
    return self.lst[start:end]
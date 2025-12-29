def get(self, index):
    """
        calcola la dimensione di ciascun blocco e il resto della divisione, e calcola le posizioni di inizio e fine corrispondenti in base all'indice della partizione.
        :param index: l'indice della partizione, int.
        :return: il blocco corrispondente, lista.
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
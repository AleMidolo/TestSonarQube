def setNum(self):
    """
    Calcula el tamaño de cada bloque y el resto de la división.
    :return: el tamaño de cada bloque y el resto de la división, tupla.
    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.setNum()
    (2, 0)

    """
    block_size = len(self.data) // self.num_partitions
    remainder = len(self.data) % self.num_partitions
    return (block_size, remainder)
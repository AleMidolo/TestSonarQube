def setNum(self):
    """
    Calcola la dimensione di ciascun blocco e il resto della divisione.
    :return: la dimensione di ciascun blocco e il resto della divisione, tupla.
    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.setNum()
    (2, 0)

    """
    block_size = len(self.data) // self.num_partitions
    remainder = len(self.data) % self.num_partitions
    return (block_size, remainder)
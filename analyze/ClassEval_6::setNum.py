def setNum(self):
    """
        Calcola la dimensione di ciascun blocco e il resto della divisione.
        :return: la dimensione di ciascun blocco e il resto della divisione, tupla.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)
        """
    size = len(self.lst) // self.limit
    remainder = len(self.lst) % self.limit
    return (size, remainder)
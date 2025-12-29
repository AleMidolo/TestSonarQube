def setNum(self):
    """
        Calcola la dimensione di ciascun blocco e il resto della divisione.
        :return: la dimensione di ciascun blocco e il resto della divisione, tupla.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)

        """
    n = len(self.lst)
    size = n // self.limit
    remainder = n % self.limit
    return (size, remainder)
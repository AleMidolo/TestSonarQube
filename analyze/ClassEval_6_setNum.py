def setNum(self):
    """
        Calcula el tamaño de cada bloque y el resto de la división.
        :return: el tamaño de cada bloque y el resto de la división, tupla.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)
        """
    size = len(self.lst) // self.limit
    remainder = len(self.lst) % self.limit
    return (size, remainder)
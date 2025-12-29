def setNum(self):
    """
        计算每个块的大小和除法的余数。
        :return: 每个块的大小和除法的余数，元组。
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)

        """
    n = len(self.lst)
    size = n // self.limit
    remainder = n % self.limit
    return (size, remainder)
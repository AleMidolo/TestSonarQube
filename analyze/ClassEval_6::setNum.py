def setNum(self):
    """
        计算每个块的大小和除法的余数。
        :return: 每个块的大小和除法的余数，元组。
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)

        """
    size = len(self.lst) // self.limit
    remainder = len(self.lst) % self.limit
    return (size, remainder)
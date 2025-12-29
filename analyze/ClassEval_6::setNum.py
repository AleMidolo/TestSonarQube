def setNum(self):
    """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)
        """
    total_length = len(self.lst)
    size = total_length // self.limit
    remainder = total_length % self.limit
    return (size, remainder)
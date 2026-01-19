def setNum(self):
    """
    Calculate the size of each block and the remainder of the division.
    :return: the size of each block and the remainder of the division, tuple.
    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.setNum()
    (2, 0)

    """
    block_size = len(self.data) // self.num_partitions
    remainder = len(self.data) % self.num_partitions
    return (block_size, remainder)
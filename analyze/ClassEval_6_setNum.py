def setNum(self):
    """
    计算每个块的大小和除法的余数。
    :return: 每个块的大小和除法的余数，元组。
    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.setNum()
    (2, 0)

    """
    total_length = len(self.data)
    num_partitions = self.num
    block_size = total_length // num_partitions
    remainder = total_length % num_partitions
    return (block_size, remainder)
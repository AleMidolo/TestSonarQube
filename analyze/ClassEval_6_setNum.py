def setNum(self):
    """
    计算每个块的大小和除法的余数。
    :return: 每个块的大小和除法的余数，元组。
    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.setNum()
    (2, 0)

    """
    total_length = len(self.data) if hasattr(self, 'data') else len(self[0]) if isinstance(self, tuple) else 0
    num_partitions = self.num if hasattr(self, 'num') else self[1] if isinstance(self, tuple) else 1
    
    block_size = total_length // num_partitions
    remainder = total_length % num_partitions
    
    return (block_size, remainder)
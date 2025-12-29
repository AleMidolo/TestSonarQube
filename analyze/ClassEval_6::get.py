def get(self, index):
    """
        计算每个块的大小和除法的余数，并根据分区的索引计算相应的起始和结束位置。
        :param index: 分区的索引，int。
        :return: 相应的块，list。
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """
    if index < 0 or index >= self.limit:
        raise IndexError('Partition index out of range')
    size, remainder = self.setNum()
    start = index * size + min(index, remainder)
    end = start + size + (1 if index < remainder else 0)
    return self.lst[start:end]
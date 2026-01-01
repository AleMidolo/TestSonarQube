def get(self, index):
    """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """
    if index < 0 or index >= self.limit:
        raise IndexError('Partition index out of range')
    size, remainder = self.setNum()
    if index < remainder:
        start = index * (size + 1)
        end = start + (size + 1)
    else:
        start = remainder * (size + 1) + (index - remainder) * size
        end = start + size
    return self.lst[start:end]
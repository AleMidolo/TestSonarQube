def get(self, index):
    """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]
        """
    size, remainder = self.setNum()
    start = index * size + min(index, remainder)
    end = start + size + (1 if index < remainder else 0)
    return self.lst[start:end]
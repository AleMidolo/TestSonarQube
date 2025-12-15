class AvgPartition: 
    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions, and check if the number of partitions is greater than 0.
        """
        self.lst = lst
        self.limit = limit

    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)
        """
        size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return size, remainder
    
    def get(self, index):
        """
        计算每个块的大小和除法的余数，并根据分区的索引计算相应的起始和结束位置。
        :param index: 分区的索引，int。
        :return: 相应的块，list。
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]
        """
        size, remainder = self.setNum()
        start = index * size + min(index, remainder)
        end = start + size + (1 if index < remainder else 0)
        return self.lst[start:end]
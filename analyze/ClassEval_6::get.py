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
        प्रत्येक ब्लॉक का आकार और विभाजन के शेषफल की गणना करें, और विभाजन के अनुक्रमांक के आधार पर संबंधित प्रारंभ और अंत स्थितियों की गणना करें।
        :param index: विभाजन का अनुक्रमांक, int.
        :return: संबंधित ब्लॉक, सूची।
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]
        """
        size, remainder = self.setNum()
        start = index * size
        end = start + size + (1 if index < remainder else 0)
        return self.lst[start:end]
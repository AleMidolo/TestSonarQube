def get(self, index):
    """
        प्रत्येक ब्लॉक का आकार और विभाजन के शेषफल की गणना करें, और विभाजन के अनुक्रमांक के आधार पर संबंधित प्रारंभ और अंत स्थितियों की गणना करें।
        :param index: विभाजन का अनुक्रमांक, int.
        :return: संबंधित ब्लॉक, सूची।
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """
    if index < 0 or index >= self.limit:
        raise IndexError(f'Index {index} out of range for {self.limit} partitions')
    size, remainder = self.setNum()
    if index < remainder:
        start = index * (size + 1)
        end = start + (size + 1)
    else:
        start = remainder * (size + 1) + (index - remainder) * size
        end = start + size
    return self.lst[start:end]
def get(self, index):
    """
    प्रत्येक ब्लॉक का आकार और विभाजन के शेषफल की गणना करें, और विभाजन के अनुक्रमांक के आधार पर संबंधित प्रारंभ और अंत स्थितियों की गणना करें।
    :param index: विभाजन का अनुक्रमांक, int.
    :return: संबंधित ब्लॉक, सूची।
    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.get(0)
    [1, 2]

    """
    # Calculate the base block size and remainder
    total_length = len(self.data)
    base_size = total_length // self.num_partitions
    remainder = total_length % self.num_partitions
    
    # Calculate start position for the given index
    # First 'remainder' blocks get one extra element
    if index < remainder:
        start = index * (base_size + 1)
        end = start + base_size + 1
    else:
        start = remainder * (base_size + 1) + (index - remainder) * base_size
        end = start + base_size
    
    return self.data[start:end]
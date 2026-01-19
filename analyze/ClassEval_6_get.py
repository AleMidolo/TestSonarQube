def get(self, index):
    """
    प्रत्येक ब्लॉक का आकार और विभाजन के शेषफल की गणना करें, और विभाजन के अनुक्रमांक के आधार पर संबंधित प्रारंभ और अंत स्थितियों की गणना करें।
    :param index: विभाजन का अनुक्रमांक, int.
    :return: संबंधित ब्लॉक, सूची।
    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.get(0)
    [1, 2]

    """
    # Calculate the size of each block and remainder
    total_length = len(self.data)
    block_size = total_length // self.num_partitions
    remainder = total_length % self.num_partitions
    
    # Calculate start and end positions based on index
    # First 'remainder' blocks get one extra element
    if index < remainder:
        start = index * (block_size + 1)
        end = start + block_size + 1
    else:
        start = remainder * (block_size + 1) + (index - remainder) * block_size
        end = start + block_size
    
    return self.data[start:end]
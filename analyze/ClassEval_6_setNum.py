def setNum(self):
    """
    हर ब्लॉक का साइज़ और डिवीज़न का बचा हुआ हिस्सा कैलकुलेट करें।

    :return: एक टपल जिसमें हर ब्लॉक का साइज़ और डिवीज़न का बचा हुआ हिस्सा हो।

    >>> a = AvgPartition([1, 2, 3, 4], 2)
    >>> a.setNum()
    (2, 0)
    """
    block_size = len(self.data) // self.num_partitions
    remainder = len(self.data) % self.num_partitions
    return (block_size, remainder)
def get_sum(self):
    """
        डेटा का योग निकालें
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_sum()
        10
        """
    return np.sum(self.data)
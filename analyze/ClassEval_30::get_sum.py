def get_sum(self):
    """
        计算数据的总和
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_sum()
        10
        """
    return np.sum(self.data)
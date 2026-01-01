def get_variance(self):
    """
        计算方差，精确到小数点后两位
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_variance()
        1.25
        """
    return round(np.var(self.data), 2)
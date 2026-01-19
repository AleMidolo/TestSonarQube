def get_max(self):
    """
        डेटा में अधिकतम मान की गणना करें
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_max()
        4
        """
    return np.max(self.data)
def get_variance(self):
    """
        वैरिएंस की गणना करें, दशमलव विभाजक के बाद दो अंकों तक सटीक
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_variance()
        1.25
        """
    return round(np.var(self.data), 2)
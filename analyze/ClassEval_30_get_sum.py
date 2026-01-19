def get_sum(self):
    """
        Calcular la suma de los datos
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_sum()
        10
        """
    return np.sum(self.data)
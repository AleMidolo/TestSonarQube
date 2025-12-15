def get_min(self):
        """
        Calculate the minimum value in the data
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_min()
        1
        """
        return np.min(self.data)
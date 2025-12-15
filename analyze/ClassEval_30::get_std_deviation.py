def get_std_deviation(self):
        """
        मानक विचलन की गणना करें, दशमलव विभाजक के बाद दो अंकों तक सटीक
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_deviation()
        1.12
        """
        return round(np.std(self.data), 2)
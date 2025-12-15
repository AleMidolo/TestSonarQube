def get_std_deviation(self):
        """
        计算标准差，精确到小数点后两位
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_deviation()
        1.12
        """
        return round(np.std(self.data), 2)
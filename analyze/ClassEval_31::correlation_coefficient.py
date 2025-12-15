def correlation_coefficient(data1, data2):
        """
        计算两组数据的相关系数。
        :param data1: 第一组数据，列表。
        :param data2: 第二组数据，列表。
        :return: 相关系数，浮点数。
        >>> correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """
        if len(data1) != len(data2):
            raise ValueError("Both data sets must have the same length.")
        
        n = len(data1)
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n
        
        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator1 = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)))
        denominator2 = math.sqrt(sum((data2[i] - mean2) ** 2 for i in range(n)))
        
        if denominator1 == 0 or denominator2 == 0:
            return 0.0
        
        correlation = numerator / (denominator1 * denominator2)
        return correlation
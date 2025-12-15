import math

class Statistics3: 

    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    
    @staticmethod
    def mode(data):
        """
            calculates the mode of the given list.
            :param data: the given list, list.
            :return: the mode of the given list, list.
            >>> statistics3 = Statistics3()
            >>> statistics3.mode([1, 2, 3, 3])
            [3]
        """
        counts = {}
        for value in data:
            counts[value] = counts.get(value, 0) + 1
        max_count = max(counts.values())
        mode_values = [value for value, count in counts.items() if count == max_count]
        return mode_values
    
    @staticmethod
    def mean(data):
        """
            calculates the mean of the given list.
            :param data: the given list, list.
            :return: the mean of the given list, float.
            >>> statistics3 = Statistics3()
            >>> statistics3.mean([1, 2, 3])
            2.0
        """
        if len(data) == 0:
            return None
        return sum(data) / len(data)
    
    @staticmethod
    def correlation_matrix(data):
        """
            calculates the correlation matrix of the given list.
            :param data: the given list, list.
            :return: the correlation matrix of the given list, list.
            >>> statistics3 = Statistics3()
            >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
        """
        matrix = []
        for i in range(len(data[0])):
            row = []
            for j in range(len(data[0])):
                column1 = [row[i] for row in data]
                column2 = [row[j] for row in data]
                correlation = Statistics3.correlation(column1, column2)
                row.append(correlation)
            matrix.append(row)
        return matrix
    
    @staticmethod
    def standard_deviation(data):
        """
            calculates the standard deviation of the given list.
            :param data: the given list, list.
            :return: the standard deviation of the given list, float.
            >>> statistics3 = Statistics3()
            >>> statistics3.standard_deviation([1, 2, 3])
            1.0
        """
        n = len(data)
        if n < 2:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / (n - 1)
        return math.sqrt(variance)
    
    @staticmethod
    def z_score(data):
        """
            calculates the z-score of the given list.
            :param data: the given list, list.
            :return: the z-score of the given list, list.
            >>> statistics3 = Statistics3()
            >>> statistics3.z_score([1, 2, 3, 4])
            [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]
        """
        mean = Statistics3.mean(data)
        std_deviation = Statistics3.standard_deviation(data)
        if std_deviation is None or std_deviation == 0:
            return None
        return [(x - mean) / std_deviation for x in data]
    
    @staticmethod
    def correlation(x, y):
        """
        计算给定列表的相关性。
        :param x: 给定列表，list。
        :param y: 给定列表，list。
        :return: 给定列表的相关性，float。
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0
        """
        if len(x) != len(y):
            raise ValueError("Lists must be of the same length.")
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
        denominator = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(len(x))) * 
                                 sum((y[i] - mean_y) ** 2 for i in range(len(y))))
        if denominator == 0:
            return 0
        return numerator / denominator
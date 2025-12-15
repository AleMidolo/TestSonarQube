def median(data):
        """
        计算给定列表的中位数。
        :param data: 给定的列表，list。
        :return: 给定列表的中位数，float。
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """
        n = len(data)
        if n == 0:
            return None
        sorted_data = sorted(data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
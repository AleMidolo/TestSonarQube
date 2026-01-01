def median(self, data):
    """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        median_value = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median_value = sorted_data[mid]
    return round(median_value, 2)
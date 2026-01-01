@staticmethod
def correlation(x, y):
    """
        दो दी गई लिस्ट का कोरिलेशन कैलकुलेट करता है।

        :param x: list, पहली लिस्ट
        :param y: list, दूसरी लिस्ट
        :return: float, दोनों लिस्ट का कोरिलेशन

        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0
        """
    if len(x) != len(y):
        return None
    n = len(x)
    if n < 2:
        return None
    mean_x = Statistics3.mean(x)
    mean_y = Statistics3.mean(y)
    std_x = Statistics3.standard_deviation(x)
    std_y = Statistics3.standard_deviation(y)
    if std_x is None or std_y is None or std_x == 0 or (std_y == 0):
        return None
    covariance = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))) / (n - 1)
    return covariance / (std_x * std_y)
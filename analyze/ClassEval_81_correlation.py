@staticmethod
def correlation(x, y):
    """
    calculates the correlation of the given list.
    :param x: the given list, list.
    :param y: the given list, list.
    :return: the correlation of the given list, float.
    >>> statistics3 = Statistics3()
    >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
    1.0

    """
    n = len(x)
    
    # Calculate means
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calculate numerator: sum of (x - mean_x) * (y - mean_y)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    # Calculate denominator: sqrt(sum of (x - mean_x)^2) * sqrt(sum of (y - mean_y)^2)
    sum_sq_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    denominator = (sum_sq_x ** 0.5) * (sum_sq_y ** 0.5)
    
    # Return correlation coefficient
    if denominator == 0:
        return 0.0
    return numerator / denominator
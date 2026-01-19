@staticmethod
def correlation(x, y):
    """
    calcula la correlación de la lista dada.
    :param x: la lista dada, lista.
    :param y: la lista dada, lista.
    :return: la correlación de la lista dada, float.
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
    
    # Return Pearson correlation coefficient
    return numerator / denominator
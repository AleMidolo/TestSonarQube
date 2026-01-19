@staticmethod
def correlation(x, y):
    """
    calcola la correlazione della lista fornita.
    :param x: la lista fornita, lista.
    :param y: la lista fornita, lista.
    :return: la correlazione della lista fornita, float.
    >>> statistics3 = Statistics3()
    >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
    1.0

    """
    n = len(x)
    
    # Calculate means
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calculate numerator (covariance)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    # Calculate denominator (product of standard deviations)
    sum_sq_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    denominator = (sum_sq_x * sum_sq_y) ** 0.5
    
    # Return Pearson correlation coefficient
    return numerator / denominator
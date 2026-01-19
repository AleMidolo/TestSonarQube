def get_correlation(self):
    """
    Calcular la correlación
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_correlation()
    1.0
    """
    import math
    
    n = len(self.data)
    
    # Create x values as indices (0, 1, 2, 3, ...)
    x = list(range(n))
    y = self.data
    
    # Calculate means
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calculate correlation coefficient
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    sum_sq_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    denominator = math.sqrt(sum_sq_x * sum_sq_y)
    
    if denominator == 0:
        return 0.0
    
    correlation = numerator / denominator
    
    return correlation
def get_correlation(self):
    """
    Calcola la correlazione
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_correlation()
    1.0
    """
    import math
    
    # Assuming this is a method of a class that stores data
    # and that we're calculating correlation between indices and values
    data = self if isinstance(self, list) else getattr(self, 'data', [])
    
    n = len(data)
    if n == 0:
        return 0.0
    
    # Create x as indices (0, 1, 2, ..., n-1) and y as the data values
    x = list(range(n))
    y = data
    
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
    
    return numerator / denominator
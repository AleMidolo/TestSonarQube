def get_correlation(self):
    """
    सहसंबंध की गणना करें
    :return:float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_correlation()
    1.0
    """
    if len(self) < 2:
        return 1.0
    
    # Create indices as x values (0, 1, 2, 3, ...)
    x = list(range(len(self)))
    y = list(self)
    
    n = len(x)
    
    # Calculate means
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calculate correlation coefficient (Pearson's r)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    sum_sq_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    denominator = (sum_sq_x * sum_sq_y) ** 0.5
    
    if denominator == 0:
        return 1.0
    
    correlation = numerator / denominator
    
    return correlation
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
    
    # Create indices for correlation calculation
    indices = list(range(len(self)))
    
    # Calculate means
    mean_x = sum(indices) / len(indices)
    mean_y = sum(self) / len(self)
    
    # Calculate correlation coefficient
    numerator = sum((indices[i] - mean_x) * (self[i] - mean_y) for i in range(len(self)))
    
    sum_sq_x = sum((indices[i] - mean_x) ** 2 for i in range(len(indices)))
    sum_sq_y = sum((self[i] - mean_y) ** 2 for i in range(len(self)))
    
    denominator = (sum_sq_x * sum_sq_y) ** 0.5
    
    if denominator == 0:
        return 1.0
    
    return numerator / denominator
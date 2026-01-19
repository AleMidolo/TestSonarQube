def get_correlation(self):
    """
    计算相关性
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_correlation()
    1.0
    """
    import numpy as np
    
    # Assuming self.data is the data attribute
    data = np.array(self.data)
    
    # Create indices as x values (0, 1, 2, 3, ...)
    x = np.arange(len(data))
    y = data
    
    # Calculate Pearson correlation coefficient
    correlation = np.corrcoef(x, y)[0, 1]
    
    return correlation
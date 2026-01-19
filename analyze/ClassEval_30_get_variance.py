def get_variance(self):
    """
    वैरिएंस की गणना करें, दशमलव विभाजक के बाद दो अंकों तक सटीक
    :return:float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_variance()
    1.25
    """
    if not self or len(self) == 0:
        return 0.0
    
    # Calculate mean
    mean = sum(self) / len(self)
    
    # Calculate variance (sum of squared differences from mean divided by n)
    variance = sum((x - mean) ** 2 for x in self) / len(self)
    
    # Round to 2 decimal places
    return round(variance, 2)
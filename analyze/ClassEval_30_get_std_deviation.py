def get_std_deviation(self):
    """
    मानक विचलन की गणना करें, दशमलव विभाजक के बाद दो अंकों तक सटीक
    :return:float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_std_deviation()
    1.12
    """
    if not self.data or len(self.data) == 0:
        return 0.0
    
    # Calculate mean
    mean = sum(self.data) / len(self.data)
    
    # Calculate variance (sum of squared differences from mean)
    variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
    
    # Calculate standard deviation (square root of variance)
    std_dev = variance ** 0.5
    
    # Round to 2 decimal places
    return round(std_dev, 2)
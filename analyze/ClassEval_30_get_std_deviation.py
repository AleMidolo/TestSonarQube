def get_std_deviation(self):
    """
    Calcular la desviación estándar, con precisión de dos dígitos después del separador decimal
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_std_deviation()
    1.12
    """
    if not self or len(self) == 0:
        return 0.0
    
    # Calculate mean
    mean = sum(self) / len(self)
    
    # Calculate variance (sum of squared differences from mean)
    variance = sum((x - mean) ** 2 for x in self) / len(self)
    
    # Calculate standard deviation (square root of variance)
    std_dev = variance ** 0.5
    
    # Round to 2 decimal places
    return round(std_dev, 2)
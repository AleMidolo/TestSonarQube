def get_variance(self):
    """
    Calcular la varianza, con precisión de dos dígitos después del separador decimal
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_variance()
    1.25
    """
    if not self or len(self) == 0:
        return 0.0
    
    # Calculate the mean
    mean = sum(self) / len(self)
    
    # Calculate the variance (sum of squared differences from mean divided by n)
    variance = sum((x - mean) ** 2 for x in self) / len(self)
    
    # Round to 2 decimal places
    return round(variance, 2)
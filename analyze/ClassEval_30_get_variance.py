def get_variance(self):
    """
    Calcola la varianza, con una precisione di due cifre  decimali
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_variance()
    1.25
    """
    if not self.data or len(self.data) == 0:
        return 0.0
    
    mean = sum(self.data) / len(self.data)
    variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
    
    return round(variance, 2)
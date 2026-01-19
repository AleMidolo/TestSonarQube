def get_variance(self):
    """
    Calculate variance, accurate to two digits after the Decimal separator
    :return:float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_variance()
    1.25
    """
    if not self or len(self) == 0:
        return 0.0
    
    mean = sum(self) / len(self)
    variance = sum((x - mean) ** 2 for x in self) / len(self)
    return round(variance, 2)
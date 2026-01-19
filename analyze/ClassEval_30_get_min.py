def get_min(self):
    """
    Calcular el valor mínimo en los datos
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_min()
    1
    """
    return min(self.data)
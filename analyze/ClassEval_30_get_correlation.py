def get_correlation(self):
    """
    Calcular la correlación
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_correlation()
    1.0
    """
    import math
    
    # Para una sola lista, calculamos la correlación con su índice (posición)
    n = len(self.data)
    
    if n == 0:
        return 0.0
    
    # x será el índice (0, 1, 2, 3, ...)
    # y será los valores de self.data
    x = list(range(n))
    y = self.data
    
    # Calcular medias
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calcular numerador: suma de (x_i - mean_x) * (y_i - mean_y)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    # Calcular denominador: sqrt(suma de (x_i - mean_x)^2) * sqrt(suma de (y_i - mean_y)^2)
    sum_sq_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    denominator = math.sqrt(sum_sq_x * sum_sq_y)
    
    if denominator == 0:
        return 0.0
    
    correlation = numerator / denominator
    
    return correlation
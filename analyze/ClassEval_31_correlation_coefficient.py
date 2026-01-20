def correlation_coefficient(data1, data2):
    """
    Calcular el coeficiente de correlación de dos conjuntos de datos.
    :param data1: El primer conjunto de datos, lista.
    :param data2: El segundo conjunto de datos, lista.
    :return: El coeficiente de correlación, float.
    >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
    0.9999999999999998

    """
    n = len(data1)
    
    # Calculate means
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    
    # Calculate numerator: sum of (xi - mean1) * (yi - mean2)
    numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
    
    # Calculate denominator: sqrt(sum of (xi - mean1)^2) * sqrt(sum of (yi - mean2)^2)
    sum_sq1 = sum((x - mean1) ** 2 for x in data1)
    sum_sq2 = sum((y - mean2) ** 2 for y in data2)
    denominator = (sum_sq1 ** 0.5) * (sum_sq2 ** 0.5)
    
    # Return Pearson correlation coefficient
    return numerator / denominator
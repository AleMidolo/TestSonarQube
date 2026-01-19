@staticmethod
def kurtosis(data):
    """
    Calcular la curtosis de un conjunto de datos.
    :param data: La lista de datos de entrada, lista.
    :return: La curtosis, float.
    >>> DataStatistics4.kurtosis([1, 20, 100])
    -1.5000000000000007

    """
    n = len(data)
    if n < 4:
        raise ValueError("Se necesitan al menos 4 datos para calcular la curtosis")
    
    # Calcular la media
    mean = sum(data) / n
    
    # Calcular la desviación estándar
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    if std_dev == 0:
        raise ValueError("La desviación estándar es cero")
    
    # Calcular el cuarto momento central
    fourth_moment = sum((x - mean) ** 4 for x in data) / n
    
    # Calcular la curtosis (exceso de curtosis)
    kurt = (fourth_moment / (variance ** 2)) - 3
    
    return kurt
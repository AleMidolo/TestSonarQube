def mode(self, data):
    """
    Calcular la moda de un conjunto de datos
    :param data: list, lista de datos
    :return: float, la moda
    >>> ds = DataStatistics()
    >>> ds.mode([2, 2, 3, 3, 4])
    [2, 3]
    """
    if not data:
        return []
    
    # Contar la frecuencia de cada valor
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    
    # Encontrar la frecuencia máxima
    max_frequency = max(frequency.values())
    
    # Obtener todos los valores con la frecuencia máxima
    modes = [key for key, freq in frequency.items() if freq == max_frequency]
    
    # Ordenar los modos
    modes.sort()
    
    return modes
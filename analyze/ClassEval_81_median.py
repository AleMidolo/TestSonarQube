def median(data):
    """
    calcula la mediana de la lista dada.
    :param data: la lista dada, lista.
    :return: la mediana de la lista dada, float.
    >>> statistics3 = Statistics3()
    >>> statistics3.median([1, 2, 3, 4])
    2.5

    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # Si la cantidad de elementos es par, promedio de los dos del medio
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        # Si la cantidad de elementos es impar, elemento del medio
        return float(sorted_data[n // 2])
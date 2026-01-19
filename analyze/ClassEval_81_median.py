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
        # Si la lista tiene un número par de elementos, la mediana es el promedio de los dos elementos centrales
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        # Si la lista tiene un número impar de elementos, la mediana es el elemento central
        return float(sorted_data[n // 2])
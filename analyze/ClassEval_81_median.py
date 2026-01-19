def median(data):
    """
    calcola la mediana della lista fornita.
    :param data: la lista fornita, lista.
    :return: la mediana della lista fornita, float.
    >>> statistics3 = Statistics3()
    >>> statistics3.median([1, 2, 3, 4])
    2.5

    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # Se la lunghezza è pari, la mediana è la media dei due valori centrali
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2.0
    else:
        # Se la lunghezza è dispari, la mediana è il valore centrale
        return float(sorted_data[n // 2])
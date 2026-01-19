def median(self, data):
    """
        Calcular la mediana de un grupo de datos, con precision de dos dígitos después del separador decimal
        :param data:list, lista de datos
        :return:float, el valor de la mediana
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        median_value = sorted_data[n // 2]
    else:
        median_value = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    return round(median_value, 2)
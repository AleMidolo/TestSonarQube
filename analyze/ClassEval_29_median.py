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
    mid = n // 2
    if n % 2 == 0:
        return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
    else:
        return round(sorted_data[mid], 2)
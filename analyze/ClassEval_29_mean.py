def mean(self, data):
    """
    Calcular el valor promedio de un grupo de datos, con precision de dos dígitos después del separador decimal
    :param data: list, lista de datos
    :return: float, el valor medio
    >>> ds = DataStatistics()
    >>> ds.mean([1, 2, 3, 4, 5])
    3.00
    """
    if not data:
        return 0.00
    
    return round(sum(data) / len(data), 2)
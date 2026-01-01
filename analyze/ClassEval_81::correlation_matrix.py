@staticmethod
def correlation_matrix(data):
    """
        calcula la matriz de correlación de la lista dada.
        :param data: la lista dada, lista.
        :return: la matriz de correlación de la lista dada, lista.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
    n = len(data)
    if n == 0:
        return []
    row_length = len(data[0])
    for row in data:
        if len(row) != row_length:
            raise ValueError('All rows must have the same length')
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1.0)
            else:
                corr = Statistics3.correlation(data[i], data[j])
                row.append(corr if corr is not None else 0.0)
        matrix.append(row)
    return matrix
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
    if any((len(row) != row_length for row in data)):
        raise ValueError('All rows must have the same length')
    corr_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        corr_matrix[i][i] = 1.0
        for j in range(i + 1, n):
            corr = Statistics3.correlation(data[i], data[j])
            if corr is None:
                corr_matrix[i][j] = 0.0
                corr_matrix[j][i] = 0.0
            else:
                corr_matrix[i][j] = corr
                corr_matrix[j][i] = corr
    return corr_matrix
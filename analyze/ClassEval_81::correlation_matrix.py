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
    correlation_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            correlation_matrix[i][j] = Statistics3.correlation(data[i], data[j])
    return correlation_matrix
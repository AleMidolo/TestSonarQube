@staticmethod
def correlation_matrix(data):
    """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
    n = len(data)
    if n == 0:
        return []
    row_length = len(data[0])
    if not all((len(row) == row_length for row in data)):
        raise ValueError('All rows must have the same length')
    corr_matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                corr_matrix[i][j] = 1.0
            else:
                corr = Statistics3.correlation(data[i], data[j])
                corr_matrix[i][j] = corr if corr is not None else 0.0
    return corr_matrix
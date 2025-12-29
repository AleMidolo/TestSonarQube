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
    m = len(data[0])
    correlation_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            correlation_matrix[i][j] = Statistics3.correlation(data[i], data[j])
    return correlation_matrix
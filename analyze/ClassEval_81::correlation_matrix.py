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
    correlation_matrix = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            correlation_matrix[i][j] = Statistics3.correlation([row[i] for row in data], [row[j] for row in data])
    return correlation_matrix
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
    correlation_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(Statistics3.correlation(data[i], data[j]))
        correlation_matrix.append(row)
    return correlation_matrix
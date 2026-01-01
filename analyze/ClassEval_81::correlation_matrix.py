@staticmethod
def correlation_matrix(data):
    """
        计算给定列表的相关性矩阵。
        :param data: 给定的列表，列表。
        :return: 给定列表的相关性矩阵，列表。
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
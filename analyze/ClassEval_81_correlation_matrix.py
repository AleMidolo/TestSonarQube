@staticmethod
def correlation_matrix(data):
    """
        दिए गए सूची का सहसंबंध मैट्रिक्स की गणना करता है।
        :param data: दी गई सूची, सूची।
        :return: दी गई सूची का सहसंबंध मैट्रिक्स, सूची।
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
    n = len(data)
    if n == 0:
        return []
    first_len = len(data[0])
    for i in range(1, n):
        if len(data[i]) != first_len:
            raise ValueError('All lists in data must have the same length')
    corr_matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                corr_matrix[i][j] = 1.0
            elif i < j:
                corr = Statistics3.correlation(data[i], data[j])
                corr_matrix[i][j] = corr if corr is not None else 0.0
                corr_matrix[j][i] = corr_matrix[i][j]
    return corr_matrix
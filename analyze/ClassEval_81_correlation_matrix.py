@staticmethod
def correlation_matrix(data):
    """
        calcola la matrice di correlazione della lista fornita.
        :param data: la lista fornita, lista.
        :return: la matrice di correlazione della lista fornita, lista.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
    n = len(data)
    correlation_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(Statistics3.correlation(data[i], data[j]))
        correlation_matrix.append(row)
    return correlation_matrix
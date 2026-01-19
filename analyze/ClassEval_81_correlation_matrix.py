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
    import numpy as np
    return np.corrcoef(data)
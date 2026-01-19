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
    import numpy as np
    return np.corrcoef(data)
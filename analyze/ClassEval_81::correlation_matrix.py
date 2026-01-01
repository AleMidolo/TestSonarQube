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
    import numpy as np
    data = np.array(data)
    return np.corrcoef(data)
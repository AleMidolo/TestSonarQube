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
    import numpy as np
    data_array = np.array(data)
    correlation_matrix = np.corrcoef(data_array)
    return correlation_matrix.tolist()
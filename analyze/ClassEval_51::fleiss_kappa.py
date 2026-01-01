@staticmethod
def fleiss_kappa(testData, N, k, n):
    """
        计算 N * k 矩阵的 Fleiss kappa 值
        :param testData: 输入数据矩阵，N * k
        :param N: int, 样本数量
        :param k: int, 类别数量
        :param n: int, 评分者数量
        :return: float, Fleiss kappa 值
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                              [0, 2, 6, 4, 2],
        >>>                              [0, 0, 3, 5, 6],
        >>>                              [0, 3, 9, 2, 0],
        >>>                              [2, 2, 8, 1, 1],
        >>>                              [7, 7, 0, 0, 0],
        >>>                              [3, 2, 6, 3, 0],
        >>>                              [2, 5, 3, 2, 2],
        >>>                              [6, 5, 2, 1, 0],
        >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
    data = np.array(testData)
    p_j = np.sum(data, axis=0) / (N * n)
    P_i = (np.sum(data * data, axis=1) - n) / (n * (n - 1))
    P_bar = np.sum(P_i) / N
    P_e = np.sum(p_j * p_j)
    kappa = (P_bar - P_e) / (1 - P_e)
    return float(kappa)
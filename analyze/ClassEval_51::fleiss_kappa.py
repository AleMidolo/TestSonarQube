@staticmethod
def fleiss_kappa(testData, N, k, n):
    """
        Calcular el valor de kappa de Fleiss de una matriz de N * k
        :param testData: Matriz de datos de entrada, N * k
        :param N: int, Número de muestras
        :param k: int, Número de categorías
        :param n: int, Número de evaluadores
        :return: float, valor de kappa de Fleiss
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
    dataMat = np.array(testData)
    p = np.sum(dataMat, axis=0) / (N * n)
    P = np.sum(dataMat ** 2, axis=0) / (N * n) ** 2
    P_bar = np.mean(P)
    P_e = np.sum(p ** 2)
    kappa_value = (P_bar - P_e) / (1 - P_e)
    return kappa_value
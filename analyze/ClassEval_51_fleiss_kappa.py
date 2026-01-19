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
                                     [0, 2, 6, 4, 2],
                                     [0, 0, 3, 5, 6],
                                     [0, 3, 9, 2, 0],
                                     [2, 2, 8, 1, 1],
                                     [7, 7, 0, 0, 0],
                                     [3, 2, 6, 3, 0],
                                     [2, 5, 3, 2, 2],
                                     [6, 5, 2, 1, 0],
                                     [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
    p = np.sum(testData, axis=0) / (N * n)
    P = np.sum(p ** 2)
    Pe = np.sum((np.sum(testData, axis=1) / n) ** 2)
    kappa = (P - Pe) / (1 - Pe)
    return kappa
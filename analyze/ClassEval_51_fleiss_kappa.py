@staticmethod
def fleiss_kappa(testData, N, k, n):
    """
        Calcola il valore di kappa di Fleiss per una matrice N * k
        :param testData: Matrice di dati di input, N * k
        :param N: int, Numero di campioni
        :param k: int, Numero di categorie
        :param n: int, Numero di valutatori
        :return: float, valore di kappa di Fleiss
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
    P = np.sum(np.sum(testData, axis=1) * (np.sum(testData, axis=1) - 1)) / (n * (n - 1) * N)
    Pe = np.sum(p ** 2)
    kappa_value = (P - Pe) / (1 - Pe)
    return kappa_value
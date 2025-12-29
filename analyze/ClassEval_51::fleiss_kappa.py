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
    N = float(N)
    P = np.sum(dataMat, axis=0) / (N * n)
    P_bar = np.sum(P ** 2)
    P_e = np.sum(np.sum(dataMat, axis=1) ** 2) / (N * n) ** 2
    fleiss_kappa_value = (P_bar - P_e) / (1 - P_e)
    return fleiss_kappa_value
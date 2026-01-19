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
    data = np.array(testData)
    p_j = np.sum(data, axis=0) / (N * n)
    P_i = (np.sum(data ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = np.mean(P_i)
    P_e = np.sum(p_j ** 2)
    kappa = (P_bar - P_e) / (1 - P_e)
    return float(kappa)
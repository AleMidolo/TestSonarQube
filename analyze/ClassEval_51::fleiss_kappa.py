@staticmethod
def fleiss_kappa(testData, N, k, n):
    """
        Calculate the fliss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
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
    P = np.sum(dataMat, axis=0) / (N * n)
    Pbar = np.sum(dataMat ** 2, axis=0) / (N * n ** 2)
    Pbar_total = np.mean(Pbar)
    fleiss_kappa_value = (Pbar_total - np.mean(P ** 2)) / (1 - np.mean(P ** 2))
    return fleiss_kappa_value
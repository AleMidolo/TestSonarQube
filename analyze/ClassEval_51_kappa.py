@staticmethod
def kappa(testData, k):
    """
        Calcola il valore di Cohen kappa di una matrice k-dimensionale
        :param testData: La matrice k-dimensionale di cui calcolare il valore di kappa di Cohen
        :param k: int, Dimensione della matrice
        :return: float, il valore di kappa di Cohen della matrice
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
    n = np.sum(testData)
    p = np.sum(testData, axis=0) / n
    p0 = np.sum(np.diag(testData)) / n
    pe = np.sum(p ** 2)
    kappa_value = (p0 - pe) / (1 - pe)
    return kappa_value
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
    n = len(testData)
    p0 = np.sum(np.array(testData) == np.array(testData).T) / (n * (n - 1))
    pe = np.sum(np.sum(testData, axis=0) ** 2) / n ** 2
    kappa_value = (p0 - pe) / (1 - pe)
    return kappa_value
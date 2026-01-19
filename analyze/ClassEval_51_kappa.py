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
    total = sum((sum(row) for row in testData))
    p0 = sum((sum(row) * (sum(row) - 1) for row in testData)) / (n * (total * (total - 1)))
    pe = sum((sum(testData[:, j]) * sum(testData[:, j]) for j in range(k))) / (n * (total * (total - 1)))
    kappa_value = (p0 - pe) / (1 - pe) if 1 - pe != 0 else 0
    return kappa_value
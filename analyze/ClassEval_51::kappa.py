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
    p0 = 0
    for row in testData:
        total = sum(row)
        p0 += sum([x * (x - 1) for x in row]) / (total * (total - 1))
    p0 /= n
    p = np.array([sum(col) for col in zip(*testData)]) / (n * k)
    pe = sum(p ** 2)
    kappa_value = (p0 - pe) / (1 - pe) if 1 - pe != 0 else 0
    return kappa_value
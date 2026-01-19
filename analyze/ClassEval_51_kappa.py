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
    data = np.array(testData, dtype=float)
    total = np.sum(data)
    Po = np.trace(data) / total
    row_sums = np.sum(data, axis=1)
    col_sums = np.sum(data, axis=0)
    Pe = np.sum(row_sums * col_sums) / total ** 2
    if Pe == 1:
        return 1.0 if Po == 1 else 0.0
    else:
        kappa_value = (Po - Pe) / (1 - Pe)
        return float(kappa_value)
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
    matrix = np.array(testData, dtype=float)
    total = np.sum(matrix)
    observed_agreement = np.trace(matrix) / total
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    expected_agreement = np.sum(row_sums * col_sums) / (total * total)
    if expected_agreement == 1:
        return 1.0 if observed_agreement == 1 else 0.0
    kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    return float(kappa_value)
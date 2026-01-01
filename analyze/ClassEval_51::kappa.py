@staticmethod
def kappa(testData, k):
    """
        Calcular el valor de kappa de Cohen de una matriz k-dimensional
        :param testData: La matriz k-dimensional de la que se necesita calcular el valor de kappa de Cohen
        :param k: int, Dimensión de la matriz
        :return: float, el valor de kappa de Cohen de la matriz
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
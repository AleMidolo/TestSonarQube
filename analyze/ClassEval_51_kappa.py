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
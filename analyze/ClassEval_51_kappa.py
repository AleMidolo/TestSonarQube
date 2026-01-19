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
    n = len(testData)
    p0 = np.sum(np.array(testData) == np.array(testData).T) / (n * (n - 1))
    pe = np.sum(np.sum(testData, axis=0) ** 2) / n ** 2
    kappa_value = (p0 - pe) / (1 - pe)
    return kappa_value
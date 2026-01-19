@staticmethod
def kappa(testData, k):
    """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
    n = np.sum(testData)
    p0 = np.sum(np.diag(testData)) / n
    pe = np.sum(np.sum(testData, axis=0) ** 2) / n ** 2
    kappa_value = (p0 - pe) / (1 - pe) if 1 - pe != 0 else 0
    return kappa_value
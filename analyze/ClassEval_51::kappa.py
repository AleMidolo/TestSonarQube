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
    p = np.sum(testData, axis=0) / n
    p0 = np.sum(np.diag(testData)) / n
    pe = np.sum(p ** 2)
    kappa_value = (p0 - pe) / (1 - pe)
    return kappa_value
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
    dataMat = np.array(testData)
    n = np.sum(dataMat)
    p0 = np.sum(np.max(dataMat, axis=1)) / n
    pe = np.sum((np.sum(dataMat, axis=0) / n) ** 2)
    kappa_value = (p0 - pe) / (1 - pe)
    return kappa_value
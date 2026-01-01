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
    total = np.sum(dataMat)
    p0 = np.sum(np.diag(dataMat)) / total
    pe = np.sum(np.sum(dataMat, axis=0) / total * (np.sum(dataMat, axis=1) / total))
    kappa_value = (p0 - pe) / (1 - pe) if 1 - pe != 0 else 0
    return kappa_value
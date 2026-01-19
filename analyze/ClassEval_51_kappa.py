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
    dataMat = np.array(testData, dtype=float)
    total = np.sum(dataMat)
    P0 = np.trace(dataMat) / total
    row_sums = np.sum(dataMat, axis=1)
    col_sums = np.sum(dataMat, axis=0)
    Pe = np.sum(row_sums * col_sums) / total ** 2
    kappa_value = (P0 - Pe) / (1 - Pe)
    return kappa_value
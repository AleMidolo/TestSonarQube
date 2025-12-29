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
    Po = np.trace(dataMat) / total
    row_sums = np.sum(dataMat, axis=1)
    col_sums = np.sum(dataMat, axis=0)
    Pe = np.sum(row_sums * col_sums) / (total * total)
    if Pe == 1:
        return 1.0 if Po == 1 else 0.0
    kappa_value = (Po - Pe) / (1 - Pe)
    return kappa_value
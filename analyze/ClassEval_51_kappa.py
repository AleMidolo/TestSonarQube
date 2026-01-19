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
    po = np.trace(dataMat) / total
    row_sums = np.sum(dataMat, axis=1)
    col_sums = np.sum(dataMat, axis=0)
    pe = np.sum(row_sums * col_sums) / (total * total)
    if pe == 1:
        return 1.0 if po == 1 else 0.0
    kappa_val = (po - pe) / (1 - pe)
    return kappa_val
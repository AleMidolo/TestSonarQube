@staticmethod
def kappa(testData, k):
    """
        Calcola il valore di Cohen kappa di una matrice k-dimensionale
        :param testData: La matrice k-dimensionale di cui calcolare il valore di kappa di Cohen
        :param k: int, Dimensione della matrice
        :return: float, il valore di kappa di Cohen della matrice
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
    n = len(testData)
    p0 = np.sum(np.array(testData) == np.max(testData, axis=1, keepdims=True), axis=1) / n
    p1 = np.sum(np.array(testData) / np.sum(testData, axis=1, keepdims=True), axis=0) / n
    p0_mean = np.mean(p0)
    p1_mean = np.mean(p1)
    kappa_value = (p0_mean - p1_mean) / (1 - p1_mean)
    return kappa_value
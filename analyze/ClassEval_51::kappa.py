@staticmethod
def kappa(testData, k):
    """
        计算k维矩阵的Cohen's kappa值
        :param testData: 需要计算Cohen's kappa值的k维矩阵
        :param k: int, 矩阵维度
        :return: float, 矩阵的Cohen's kappa值
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
    n = len(testData)
    p0 = 0.0
    p1 = 0.0
    for i in range(n):
        total = sum(testData[i])
        p0 += total * (total - 1) / (n * (n - 1))
        for j in range(k):
            p1 += testData[i][j] * (testData[i][j] - 1) / (n * (n - 1))
    p0 /= n
    p1 /= n
    kappa_value = (p0 - p1) / (1 - p1) if 1 - p1 != 0 else 0
    return kappa_value
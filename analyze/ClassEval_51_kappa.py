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
    total = sum((sum(row) for row in testData))
    p0 = sum((sum(row) ** 2 for row in testData)) / total ** 2
    pe = sum((sum((testData[i][j] for i in range(n))) ** 2 for j in range(k))) / total ** 2
    kappa_value = (p0 - pe) / (1 - pe) if 1 - pe != 0 else 0
    return kappa_value
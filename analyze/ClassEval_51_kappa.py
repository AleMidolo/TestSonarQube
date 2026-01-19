def kappa(testData, k):
    """
    计算k维矩阵的Cohen's kappa值
    :param testData: 需要计算Cohen's kappa值的k维矩阵
    :param k: int, 矩阵维度
    :return: float, 矩阵的Cohen's kappa值
    >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
    0.25
    """
    # Calculate the total number of observations
    n = sum(sum(row) for row in testData)
    
    # Calculate observed agreement (Po)
    po = sum(testData[i][i] for i in range(k)) / n
    
    # Calculate expected agreement (Pe)
    row_sums = [sum(testData[i]) for i in range(k)]
    col_sums = [sum(testData[i][j] for i in range(k)) for j in range(k)]
    
    pe = sum(row_sums[i] * col_sums[i] for i in range(k)) / (n * n)
    
    # Calculate Cohen's kappa
    if pe == 1:
        return 0.0
    
    kappa_value = (po - pe) / (1 - pe)
    
    return round(kappa_value, 2)
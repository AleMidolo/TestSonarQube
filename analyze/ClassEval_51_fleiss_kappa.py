@staticmethod
def fleiss_kappa(testData, N, k, n):
    """
    Calculate the fliss kappa value of an N * k matrix
    :param testData: Input data matrix, N * k
    :param N: int, Number of samples
    :param k: int, Number of categories
    :param n: int, Number of raters
    :return: float, fleiss kappa value
    >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
    >>>                              [0, 2, 6, 4, 2],
    >>>                              [0, 0, 3, 5, 6],
    >>>                              [0, 3, 9, 2, 0],
    >>>                              [2, 2, 8, 1, 1],
    >>>                              [7, 7, 0, 0, 0],
    >>>                              [3, 2, 6, 3, 0],
    >>>                              [2, 5, 3, 2, 2],
    >>>                              [6, 5, 2, 1, 0],
    >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
    0.20993070442195522
    """
    # Calculate P_i (proportion of agreement for each subject)
    P_i_sum = 0.0
    for i in range(N):
        sum_sq = 0.0
        for j in range(k):
            sum_sq += testData[i][j] ** 2
        P_i = (sum_sq - n) / (n * (n - 1))
        P_i_sum += P_i
    
    # Calculate P_bar (mean of P_i values)
    P_bar = P_i_sum / N
    
    # Calculate P_e (expected agreement by chance)
    P_e = 0.0
    for j in range(k):
        sum_col = 0.0
        for i in range(N):
            sum_col += testData[i][j]
        p_j = sum_col / (N * n)
        P_e += p_j ** 2
    
    # Calculate Fleiss' kappa
    kappa = (P_bar - P_e) / (1 - P_e)
    
    return kappa
@staticmethod
def fleiss_kappa(testData, N, k, n):
    """
    Calcular el valor de kappa de Fleiss de una matriz de N * k
    :param testData: Matriz de datos de entrada, N * k
    :param N: int, Número de muestras
    :param k: int, Número de categorías
    :param n: int, Número de evaluadores
    :return: float, valor de kappa de Fleiss
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
    
    # Calculate P_j (proportion of ratings in each category)
    P_j_sum = 0.0
    for j in range(k):
        n_j = 0.0
        for i in range(N):
            n_j += testData[i][j]
        P_j = n_j / (N * n)
        P_j_sum += P_j ** 2
    
    # Calculate P_e_bar (expected agreement by chance)
    P_e_bar = P_j_sum
    
    # Calculate Fleiss' kappa
    kappa = (P_bar - P_e_bar) / (1 - P_e_bar)
    
    return kappa
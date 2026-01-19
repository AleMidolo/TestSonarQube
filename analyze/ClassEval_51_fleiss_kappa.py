@staticmethod
def fleiss_kappa(testData, N, k, n):
    """
    N × k मैट्रिक्स की Fleiss' kappa वैल्यू कैलकुलेट करें।

    :param testData: इनपुट डेटा मैट्रिक्स (N × k)
    :param N: int, सैंपल की संख्या
    :param k: int, कैटेगरी की संख्या
    :param n: int, रेट करने वालों की संख्या
    :return: float, Fleiss' kappa वैल्यू

    >>> KappaCalculator.fleiss_kappa(
    ...     [
    ...         [0, 0, 0, 0, 14],
    ...         [0, 2, 6, 4, 2],
    ...         [0, 0, 3, 5, 6],
    ...         [0, 3, 9, 2, 0],
    ...         [2, 2, 8, 1, 1],
    ...         [7, 7, 0, 0, 0],
    ...         [3, 2, 6, 3, 0],
    ...         [2, 5, 3, 2, 2],
    ...         [6, 5, 2, 1, 0],
    ...         [0, 2, 2, 3, 7]
    ...     ],
    ...     10, 5, 14
    ... )
    0.20993070442195522
    """
    # Step 1: Calculate P_i (proportion of agreement for each subject)
    P_i_sum = 0.0
    for i in range(N):
        sum_sq = 0.0
        for j in range(k):
            sum_sq += testData[i][j] ** 2
        P_i = (sum_sq - n) / (n * (n - 1))
        P_i_sum += P_i
    
    # Step 2: Calculate P_bar (mean of P_i values)
    P_bar = P_i_sum / N
    
    # Step 3: Calculate P_j (proportion of ratings in each category)
    P_j_sum = 0.0
    for j in range(k):
        sum_category = 0.0
        for i in range(N):
            sum_category += testData[i][j]
        P_j = sum_category / (N * n)
        P_j_sum += P_j ** 2
    
    # Step 4: Calculate P_e_bar (expected agreement by chance)
    P_e_bar = P_j_sum
    
    # Step 5: Calculate Fleiss' kappa
    kappa = (P_bar - P_e_bar) / (1 - P_e_bar)
    
    return kappa
def kappa(testData, k):
    """
    Calcola il valore di Cohen kappa di una matrice k-dimensionale
    :param testData: La matrice k-dimensionale di cui calcolare il valore di kappa di Cohen
    :param k: int, Dimensione della matrice
    :return: float, il valore di kappa di Cohen della matrice
    >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
    0.25
    """
    # Calculate total number of observations
    n = sum(sum(row) for row in testData)
    
    # Calculate observed agreement (Po)
    po = sum(testData[i][i] for i in range(k)) / n
    
    # Calculate expected agreement (Pe)
    # Sum of row totals * column totals / n^2
    row_totals = [sum(testData[i]) for i in range(k)]
    col_totals = [sum(testData[i][j] for i in range(k)) for j in range(k)]
    
    pe = sum(row_totals[i] * col_totals[i] for i in range(k)) / (n * n)
    
    # Calculate Cohen's kappa
    if pe == 1:
        return 0.0
    
    kappa_value = (po - pe) / (1 - pe)
    
    return round(kappa_value, 2)
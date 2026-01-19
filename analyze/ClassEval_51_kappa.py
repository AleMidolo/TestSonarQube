def kappa(testData, k):
    """
    Calcular el valor de kappa de Cohen de una matriz k-dimensional
    :param testData: La matriz k-dimensional de la que se necesita calcular el valor de kappa de Cohen
    :param k: int, Dimensión de la matriz
    :return: float, el valor de kappa de Cohen de la matriz
    >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
    0.25
    """
    # Calculate total number of observations
    n = sum(sum(row) for row in testData)
    
    # Calculate observed agreement (Po)
    # Sum of diagonal elements divided by total
    observed_agreement = sum(testData[i][i] for i in range(k)) / n
    
    # Calculate expected agreement (Pe)
    # Sum of (row_total * col_total) / n^2 for each category
    row_sums = [sum(testData[i]) for i in range(k)]
    col_sums = [sum(testData[i][j] for i in range(k)) for j in range(k)]
    
    expected_agreement = sum(row_sums[i] * col_sums[i] for i in range(k)) / (n * n)
    
    # Calculate Cohen's kappa
    # kappa = (Po - Pe) / (1 - Pe)
    if expected_agreement == 1:
        return 0.0
    
    kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    
    return round(kappa_value, 2)
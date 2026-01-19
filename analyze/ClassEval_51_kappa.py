def kappa(testData, k):
    """
    Calculate the cohens kappa value of a k-dimensional matrix
    :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
    :param k: int, Matrix dimension
    :return:float, the cohens kappa value of the matrix
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
    row_totals = [sum(testData[i]) for i in range(k)]
    col_totals = [sum(testData[i][j] for i in range(k)) for j in range(k)]
    
    expected_agreement = sum(row_totals[i] * col_totals[i] for i in range(k)) / (n * n)
    
    # Calculate Cohen's Kappa
    # kappa = (Po - Pe) / (1 - Pe)
    if expected_agreement == 1:
        return 0.0
    
    kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    
    return round(kappa_value, 2)
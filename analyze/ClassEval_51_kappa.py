def kappa(testData, k):
    """
    कोहेन का काप्पा मान एक k-आयामी मैट्रिक्स का गणना करें
    :param testData: वह k-आयामी मैट्रिक्स जिसके लिए कोहेन का काप्पा मान निकालना है
    :param k: int, मैट्रिक्स का आयाम
    :return: float, मैट्रिक्स का कोहेन का काप्पा मान
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
    
    # Calculate Cohen's Kappa
    # kappa = (Po - Pe) / (1 - Pe)
    if expected_agreement == 1:
        return 0.0
    
    kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    
    return round(kappa_value, 2)
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
    po = sum(testData[i][i] for i in range(k)) / n
    
    # Calculate expected agreement (Pe)
    # Sum of row totals
    row_sums = [sum(testData[i]) for i in range(k)]
    # Sum of column totals
    col_sums = [sum(testData[i][j] for i in range(k)) for j in range(k)]
    
    # Calculate expected agreement
    pe = sum(row_sums[i] * col_sums[i] for i in range(k)) / (n * n)
    
    # Calculate Cohen's Kappa
    if pe == 1:
        return 0.0
    
    kappa_value = (po - pe) / (1 - pe)
    
    return kappa_value
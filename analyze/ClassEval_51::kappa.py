@staticmethod
def kappa(testData, k):
    """
        कोहेन का काप्पा मान एक k-आयामी मैट्रिक्स का गणना करें
        :param testData: वह k-आयामी मैट्रिक्स जिसके लिए कोहेन का काप्पा मान निकालना है
        :param k: int, मैट्रिक्स का आयाम
        :return: float, मैट्रिक्स का कोहेन का काप्पा मान
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
    matrix = np.array(testData, dtype=float)
    total = np.sum(matrix)
    observed_agreement = np.trace(matrix) / total
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    expected_agreement = np.sum(row_sums * col_sums) / (total * total)
    if expected_agreement == 1:
        return 1.0 if observed_agreement == 1 else 0.0
    kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    return float(kappa_value)
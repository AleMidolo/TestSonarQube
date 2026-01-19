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
    data = np.array(testData, dtype=float)
    total = np.sum(data)
    Po = np.trace(data) / total
    row_sums = np.sum(data, axis=1)
    col_sums = np.sum(data, axis=0)
    Pe = np.sum(row_sums * col_sums) / total ** 2
    kappa_value = (Po - Pe) / (1 - Pe)
    return kappa_value
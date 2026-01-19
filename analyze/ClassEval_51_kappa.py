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
    n = np.sum(testData)
    p = np.sum(testData, axis=0) / n
    p0 = np.sum(np.diag(np.dot(testData, testData.T))) / n
    pe = np.sum(p ** 2)
    kappa_value = (p0 - pe) / (1 - pe)
    return kappa_value
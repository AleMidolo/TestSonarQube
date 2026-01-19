def f1_score(self, predicted_labels, true_labels):
    """
    f1 स्कोर की गणना करें, जो प्रिसिजन और रिकॉल का हार्मोनिक माध्य है
    :param predicted_labels: सूची, पूर्वानुमानित परिणाम
    :param true_labels: सूची, सत्य लेबल
    :return: फ्लोट
    >>> mc = MetricsCalculator()
    >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    precision_value = self.precision(predicted_labels, true_labels)
    recall_value = self.recall(predicted_labels, true_labels)
    if precision_value + recall_value == 0:
        return 0.0
    return 2 * (precision_value * recall_value) / (precision_value + recall_value)
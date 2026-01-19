def accuracy(self, predicted_labels, true_labels):
    """
        सटीकता की गणना करें
        :param predicted_labels: सूची, पूर्वानुमानित परिणाम
        :param true_labels: सूची, सही लेबल
        :return: फ्लोट
        >>> mc = MetricsCalculator()
        >>> mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
    self.update(predicted_labels, true_labels)
    total = len(predicted_labels)
    if total == 0:
        return 0.0
    return (self.true_positives + self.true_negatives) / total
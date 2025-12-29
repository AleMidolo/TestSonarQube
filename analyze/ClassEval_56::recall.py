def recall(self, predicted_labels, true_labels):
    """
        पुनः प्राप्ति की गणना करें
        :param predicted_labels: सूची, पूर्वानुमानित परिणाम
        :param true_labels: सूची, सही लेबल
        :return: फ्लोट
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
    self.update(predicted_labels, true_labels)
    if self.true_positives + self.false_negatives == 0:
        return 0.0
    return self.true_positives / (self.true_positives + self.false_negatives)
def accuracy(self, predicted_labels=None, true_labels=None):
    """
        Calculate accuracy
        :param predicted_labels: list, predicted results (optional if update was already called)
        :param true_labels: list, true labels (optional if update was already called)
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
    if predicted_labels is not None and true_labels is not None:
        self.update(predicted_labels, true_labels)
    total = self.true_positives + self.false_positives + self.false_negatives + self.true_negatives
    if total == 0:
        return 0.0
    return (self.true_positives + self.true_negatives) / total
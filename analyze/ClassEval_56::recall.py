def recall(self, predicted_labels, true_labels):
    """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
    self.update(predicted_labels, true_labels)
    if self.true_positives + self.false_negatives == 0:
        return 0.0
    return self.true_positives / (self.true_positives + self.false_negatives)
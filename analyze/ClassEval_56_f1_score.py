def f1_score(self, predicted_labels, true_labels):
    """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
    prec = self.precision(predicted_labels, true_labels)
    rec = self.recall(predicted_labels, true_labels)
    if prec + rec == 0:
        return 0.0
    return 2 * (prec * rec) / (prec + rec)
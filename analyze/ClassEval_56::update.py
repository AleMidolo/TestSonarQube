def update(self, predicted_labels, true_labels):
    """
        Update the number of all four samples (true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, modifies the count of corresponding samples
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
    for pred, true in zip(predicted_labels, true_labels):
        if pred == 1 and true == 1:
            self.true_positives += 1
        elif pred == 1 and true == 0:
            self.false_positives += 1
        elif pred == 0 and true == 1:
            self.false_negatives += 1
        elif pred == 0 and true == 0:
            self.true_negatives += 1
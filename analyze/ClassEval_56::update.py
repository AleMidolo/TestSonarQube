def update(self, predicted_labels, true_labels):
    """
        Update the number of all four samples (true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, modifies the count of the corresponding samples
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
    for p, t in zip(predicted_labels, true_labels):
        if p == 1 and t == 1:
            self.true_positives += 1
        elif p == 1 and t == 0:
            self.false_positives += 1
        elif p == 0 and t == 1:
            self.false_negatives += 1
        elif p == 0 and t == 0:
            self.true_negatives += 1
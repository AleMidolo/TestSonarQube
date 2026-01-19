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
    true_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    false_negatives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 0 and true == 1)
    
    if true_positives + false_negatives == 0:
        return 0.0
    
    return true_positives / (true_positives + false_negatives)
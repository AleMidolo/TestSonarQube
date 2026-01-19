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
    # Calculate true positives, false positives, and false negatives
    true_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    false_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 0)
    false_negatives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 0 and true == 1)
    
    # Calculate precision
    if true_positives + false_positives == 0:
        precision = 0
    else:
        precision = true_positives / (true_positives + false_positives)
    
    # Calculate recall
    if true_positives + false_negatives == 0:
        recall = 0
    else:
        recall = true_positives / (true_positives + false_negatives)
    
    # Calculate F1 score
    if precision + recall == 0:
        return 0.0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)
        return f1
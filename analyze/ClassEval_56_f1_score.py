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
    # Calculate True Positives, False Positives, and False Negatives
    tp = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    fp = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 0)
    fn = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 0 and true == 1)
    
    # Calculate precision and recall
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    # Calculate F1 score (harmonic mean of precision and recall)
    if precision + recall == 0:
        return 0.0
    
    f1 = 2 * (precision * recall) / (precision + recall)
    
    return f1
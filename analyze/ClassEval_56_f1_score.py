def f1_score(self, predicted_labels, true_labels):
    """
    f1 स्कोर की गणना करें, जो प्रिसिजन और रिकॉल का हार्मोनिक माध्य है
    :param predicted_labels: सूची, पूर्वानुमानित परिणाम
    :param true_labels: सूची, सत्य लेबल
    :return: फ्लोट
    >>> mc = MetricsCalculator()
    >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    # Calculate True Positives, False Positives, and False Negatives
    true_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    false_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 0)
    false_negatives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 0 and true == 1)
    
    # Calculate Precision
    if true_positives + false_positives == 0:
        precision = 0
    else:
        precision = true_positives / (true_positives + false_positives)
    
    # Calculate Recall
    if true_positives + false_negatives == 0:
        recall = 0
    else:
        recall = true_positives / (true_positives + false_negatives)
    
    # Calculate F1 Score
    if precision + recall == 0:
        return 0.0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)
        return f1
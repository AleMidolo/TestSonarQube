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
    true_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    false_negatives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 0 and true == 1)
    
    if true_positives + false_negatives == 0:
        return 0.0
    
    return true_positives / (true_positives + false_negatives)
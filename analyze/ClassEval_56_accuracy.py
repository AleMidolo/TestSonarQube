def accuracy(self, predicted_labels, true_labels):
    """
    सटीकता की गणना करें
    :param predicted_labels: सूची, पूर्वानुमानित परिणाम
    :param true_labels: सूची, सही लेबल
    :return: फ्लोट
    >>> mc = MetricsCalculator()
    >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    if len(predicted_labels) != len(true_labels):
        raise ValueError("Lists must have the same length")
    
    if len(predicted_labels) == 0:
        return 0.0
    
    correct = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == true)
    return correct / len(predicted_labels)
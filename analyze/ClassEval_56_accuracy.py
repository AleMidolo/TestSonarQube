def accuracy(self, predicted_labels, true_labels):
    """
    Calculate accuracy
    :param predicted_labels: list, predicted results
    :param true_labels: list, true labels
    :return: float
    >>> mc = MetricsCalculator()
    >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    if len(predicted_labels) != len(true_labels):
        raise ValueError("predicted_labels and true_labels must have the same length")
    
    if len(predicted_labels) == 0:
        return 0.0
    
    correct = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == true)
    return correct / len(predicted_labels)
def recall(self, predicted_labels, true_labels):
    """
    计算召回率
    :param predicted_labels: list, 预测结果
    :param true_labels: list, 真实标签
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    if len(predicted_labels) != len(true_labels):
        raise ValueError("predicted_labels and true_labels must have the same length")
    
    true_positives = 0
    actual_positives = 0
    
    for pred, true in zip(predicted_labels, true_labels):
        if true == 1:
            actual_positives += 1
            if pred == 1:
                true_positives += 1
    
    if actual_positives == 0:
        return 0.0
    
    return true_positives / actual_positives
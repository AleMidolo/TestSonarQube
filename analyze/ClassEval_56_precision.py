def precision(self, predicted_labels, true_labels):
    """
    计算精确率
    :param predicted_labels: list, 预测结果
    :param true_labels: list, 真实标签
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    if len(predicted_labels) != len(true_labels):
        raise ValueError("predicted_labels and true_labels must have the same length")
    
    # Calculate True Positives (TP)
    true_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) 
                        if pred == 1 and true == 1)
    
    # Calculate all Positive predictions (TP + FP)
    predicted_positives = sum(predicted_labels)
    
    # Precision = TP / (TP + FP)
    if predicted_positives == 0:
        return 0.0
    
    return true_positives / predicted_positives
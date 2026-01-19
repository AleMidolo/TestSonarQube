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
    true_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    predicted_positives = sum(1 for pred in predicted_labels if pred == 1)
    
    if predicted_positives == 0:
        return 0.0
    
    return true_positives / predicted_positives
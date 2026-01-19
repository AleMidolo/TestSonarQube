def f1_score(self, predicted_labels, true_labels):
    """
    计算 f1 分数，也就是精确度和召回率的调和平均数
    :param predicted_labels: list, 预测结果
    :param true_labels: list, 真实标签
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    precision_value = self.precision(predicted_labels, true_labels)
    recall_value = self.recall(predicted_labels, true_labels)
    if precision_value + recall_value == 0:
        return 0.0
    return 2 * (precision_value * recall_value) / (precision_value + recall_value)
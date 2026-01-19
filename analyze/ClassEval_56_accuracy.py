def accuracy(self, predicted_labels, true_labels):
    """
    计算准确率
    :param predicted_labels: list, 预测结果
    :param true_labels: list, 真实标签
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    self.update(predicted_labels, true_labels)
    total_samples = self.true_positives + self.false_positives + self.false_negatives + self.true_negatives
    if total_samples == 0:
        return 0.0
    return (self.true_positives + self.true_negatives) / total_samples
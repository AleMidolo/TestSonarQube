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
    self.update(predicted_labels, true_labels)
    if self.true_positives + self.false_positives == 0:
        return 0.0
    return self.true_positives / (self.true_positives + self.false_positives)
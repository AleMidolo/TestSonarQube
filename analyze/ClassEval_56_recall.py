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
    self.update(predicted_labels, true_labels)
    if self.true_positives + self.false_negatives == 0:
        return 0.0
    return self.true_positives / (self.true_positives + self.false_negatives)
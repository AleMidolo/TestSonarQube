def update(self, predicted_labels, true_labels):
    """
        更新四类样本数量（true_positives、false_positives、false_negatives、true_negatives）
        :param predicted_labels: list, 预测结果
        :param true_labels: list, 真实标签
        :return: None, 更改相应样本的数量
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
    if len(predicted_labels) != len(true_labels):
        raise ValueError('predicted_labels and true_labels must have the same length')
    for pred, true in zip(predicted_labels, true_labels):
        if pred == 1 and true == 1:
            self.true_positives += 1
        elif pred == 1 and true == 0:
            self.false_positives += 1
        elif pred == 0 and true == 1:
            self.false_negatives += 1
        elif pred == 0 and true == 0:
            self.true_negatives += 1
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
    # 计算 True Positives, False Positives, False Negatives
    tp = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    fp = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 0)
    fn = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 0 and true == 1)
    
    # 计算精确度 (Precision)
    if tp + fp == 0:
        precision = 0
    else:
        precision = tp / (tp + fp)
    
    # 计算召回率 (Recall)
    if tp + fn == 0:
        recall = 0
    else:
        recall = tp / (tp + fn)
    
    # 计算 F1 分数 (调和平均数)
    if precision + recall == 0:
        return 0.0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)
        return f1
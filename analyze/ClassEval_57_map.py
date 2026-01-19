@staticmethod
def map(data):
    """
    计算输入数据的MAP。MAP是一个广泛使用的评估指标。它是AP（平均精度）的均值。
    :param data: 数据必须是一个元组，列表 0,1，例如（[1,0,...],5）。在每个元组中（实际结果，真实标签数量），真实标签数量是总的真实数量。
    ([1,0,...],5)，
    或者元组的列表，例如 [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)]。
    1代表正确答案，0代表错误答案。
    :return: 如果输入数据是列表，则返回该列表的召回率。如果输入数据是列表的列表，则返回所有列表的平均召回率。第二个返回值是每个输入的精度列表。
    >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
    >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    0.41666666666666663, [0.41666666666666663]
    0.3333333333333333, [0.41666666666666663, 0.25]
    """
    def calculate_ap(predictions, total_relevant):
        """计算单个查询的平均精度(AP)"""
        if total_relevant == 0:
            return 0.0
        
        ap = 0.0
        num_correct = 0
        
        for i, pred in enumerate(predictions):
            if pred == 1:
                num_correct += 1
                precision_at_i = num_correct / (i + 1)
                ap += precision_at_i
        
        if total_relevant > 0:
            ap /= total_relevant
        
        return ap
    
    # 检查输入是单个元组还是元组列表
    if isinstance(data, tuple):
        # 单个元组
        predictions, total_relevant = data
        ap = calculate_ap(predictions, total_relevant)
        return ap, [ap]
    else:
        # 元组列表
        ap_list = []
        for predictions, total_relevant in data:
            ap = calculate_ap(predictions, total_relevant)
            ap_list.append(ap)
        
        mean_ap = sum(ap_list) / len(ap_list) if ap_list else 0.0
        return mean_ap, ap_list
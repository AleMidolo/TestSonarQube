def mrr(data):
    """
    计算输入数据的 MRR。MRR 是一个广泛使用的评估指标。它是倒数排名的平均值。
    :param data: 数据必须是一个元组，列表 0,1，例如（[1,0,...],5）。在每个元组中（实际结果，真实值数量），真实值数量是总的真实数量。
     ([1,0,...],5),
    或元组列表，例如 [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)]。
    1 代表正确答案，0 代表错误答案。
    :return: 如果输入数据是列表，则返回该列表的召回率。如果输入数据是列表的列表，则返回所有列表的平均召回率。第二个返回值是每个输入的精确度列表。
    >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
    >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    1.0, [1.0]
    0.75, [1.0, 0.5]
    """
    def calculate_single_mrr(result_list, total_true):
        # Find the position of the first 1 (correct answer)
        for i, val in enumerate(result_list):
            if val == 1:
                # Return reciprocal rank (1-indexed position)
                return 1.0 / (i + 1)
        # If no correct answer found, return 0
        return 0.0
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single tuple case
        result_list, total_true = data
        mrr_value = calculate_single_mrr(result_list, total_true)
        return mrr_value, [mrr_value]
    else:
        # List of tuples case
        mrr_values = []
        for result_list, total_true in data:
            mrr_value = calculate_single_mrr(result_list, total_true)
            mrr_values.append(mrr_value)
        
        # Calculate average MRR
        avg_mrr = sum(mrr_values) / len(mrr_values) if mrr_values else 0.0
        return avg_mrr, mrr_values
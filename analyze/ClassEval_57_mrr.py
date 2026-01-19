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
    if type(data) != list and type(data) != tuple:
        raise Exception('the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple')
    if len(data) == 0:
        return (0.0, [0.0])
    if type(data) == tuple:
        sub_list, total_num = data
        if total_num == 0:
            return (0.0, [0.0])
        rank = 0
        for i, value in enumerate(sub_list):
            if value == 1:
                rank = i + 1
                break
        mrr_value = 1 / rank if rank > 0 else 0
        return (mrr_value, [mrr_value])
    if type(data) == list:
        separate_result = []
        for sub_list, total_num in data:
            if total_num == 0:
                mrr_value = 0.0
            else:
                rank = 0
                for i, value in enumerate(sub_list):
                    if value == 1:
                        rank = i + 1
                        break
                mrr_value = 1 / rank if rank > 0 else 0
            separate_result.append(mrr_value)
        return (np.mean(separate_result), separate_result)
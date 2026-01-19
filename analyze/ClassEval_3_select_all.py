def select_all(self):
    """
    生成一个所有排列的列表，至少选择1个元素，最多选择内部数据的数量。
    :return: List，所有排列的列表。
    >>> ac = ArrangementCalculator([1, 2, 3])
    >>> ac.select_all()
    [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """
    from itertools import permutations
    
    result = []
    n = len(self.data)
    
    # 从选择1个元素到选择n个元素
    for r in range(1, n + 1):
        # 生成长度为r的所有排列
        for perm in permutations(self.data, r):
            result.append(list(perm))
    
    return result
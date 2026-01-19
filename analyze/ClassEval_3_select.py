def select(self, m=None):
    """
        通过从内部数据中选择 m 个元素来生成排列列表。
        如果未提供 m，则选择所有元素。
        :param m: int，选择的元素数量（默认=None）。
        :return: List，排列的列表。
        >>> ac = ArrangementCalculator([1, 2, 3, 4])
        >>> ac.select(2)
        [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]

        """
    if m is None:
        m = len(self.datas)
    result = []
    for perm in itertools.permutations(self.datas, m):
        result.append(list(perm))
    return result
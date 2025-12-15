def select_all(self):
        """
        生成一个所有排列的列表，至少选择1个元素，最多选择内部数据的数量。
        :return: List，所有排列的列表。
        >>> ac = ArrangementCalculator([1, 2, 3])
        >>> ac.select_all()
        [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        """
        result = []
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result
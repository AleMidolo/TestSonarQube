def select(self, m: int) -> List[List[str]]:
    """
        生成指定元素数量的组合。
        :param m: 每个组合中的元素数量，int。
        :return: 组合的列表，List[List[str]]。
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
    if m <= 0 or m > len(self.datas):
        return []
    result = []
    self._select(0, [None] * m, 0, result)
    return result